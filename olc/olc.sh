#!/usr/bin/env bash
# Naif yol ile akıllı yolu aynı 24 PDF üzerinde ölçer.
#
#   olc/olc.sh naif    [tekrar]   # Opus tek başına: oku, ele, adlandır, sentezle
#   olc/olc.sh akilli  [tekrar]   # /arastirma-masasi: betik + Haiku eleyici + Sonnet sentez
#   olc/olc.sh jev     [tekrar]   # aynısı, dahil/hariç kararı Jev'de (--eleyici jev; TYPESAFE_API_KEY ortamda)
#   olc/olc.sh context            # mod kapalı / açık iken /context
#
# Her koşu geçici bir klasörde, ham/ kopyası üzerinde çalışır. Sonuç satırları olc/sonuclar.jsonl'a eklenir.
# Kullanıcı ayarları ve hook'ları yüklenmez (--setting-sources project); afplay/say sessiz kopyayla gölgelenir.
set -euo pipefail

KOK="$(cd "$(dirname "$0")/.." && pwd)"
PLUGIN="$KOK/plugins/arastirma-masasi"
ANAHTAR="$KOK/ornek-makaleler/cevap-anahtari.json"
ISLER="${OLC_KLASORU:-${TMPDIR:-/tmp}/seviye-b-olc}"
SONUC="$KOK/olc/sonuclar.jsonl"
BUTCE_NAIF="${BUTCE_NAIF:-1.20}"
BUTCE_AKILLI="${BUTCE_AKILLI:-0.80}"

SORU="Uzaktan ve hibrit çalışma, bilgi çalışanlarının verimliliğini nasıl etkiliyor?"
OLCUT="Dahil ölçütleri: (1) konu uzaktan, hibrit ya da evden çalışma; (2) çalışan verimliliği ya da iş performansı ölçülüyor; (3) ampirik veri var. Biri eksikse hariç."
BICIM='{"soru": "...", "belgeler": [{"dosya": "<ham/ içindeki ad>", "yazarlar": ["Ad Soyad"], "yil": 2023, "baslik": "...", "dergi": "...", "karar": "dahil|haric", "gerekce": "tek cümle"}]}'

ORTAK=(--setting-sources project --output-format json --permission-mode acceptEdits
       --allowedTools "Read,Write,Edit,Glob,Grep,Bash,Agent")

sessiz_path() {
  mkdir -p "$ISLER/sessiz-bin"
  for k in afplay say; do printf '#!/bin/sh\nexit 0\n' > "$ISLER/sessiz-bin/$k"; chmod +x "$ISLER/sessiz-bin/$k"; done
  export PATH="$ISLER/sessiz-bin:$PATH"
}

hazirla() {  # $1 = koşu adı -> koşu klasörünü basar
  local w="$ISLER/$1"
  rm -rf "$w" && mkdir -p "$w/ham"
  cp "$KOK/ornek-makaleler/ham/"*.pdf "$w/ham/"
  python3 "$KOK/olc/puanla.py" --ozet "$w/ham" > "$w/.ham-ozet"
  echo "$w"
}

naif() {
  local w; w="$(hazirla "naif-$1")"
  local istem="Bu klasördeki ham/ altında 24 PDF var. Hepsini oku. Araştırma sorusu: \"$SORU\" $OLCUT
İlgili olanları bul. Her PDF'in Yazar-Yıl-Başlık biçiminde yeniden adlandırılmış bir kopyasını duzenli/ altına koy (ham/'a dokunma).
Dahil olanlar için notlar/sentez.md dosyasına kaynak gösteren bir sentez notu yaz.
Kararlarını .masa/eleme.json dosyasına şu biçimde yaz: $BICIM"
  (cd "$w" && claude -p "$istem" --model opus --max-budget-usd "$BUTCE_NAIF" "${ORTAK[@]}" > "$w/claude.json" 2> "$w/hata.txt") || true
  python3 "$KOK/olc/puanla.py" naif "$w" "$w/claude.json" "$ANAHTAR" | tee -a "$SONUC"
}

akilli() {
  local w; w="$(hazirla "akilli-$1")"
  local istem="/arastirma-masasi:arastirma-masasi $w \"$SORU\" $OLCUT --onayli"
  (cd "$w" && claude -p "$istem" --model sonnet --plugin-dir "$PLUGIN" --max-budget-usd "$BUTCE_AKILLI" "${ORTAK[@]}" \
     > "$w/claude.json" 2> "$w/hata.txt") || true
  python3 "$KOK/olc/puanla.py" akilli "$w" "$w/claude.json" "$ANAHTAR" | tee -a "$SONUC"
}

jev() {
  if [ -z "${TYPESAFE_API_KEY:-}${JEV_ANAHTAR:-}" ]; then
    echo "UYARI: TYPESAFE_API_KEY yok, Jev SAHTE modda koşacak (kararlar gerçek değil)." >&2
  fi
  local w; w="$(hazirla "jev-$1")"
  local istem="/arastirma-masasi:arastirma-masasi $w \"$SORU\" $OLCUT --eleyici jev --onayli"
  (cd "$w" && claude -p "$istem" --model sonnet --plugin-dir "$PLUGIN" --max-budget-usd "$BUTCE_AKILLI" "${ORTAK[@]}" \
     > "$w/claude.json" 2> "$w/hata.txt") || true
  python3 "$KOK/olc/puanla.py" jev "$w" "$w/claude.json" "$ANAHTAR" | tee -a "$SONUC"
}

context_olc() {
  local w="$ISLER/context" && mkdir -p "$w"
  (cd "$w" && claude -p "/context" --model sonnet --setting-sources project > "$w/kapali.txt" 2>&1) || true
  (cd "$w" && claude -p "/context" --model sonnet --setting-sources project --plugin-dir "$PLUGIN" > "$w/acik.txt" 2>&1) || true
  echo "--- mod KAPALI"; cat "$w/kapali.txt"
  echo "--- mod AÇIK"; cat "$w/acik.txt"
}

main() {
  local komut="${1:-}" tekrar="${2:-2}"
  sessiz_path
  mkdir -p "$ISLER"
  case "$komut" in
    naif)    for i in $(seq 1 "$tekrar"); do naif "$i"; done ;;
    akilli)  for i in $(seq 1 "$tekrar"); do akilli "$i"; done ;;
    jev)     for i in $(seq 1 "$tekrar"); do jev "$i"; done ;;
    context) context_olc ;;
    *) sed -n '2,10p' "$0"; exit 2 ;;
  esac
}

main "$@"
