import { CONFIG } from './config'

export const ORTHOGRAPHY = [
  'a',
  'b',
  'c',
  'd',
  'e',
  'g',
  'h',
  'i',
  'k',
  'l',
  'm',
  'n',
  'o',
  'p',
  'q',
  'r',
  's',
  't',
  'u',
  'v',
  'x',
  'y',
]

if (CONFIG.normalization) {
  ORTHOGRAPHY.forEach(
    (val, i) => (ORTHOGRAPHY[i] = val.normalize(CONFIG.normalization))
  )
}
