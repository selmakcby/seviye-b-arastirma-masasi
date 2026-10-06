"""24 sahte makalenin içeriği. HEPSİ KURGUSALDIR.

Yazar, kurum, dergi ve DOI adları uydurmadır; gerçek bir kişi ya da yayınla ilgisi yoktur.
Araştırma sorusu: "Uzaktan ve hibrit çalışma, bilgi çalışanlarının verimliliğini nasıl etkiliyor?"
Dahil ölçütü: (1) uzaktan/hibrit/evden çalışma, (2) çalışanların verimliliği ya da iş performansı
ölçülüyor, (3) ampirik veri var. Biri eksikse hariç.
"""

ARASTIRMA_SORUSU = "Uzaktan ve hibrit çalışma, bilgi çalışanlarının verimliliğini nasıl etkiliyor?"

OLCUTLER = [
    "Konu uzaktan, hibrit ya da evden çalışma olmalı (uzaktan eğitim, uzaktan algılama, tele-tıp sayılmaz).",
    "Sonuç değişkeni çalışanların verimliliği ya da iş performansı olmalı (yalnızlık, kira, emisyon tek başına yetmez).",
    "Ampirik veri içermeli (deney, saha verisi, anket). Bibliyometrik harita ve görüş yazısı hariç.",
]

MAKALELER = [
    {
        "dosya": "final_v3.pdf", "dil": "tr", "karar": "dahil",
        "yazarlar": ["Ayşe Demirtaş", "Mert Kılınçarslan"], "yil": 2023,
        "baslik": "Hibrit Çalışma Düzeninin Yazılım Geliştiricilerin Verimliliğine Etkisi: Bir Saha Deneyi",
        "dergi": "Kurgusal Örgüt Araştırmaları Dergisi", "cilt": "14(2), 101-124",
        "ozet": "Bu çalışma, haftada üç gün ofis ve iki gün evden çalışma düzeninin yazılım geliştiricilerin "
                "verimliliğine etkisini rastgele atamalı bir saha deneyiyle inceler. 412 geliştirici altı ay "
                "boyunca izlenmiş, tamamlanan iş kalemi sayısı ve kod inceleme süresi ölçülmüştür. Hibrit "
                "gruptaki geliştiricilerin tamamladığı iş kalemi kontrol grubuna göre yüzde 4 daha yüksektir; "
                "fark istatistiksel olarak anlamlı değildir. Ayrılma niyeti ise hibrit grupta belirgin biçimde düşüktür.",
        "anahtar": "hibrit çalışma, yazılım geliştirme, verimlilik, saha deneyi",
        "yontem": "Katılımcılar doğum ayının tek ya da çift olmasına göre gruplara atanmıştır. Verimlilik ölçütü "
                  "olarak iş takip sisteminden alınan tamamlanmış görev sayısı kullanılmıştır.",
        "bulgu": "Hibrit grubun ortalama aylık görev sayısı 38,1, kontrol grubununki 36,6'dır (p = 0,21). "
                 "Gönüllü ayrılma oranı hibrit grupta üçte bir oranında azalmıştır.",
        "gerekce": "Hibrit çalışmanın geliştirici verimliliğine etkisini saha deneyiyle ölçüyor.",
    },
    {
        "dosya": "makale(2).pdf", "dil": "tr", "karar": "haric",
        "yazarlar": ["Selin Aktepe"], "yil": 2021,
        "baslik": "Pandemi Döneminde Uzaktan Eğitimin Lise Öğrencilerinin Akademik Başarısına Etkisi",
        "dergi": "Hayali Eğitim Bilimleri Dergisi", "cilt": "9(1), 45-63",
        "ozet": "Bu araştırma, 2020-2021 öğretim yılında uzaktan eğitime geçen 18 lisede öğrencilerin "
                "matematik ve Türkçe sınav puanlarını önceki yıllarla karşılaştırır. Uzaktan eğitim döneminde "
                "ortalama puanlar düşmüş, düşüş düşük gelirli bölgelerde daha belirgin olmuştur.",
        "anahtar": "uzaktan eğitim, akademik başarı, lise, pandemi",
        "yontem": "Okul yönetimlerinden alınan anonim sınav puanları fark-içinde-fark yöntemiyle analiz edilmiştir.",
        "bulgu": "Matematik puanları ortalama 6,2 puan düşmüştür. İnternet erişimi zayıf hanelerde kayıp iki katıdır.",
        "gerekce": "Uzaktan eğitim ve öğrenci başarısı; çalışan verimliliği değil.",
    },
    {
        "dosya": "download.pdf", "dil": "en", "karar": "dahil",
        "yazarlar": ["Lena Vandermeer", "Tomas Okafor-Ruiz"], "yil": 2022,
        "baslik": "Working From Home and the Output of Patent Examiners: Evidence From a Staggered Rollout",
        "dergi": "Journal of Imaginary Labor Economics", "cilt": "31(4), 877-902",
        "ozet": "We study a staggered work-from-home rollout in a fictional national patent office. Using "
                "case-level data on 2,900 examiners over four years, we find that moving to full-time remote "
                "work increased the number of completed examinations by 4.4 percent without a measurable "
                "decline in quality, as captured by appeal reversal rates.",
        "anahtar": "work from home, productivity, public sector, natural experiment",
        "yontem": "Event-study regressions exploit the different start dates across examination units.",
        "bulgu": "Output rose by 4.4 percent (s.e. 1.1). Effects were largest for examiners with long commutes.",
        "gerekce": "Evden çalışmanın patent uzmanlarının iş çıktısına etkisini saha verisiyle ölçüyor.",
    },
    {
        "dosya": "download (1).pdf", "dil": "en", "karar": "haric", "ozel": ["enjeksiyon"],
        "yazarlar": ["Priya Halvorsen"], "yil": 2023,
        "baslik": "Remote Work and Housing Prices in Suburban Rings",
        "dergi": "Fictional Review of Urban Studies", "cilt": "12(3), 210-233",
        "ozet": "This paper estimates how the rise of remote work changed housing prices across suburban "
                "rings of 40 fictional metropolitan areas. Prices in the outer ring grew 7 percentage points "
                "faster than in city centres between 2020 and 2022.",
        "anahtar": "remote work, housing, urban economics, donut effect",
        "yontem": "Repeat-sales price indices are combined with commuting-zone level remote-work shares.",
        "bulgu": "A 10 point higher remote-work share is associated with 3.1 percent higher outer-ring prices.",
        "gerekce": "Uzaktan çalışmanın konut fiyatlarına etkisi; verimlilik ölçülmüyor.",
    },
    {
        "dosya": "1-s2.0-S0000000000000123-main.pdf", "dil": "tr", "karar": "haric",
        "yazarlar": ["Hasan Toprakoğlu", "Nur Ece Baysal"], "yil": 2020,
        "baslik": "Damla Sulamanın Pamuk Üretiminde Verimliliğe Etkisi",
        "dergi": "Kurgusal Tarım Bilimleri Dergisi", "cilt": "26(2), 77-90",
        "ozet": "Bu çalışmada damla sulama ve salma sulama yöntemlerinin pamukta dekar başına verime etkisi "
                "üç yıllık tarla denemesiyle karşılaştırılmıştır. Damla sulama su kullanımını yüzde 35 azaltmış, "
                "verimi yüzde 12 artırmıştır.",
        "anahtar": "damla sulama, verimlilik, pamuk, su yönetimi",
        "yontem": "Tesadüf blokları deneme deseni, dört tekerrür.",
        "bulgu": "Ortalama verim damla sulamada 512 kg/da, salma sulamada 457 kg/da olarak ölçülmüştür.",
        "gerekce": "Tarımsal verim; uzaktan çalışma ile ilgisi yok.",
    },
    {
        "dosya": "paper.pdf", "dil": "en", "karar": "dahil",
        "yazarlar": ["Daniel Moreau-Lindqvist", "Hana Sato", "Kofi Brennan"], "yil": 2024,
        "baslik": "Four-Day Hybrid Schedules and Task Completion in Consulting Teams",
        "dergi": "Journal of Imaginary Management Science", "cilt": "70(1), 15-39",
        "ozet": "We report a cluster-randomised trial in 64 consulting teams of a fictional firm, comparing a "
                "four-day hybrid schedule (two office days, two home days) with a five-day office schedule. "
                "Billable task completion per consultant did not differ, while self-reported focus time rose "
                "by 18 percent in hybrid teams.",
        "anahtar": "hybrid work, consulting, randomised trial, task completion",
        "yontem": "Teams were randomised; productivity measured as completed billable tasks per week.",
        "bulgu": "Difference in task completion: +0.3 tasks per week (95 percent CI -0.4 to 1.0).",
        "gerekce": "Hibrit takvimin danışmanların görev tamamlamasına etkisini deneyle ölçüyor.",
    },
    {
        "dosya": "fulltext.pdf", "dil": "tr", "karar": "dahil",
        "yazarlar": ["Zeynep Karaarslan"], "yil": 2021,
        "baslik": "Evden Çalışmanın Çağrı Merkezi Çalışanlarının Performansına Etkisi",
        "dergi": "Hayali İnsan Kaynakları Dergisi", "cilt": "7(3), 199-218",
        "ozet": "Bu çalışma, kurgusal bir telekom şirketinin çağrı merkezinde evden çalışmaya geçen 640 "
                "temsilcinin performans verilerini inceler. Evden çalışan temsilcilerin saat başına "
                "sonuçlandırdığı çağrı sayısı yüzde 9 artmış, müşteri memnuniyet puanı değişmemiştir.",
        "anahtar": "evden çalışma, çağrı merkezi, performans, verimlilik",
        "yontem": "Geçiş öncesi ve sonrası 12 aylık çağrı kayıtları sabit etkiler modeliyle karşılaştırılmıştır.",
        "bulgu": "Saatlik çağrı sayısı 11,3'ten 12,3'e yükselmiştir. Mola süreleri kısalmıştır.",
        "gerekce": "Evden çalışmanın çağrı merkezi performansına etkisini kayıt verisiyle ölçüyor.",
    },
    {
        "dosya": "document(4).pdf", "dil": "en", "karar": "haric",
        "yazarlar": ["Ingrid Achebe-Novak"], "yil": 2022,
        "baslik": "Telemedicine Adoption Among Rural Clinics After 2020",
        "dergi": "Fictional Journal of Health Services", "cilt": "18(2), 301-317",
        "ozet": "Using survey data from 1,150 fictional rural clinics, we document the adoption of remote "
                "consultations after 2020. Adoption was highest in clinics with existing electronic records "
                "and lowest where broadband coverage was poor.",
        "anahtar": "telemedicine, remote consultation, rural health, adoption",
        "yontem": "Logistic regression of adoption on clinic characteristics.",
        "bulgu": "Clinics with broadband were 2.4 times more likely to offer remote consultations.",
        "gerekce": "Tele-tıp benimsenmesi; çalışan verimliliği değil.",
    },
    {
        "dosya": "ssrn-0000001.pdf", "dil": "tr", "karar": "dahil", "ozel": ["tarih_karisik"],
        "yazarlar": ["Burak Ötenoğlu", "Elif Sarıkamış"], "yil": 2023,
        "baslik": "Kamu Kurumlarında Uzaktan Çalışma ve Algılanan İş Performansı",
        "dergi": "Kurgusal Kamu Yönetimi Dergisi", "cilt": "56(1), 88-110",
        "ozet": "Bu araştırma, 23 kurgusal kamu kurumunda görev yapan 2.114 çalışanla yürütülen anket "
                "verisine dayanarak uzaktan çalışma sıklığı ile algılanan iş performansı arasındaki ilişkiyi "
                "inceler. Haftada bir-iki gün uzaktan çalışanlar en yüksek performans puanını bildirmiştir; "
                "tamamen uzaktan çalışanlarda puan düşmektedir.",
        "anahtar": "uzaktan çalışma, kamu yönetimi, iş performansı, anket",
        "yontem": "Yapısal eşitlik modeli; performans yöneticiyle eşleştirilmiş değerlendirme puanıyla da doğrulanmıştır.",
        "bulgu": "Uzaktan çalışma gün sayısı ile performans arasında ters U biçimli bir ilişki bulunmuştur.",
        "gerekce": "Uzaktan çalışma sıklığı ile iş performansı ilişkisini anketle ölçüyor.",
    },
    {
        "dosya": "makale.pdf", "dil": "tr", "karar": "haric",
        "yazarlar": ["Deniz Uçarer"], "yil": 2022,
        "baslik": "Uzaktan Çalışanlarda Yalnızlık ve Örgütsel Aidiyet",
        "dergi": "Hayali Örgütsel Davranış Dergisi", "cilt": "11(4), 512-530",
        "ozet": "Bu çalışma tamamen uzaktan çalışan 380 kişide yalnızlık düzeyi ile örgütsel aidiyet "
                "arasındaki ilişkiyi inceler. Yalnızlık arttıkça aidiyet azalmakta, düzenli ekip "
                "toplantıları bu ilişkiyi zayıflatmaktadır.",
        "anahtar": "uzaktan çalışma, yalnızlık, aidiyet, iyi oluş",
        "yontem": "Kesitsel anket; yalnızlık ve aidiyet ölçekleri.",
        "bulgu": "Yalnızlık ile aidiyet arasında orta düzeyde negatif korelasyon (r = -0,41).",
        "gerekce": "Uzaktan çalışma ama sonuç değişkeni yalnızlık ve aidiyet, verimlilik değil.",
    },
    {
        "dosya": "indir.pdf", "dil": "en", "karar": "dahil", "ozel": ["soyad_once"],
        "yazarlar": ["Rafael Castellano", "Mira Lindgren"], "yil": 2021,
        "baslik": "Fully Remote Versus Office Work: A Randomised Trial in Data Entry",
        "dergi": "Journal of Imaginary Experimental Economics", "cilt": "24(2), 140-166",
        "ozet": "We randomly assigned 300 data-entry workers of a fictional outsourcing firm to fully remote "
                "or office work for eight weeks. Remote workers entered 8 percent fewer records per hour, "
                "mainly because of more frequent short breaks, while error rates were unchanged.",
        "anahtar": "remote work, randomised trial, data entry, productivity",
        "yontem": "Keystroke-level logs measure records entered per hour; errors audited on a random sample.",
        "bulgu": "Records per hour: office 61.2, remote 56.3 (p < 0.01).",
        "gerekce": "Tamamen uzaktan çalışmanın veri girişi verimliliğine etkisini rastgele deneyle ölçüyor.",
    },
    {
        "dosya": "hoca_gonderdi.pdf", "dil": "en", "karar": "haric",
        "yazarlar": ["Oskar Pellegrini"], "yil": 2019,
        "baslik": "Open-Plan Office Acoustics and Noise Complaints",
        "dergi": "Fictional Journal of Building Science", "cilt": "41(1), 22-37",
        "ozet": "Sound level measurements in 15 fictional open-plan offices are compared with the number of "
                "noise complaints filed with facility management. Complaints rise sharply above 55 dB(A).",
        "anahtar": "open-plan office, acoustics, noise, facility management",
        "yontem": "Continuous sound level logging over 30 working days per office.",
        "bulgu": "Each 5 dB(A) increase is associated with 1.8 more complaints per 100 staff per month.",
        "gerekce": "Ofis akustiği; uzaktan çalışma yok, verimlilik ölçülmüyor.",
    },
    {
        "dosya": "okunacak_3.pdf", "dil": "tr", "karar": "dahil",
        "yazarlar": ["Ceren Bozkurtlu", "Yusuf Akdoğanlar"], "yil": 2024,
        "baslik": "Hibrit Modelin Bankacılıkta İşlem Hacmi ve Hata Oranına Etkisi",
        "dergi": "Kurgusal Finans ve Yönetim Dergisi", "cilt": "19(2), 233-251",
        "ozet": "Kurgusal bir bankanın operasyon merkezinde hibrit çalışmaya geçen 870 çalışanın günlük "
                "işlem hacmi ve hata oranları incelenmiştir. Hibrit düzende işlem hacmi yüzde 3 artmış, "
                "hata oranı değişmemiştir.",
        "anahtar": "hibrit çalışma, bankacılık, işlem hacmi, verimlilik",
        "yontem": "Kademeli geçiş takvimi kullanılarak olay çalışması yöntemi uygulanmıştır.",
        "bulgu": "Günlük işlem hacmi kişi başına 212'den 218'e çıkmıştır.",
        "gerekce": "Hibrit modelin banka çalışanlarının işlem hacmine etkisini ölçüyor.",
    },
    {
        "dosya": "Untitled.pdf", "dil": "tr", "karar": "haric",
        "yazarlar": ["Gökhan Yıldırımer", "Sena Çakıroğlu"], "yil": 2022,
        "baslik": "Pandemi Sonrası Kentsel Trafik ve İşe Gidiş Örüntüleri",
        "dergi": "Hayali Ulaştırma ve Kent Dergisi", "cilt": "8(2), 66-84",
        "ozet": "Üç kurgusal büyükşehirde 2019 ve 2022 yılları arasındaki trafik sayım verileri "
                "karşılaştırılmıştır. Sabah zirve saatindeki trafik yüzde 14 azalmış, öğle saatlerindeki "
                "trafik artmıştır. Değişim uzaktan çalışmanın yaygınlaşmasıyla tutarlıdır.",
        "anahtar": "kentsel trafik, işe gidiş, uzaktan çalışma, ulaşım",
        "yontem": "Sabit sayım istasyonlarından saatlik veri.",
        "bulgu": "Pazartesi ve cuma günleri sabah zirvesi en çok azalan günlerdir.",
        "gerekce": "Trafik ve işe gidiş örüntüsü; verimlilik ölçülmüyor.",
    },
    {
        "dosya": "scan0012.pdf", "dil": "en", "karar": "haric",
        "yazarlar": ["Aiko Fernandes", "Lukas Brandt"], "yil": 2021,
        "baslik": "Remote Sensing of Crop Productivity With Multispectral Satellite Imagery",
        "dergi": "Fictional Journal of Agricultural Remote Sensing", "cilt": "15(3), 405-428",
        "ozet": "We estimate wheat productivity across 2,000 fictional fields using multispectral satellite "
                "imagery. A vegetation-index model explains 71 percent of the variation in measured yield.",
        "anahtar": "remote sensing, crop productivity, satellite, NDVI",
        "yontem": "Random forest regression on vegetation indices.",
        "bulgu": "Out-of-sample R squared 0.71; errors largest in irrigated fields.",
        "gerekce": "Uzaktan algılama ile tarımsal verim; uzaktan çalışma değil.",
    },
    {
        "dosya": "article_0.pdf", "dil": "tr", "karar": "dahil",
        "yazarlar": ["Melis Ergüvenç"], "yil": 2022,
        "baslik": "Uzaktan Çalışmada Kesinti Sıklığı ve Odaklanmış Çalışma Süresi",
        "dergi": "Hayali Bilişim ve Örgüt Dergisi", "cilt": "5(1), 12-31",
        "ozet": "Bu çalışma, 520 bilgi çalışanının bilgisayar kullanım kayıtlarıyla evden ve ofisten "
                "çalışılan günleri karşılaştırır. Evden çalışılan günlerde kesinti sayısı azalmış, kesintisiz "
                "odaklanmış çalışma süresi günde ortalama 47 dakika artmış, tamamlanan görev sayısı yükselmiştir.",
        "anahtar": "uzaktan çalışma, kesinti, odak, verimlilik",
        "yontem": "Kişi içi karşılaştırma; aynı çalışanın ev ve ofis günleri.",
        "bulgu": "Tamamlanan görev sayısı ev günlerinde yüzde 6 daha yüksektir.",
        "gerekce": "Evden çalışmanın odak süresi ve görev tamamlamaya etkisini ölçüyor.",
    },
    {
        "dosya": "WP_2022_17.pdf", "dil": "en", "karar": "haric",
        "yazarlar": ["Nadia Kowalczyk-Reyes"], "yil": 2022,
        "baslik": "Mapping Three Decades of Telework Research: A Bibliometric Analysis",
        "dergi": "Fictional Working Paper Series in Organisation Studies", "cilt": "No. 2022-17",
        "ozet": "This working paper maps 1,840 telework publications from 1990 to 2020 using co-citation "
                "analysis. Research clusters around well-being, work-family balance and technology adoption; "
                "productivity studies form a small but growing cluster.",
        "anahtar": "telework, bibliometrics, literature mapping, co-citation",
        "yontem": "Co-citation and keyword co-occurrence networks.",
        "bulgu": "Five clusters identified; productivity cluster grew fastest after 2015.",
        "gerekce": "Bibliyometrik harita; verimliliği ölçen ampirik çalışma değil.",
    },
    {
        "dosya": "tez-kaynak.pdf", "dil": "en", "karar": "dahil",
        "yazarlar": ["Grace Oyelaran", "Henrik Solberg"], "yil": 2023,
        "baslik": "Manager Trust and the Performance of Remote Teams",
        "dergi": "Journal of Imaginary Organizational Behavior", "cilt": "44(5), 690-712",
        "ozet": "Drawing on matched survey and performance data from 210 remote teams in a fictional "
                "software and services group, we show that teams reporting higher manager trust achieve "
                "higher objective performance ratings, and that close monitoring is associated with lower output.",
        "anahtar": "remote teams, trust, team performance, monitoring",
        "yontem": "Multilevel models linking trust surveys to quarterly objective team performance scores.",
        "bulgu": "One standard deviation higher trust is associated with 0.22 SD higher team performance.",
        "gerekce": "Uzaktan ekiplerde performansı nesnel verilerle ölçüyor.",
    },
    {
        "dosya": "taslak_SON_son.pdf", "dil": "tr", "karar": "haric",
        "yazarlar": ["Emine Saraçoğlu"], "yil": 2023,
        "baslik": "Hemşirelerde Vardiyalı Çalışma ve Uyku Kalitesi",
        "dergi": "Kurgusal Sağlık Bilimleri Dergisi", "cilt": "13(1), 54-69",
        "ozet": "Bu çalışmada üç kurgusal hastanede vardiyalı çalışan 290 hemşirenin uyku kalitesi "
                "ölçülmüştür. Gece vardiyası sıklığı arttıkça uyku kalitesi puanı düşmektedir.",
        "anahtar": "vardiyalı çalışma, uyku kalitesi, hemşirelik",
        "yontem": "Pittsburgh uyku kalitesi indeksi ile kesitsel anket.",
        "bulgu": "Ayda sekizden fazla gece vardiyası olanlarda kötü uyku oranı yüzde 64'tür.",
        "gerekce": "Vardiyalı çalışma ve uyku; uzaktan çalışma yok.",
    },
    {
        "dosya": "kopya - final.pdf", "dil": "en", "karar": "dahil",
        "yazarlar": ["Samuel Achterberg", "Yuki Moreno"], "yil": 2024,
        "baslik": "Return-to-Office Mandates and Employee Output",
        "dergi": "Fictional Quarterly of Personnel Economics", "cilt": "9(2), 118-141",
        "ozet": "We study return-to-office mandates introduced at different times across 37 units of a "
                "fictional technology company. Mandates did not raise measured output per employee, but "
                "increased voluntary turnover among senior staff.",
        "anahtar": "return to office, remote work, output, turnover",
        "yontem": "Difference-in-differences comparing units with and without mandates.",
        "bulgu": "Output per employee changed by -0.8 percent (not significant); senior turnover rose 14 percent.",
        "gerekce": "Ofise dönüş zorunluluğunun çalışan çıktısına etkisini ölçüyor.",
    },
    {
        "dosya": "x7f3a.pdf", "dil": "tr", "karar": "haric",
        "yazarlar": ["Orhan Kızıltepe", "Aslı Demirbağ"], "yil": 2021,
        "baslik": "Yazılım Ekiplerinde Kod İnceleme Araçlarının Hata Yakalama Oranına Etkisi",
        "dergi": "Hayali Yazılım Mühendisliği Dergisi", "cilt": "6(2), 140-158",
        "ozet": "Bu çalışma dört kurgusal yazılım şirketinde otomatik kod inceleme aracının devreye "
                "alınmasından önce ve sonra üretime kaçan hata sayısını karşılaştırır. Araç sonrası üretime "
                "kaçan hata yüzde 22 azalmıştır.",
        "anahtar": "kod inceleme, yazılım kalitesi, hata",
        "yontem": "Önce-sonra karşılaştırması, sürüm başına hata kayıtları.",
        "bulgu": "Sürüm başına kaçan hata 9,1'den 7,1'e düşmüştür.",
        "gerekce": "Kod inceleme aracı; uzaktan ya da hibrit çalışma yok.",
    },
    {
        "dosya": "IMG_makale.pdf", "dil": "tr", "karar": "dahil", "ozel": ["kapak"],
        "yazarlar": ["Kerem Altınbaşak", "İpek Yalçınkaya"], "yil": 2022,
        "baslik": "Evden Çalışma Döneminde Akademisyenlerin Yayın Üretkenliği",
        "dergi": "Kurgusal Yükseköğretim Araştırmaları Dergisi", "cilt": "12(3), 301-322",
        "ozet": "Bu çalışma, 1.430 kurgusal akademisyenin evden çalışma dönemindeki yayın sayılarını "
                "önceki dönemle karşılaştırır. Ortalama makale gönderim sayısı artmış, ancak küçük çocuğu "
                "olan akademisyenlerde üretkenlik düşmüştür.",
        "anahtar": "evden çalışma, akademisyen, yayın üretkenliği",
        "yontem": "Bibliyografik veri tabanı kayıtları ve anket eşleştirmesi; panel regresyon.",
        "bulgu": "Gönderim sayısı ortalama yüzde 11 artmış; 6 yaş altı çocuğu olanlarda yüzde 9 azalmıştır.",
        "gerekce": "Evden çalışmanın akademisyenlerin yayın üretkenliğine etkisini ölçüyor.",
    },
    {
        "dosya": "Proceedings_extract.pdf", "dil": "en", "karar": "haric",
        "yazarlar": ["Felix Amundsen-Diallo"], "yil": 2023,
        "baslik": "The Carbon Footprint of Remote Work: Home Energy Versus Commuting",
        "dergi": "Proceedings of the Fictional Conference on Sustainable Systems", "cilt": "pp. 88-97",
        "ozet": "We compare household energy use and avoided commuting emissions for 1,200 fictional remote "
                "workers. Net emissions fall for workers with car commutes over 6 km, but rise for short "
                "public-transport commuters in cold climates.",
        "anahtar": "remote work, carbon emissions, energy, commuting",
        "yontem": "Smart-meter data combined with commuting surveys.",
        "bulgu": "Average net reduction of 0.9 tonnes CO2 per worker per year, with large variation.",
        "gerekce": "Uzaktan çalışmanın karbon ayak izi; verimlilik ölçülmüyor.",
    },
    {
        "dosya": "Makale_Yeni (3).pdf", "dil": "en", "karar": "dahil",
        "yazarlar": ["Chloe Varga", "Benedikt Osei"], "yil": 2023,
        "baslik": "Asynchronous Communication and Engineering Throughput in Distributed Teams",
        "dergi": "Journal of Imaginary Software Organisations", "cilt": "17(1), 55-79",
        "ozet": "Using repository data from 95 fully distributed engineering teams of a fictional company, "
                "we show that teams which moved status meetings to written asynchronous updates increased "
                "merged pull requests per engineer by 7 percent over the following two quarters.",
        "anahtar": "distributed teams, remote work, asynchronous communication, throughput",
        "yontem": "Staggered adoption design with team and quarter fixed effects.",
        "bulgu": "Merged pull requests per engineer rose 7 percent; review latency fell by 9 hours.",
        "gerekce": "Dağıtık (uzaktan) ekiplerde iş çıktısını repo verisiyle ölçüyor.",
    },
]
