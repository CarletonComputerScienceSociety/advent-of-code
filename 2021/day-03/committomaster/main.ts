let powerConsumption = (bitstrings: string[]) => {
  let [gamma, epsilon] = ['', '']
  let ones = Array.from(bitstrings[0], () => 0)

  for (let bitstring of bitstrings)
    for (let [i, bit] of bitstring.split('').entries())
      ones[i] += Number(bit)

  for (let count of ones)
    [gamma, epsilon] =
      count > bitstrings.length - count
        ? [gamma + '1', epsilon + '0']
        : [gamma + '0', epsilon + '1']

  return parseInt(gamma, 2) * parseInt(epsilon, 2)
}

let lifeSupportRating = (bitstrings: string[]) => {
  let [oxygens, carbons] = [bitstrings, bitstrings]

  for (let i = 0; i < bitstrings[0].length; i += 1) {
    if (oxygens.length > 1) {
      let [zeros, ones] = [[], []]
      for (let bitstring of oxygens) {
        if (bitstring[i] == '0') zeros.push(bitstring)
        if (bitstring[i] == '1') ones.push(bitstring)
      }
      oxygens = zeros.length > ones.length ? zeros : ones
    }

    if (carbons.length > 1) {
      let [zeros, ones] = [[], []]
      for (let bitstring of carbons) {
        if (bitstring[i] == '0') zeros.push(bitstring)
        if (bitstring[i] == '1') ones.push(bitstring)
      }
      carbons = zeros.length <= ones.length ? zeros : ones
    }
  }

  return parseInt(oxygens[0], 2) * parseInt(carbons[0], 2)
}

import('./input.json', { assert: { type: 'json' } }).then(
  (bitstrings: string[]) => {
    console.log('Part One:', powerConsumption(bitstrings))
    console.log('Part Two:', lifeSupportRating(bitstrings))
  }
)
