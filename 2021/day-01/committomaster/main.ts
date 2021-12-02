let sonarSweep = (values: Array<number>, window = 1) =>
  values
    .slice(window)
    .reduce((n, value, i) => value > values[i] ? n + 1 : n, 0)

import('./input.json', { assert: { type: 'json' } }).then(values => {
  console.log('Part One:', sonarSweep(values))
  console.log('Part Two:', sonarSweep(values, 3))
})
