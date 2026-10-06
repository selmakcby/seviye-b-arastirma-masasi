// Araştırma masası modu: çalışan alt-ajanı istemin üstündeki bantta gösterir.
//   ◆ eleyici · claude-haiku-4-5      (bir ajan çalışırken)
//   ◇ araştırma masası · ana ajan     (boştayken: mod açık demektir)
// Ses yok, model yönlendirme yok: modeli ajan dosyasındaki `model:` satırı seçer.
import { atom, read, update } from 'claude-code'
import type { Register } from 'claude-code'

import type { AktifAjan } from '../types'

const RENK = '#d97757'
const aktif = atom({ plugin: 'arastirma-masasi', key: 'aktif' } as const, [] as AktifAjan[])

// "arastirma-masasi:eleyici" -> "eleyici"
export const kisaAd = (tur: string): string => tur.split(':').pop() || tur

// "claude-haiku-4-5-20251001" -> "claude-haiku-4-5"
export const kisaModel = (model: string): string => model.replace(/-\d{8}$/, '')

export const bantMetni = (liste: readonly AktifAjan[]): string =>
  liste.length
    ? liste.map(a => `◆ ${a.ad} · ${a.model}`).join('   ')
    : '◇ araştırma masası · ana ajan'

export const register: Register = on => {
  on('agent.spawn', async ($, e, next) => {
    const sonuc = await next(e)
    if (sonuc.deny !== undefined || !sonuc.agentId) {
      return sonuc
    }
    const yeni: AktifAjan = { id: sonuc.agentId, ad: kisaAd(e.subagentType), model: kisaModel(sonuc.model) }
    await update($, aktif, liste => [...liste.filter(a => a.id !== yeni.id), yeni])
    return sonuc
  })

  on('turn.complete', async ($, e, next) => {
    const bitenId = e.agentId
    if (bitenId) {
      await update($, aktif, liste => liste.filter(a => a.id !== bitenId))
    }
    return next(e)
  })

  on('session.end', async ($, e, next) => {
    await update($, aktif, () => [])
    return next(e)
  })

  on('ui.render', { component: 'AbovePrompt' }, async ($, e, next) => {
    if (e.props.hasSurvey) {
      return next(e)
    }
    const { Box, Text } = $.ui.resolve(e)
    const digerleri = await next(e)
    const liste = await read($, aktif)
    const bant = Text({ key: 'masa-bandi', color: RENK, dimColor: liste.length === 0, children: [bantMetni(liste)] })
    return Box({ flexDirection: 'column', children: [...(digerleri ? [digerleri] : []), bant] })
  })
}
