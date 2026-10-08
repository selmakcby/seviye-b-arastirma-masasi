import { expect, test } from 'claude-code/testing'

import { bantMetni, jevAdimiMi, kisaAd, kisaModel } from '../hooks/register'

const BANT = { component: 'AbovePrompt', props: { hasSurvey: false, isWorking: true } } as const

const SPAWN = {
  tool_use_id: 'tu1',
  prompt: 'ilk sayfaları ele',
  description: 'PDF ele',
  subagentType: 'arastirma-masasi:eleyici',
  provider: { plugin: 'arastirma-masasi', tier: 'user' },
  parentModel: 'claude-sonnet-5-5',
  background: false,
  fork: false,
} as const

test('ad ve model kısalır', async () => {
  expect(kisaAd('arastirma-masasi:eleyici')).toBe('eleyici')
  expect(kisaAd('Explore')).toBe('Explore')
  expect(kisaModel('claude-haiku-4-5-20251001')).toBe('claude-haiku-4-5')
  expect(bantMetni([])).toBe('◇ araştırma masası · ana ajan')
  expect(jevAdimiMi('python3 "/x/scripts/jev_ele.py" /m --soru "s"')).toBe(true)
  expect(jevAdimiMi('python3 /x/scripts/masa.py cikar /m')).toBe(false)
})

test('jev_ele.py koşarken bant Jev eleyiciyi gösterir, bitince boşa döner', async ($, on) => {
  on('ui.render', async ($$, e) => $$.ui.resolve(e).Box({ children: [] }))
  const gorulen: string[] = []
  on('tool.call', async () => {
    const ekran = await $.ui.mount({ plugin: 'arastirma-masasi', surface: 'terminal', ...BANT })
    if (await ekran.find({ type: 'Text', text: /^◆ eleyici · jev$/ })) {
      gorulen.push('jev')
    }
    await ekran.unmount()
    return { result: { stdout: '', stderr: '', interrupted: false } }
  })

  await $.tool.call({ tool: 'Bash', command: 'python3 scripts/jev_ele.py /m --soru "s"' })
  expect(gorulen).toEqual(['jev'])
  const bitti = await $.ui.mount({ plugin: 'arastirma-masasi', surface: 'terminal', ...BANT })
  expect(await bitti.find({ type: 'Text', text: /ana ajan/ })).toBeDefined()
  await bitti.unmount()
})

test('ajan çalışırken bant adını ve modelini gösterir, bitince boşa döner', async ($, on) => {
  on('agent.spawn', async () => ({ model: 'claude-haiku-4-5-20251001', agentId: 'a1' }))
  on('ui.render', async ($$, e) => $$.ui.resolve(e).Box({ children: [] }))
  on('turn.complete', async () => ({ text: '' }))
  for (const surface of ['terminal', 'desktop'] as const) {
    const bos = await $.ui.mount({ plugin: 'arastirma-masasi', surface, ...BANT })
    expect(await bos.find({ type: 'Text', text: /araştırma masası/ })).toBeDefined()
    await bos.unmount()
  }

  await $.agent.spawn(SPAWN)
  const calisan = await $.ui.mount({ plugin: 'arastirma-masasi', surface: 'terminal', ...BANT })
  expect(await calisan.find({ type: 'Text', text: '◆ eleyici · claude-haiku-4-5' })).toBeDefined()
  await calisan.unmount()

  await $.turn.complete({ answer: '', durationMs: 10, isAborted: false, turnId: 't1', agentId: 'a1', reason: 'completed' })
  const bitti = await $.ui.mount({ plugin: 'arastirma-masasi', surface: 'terminal', ...BANT })
  expect(await bitti.find({ type: 'Text', text: /ana ajan/ })).toBeDefined()
  await bitti.unmount()
})
