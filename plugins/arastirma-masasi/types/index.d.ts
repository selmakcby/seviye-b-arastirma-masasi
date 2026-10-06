/** Çalışan bir alt-ajan: bantta bir satır. */
export type AktifAjan = { id: string; ad: string; model: string }

declare module 'claude-code' {
  interface PluginState {
    'arastirma-masasi': { aktif: AktifAjan[] }
  }
}
