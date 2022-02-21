import { CONFIG } from './config'

export const ORTHOGRAPHY = [
  'q',
  'e',
  'r',
  't',
  'y',
  'u',
  'i',
  'o',
  'p',
  'a',
  's',
  'd',
  'h',
  'g',
  'k',
  'l',
  'x',
  'c',
  'v',
  'b',
  'n',
  'm',
]

export const ORTHOGRAPHY_ROWS = [
  ['q', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
  ['a', 's', 'd', 'h', 'g', 'k', 'l'],
  ['x', 'c', 'v', 'b', 'n', 'm'],
]

if (CONFIG.normalization) {
  ORTHOGRAPHY.forEach(
    (val, i) => (ORTHOGRAPHY[i] = val.normalize(CONFIG.normalization))
  )
}
