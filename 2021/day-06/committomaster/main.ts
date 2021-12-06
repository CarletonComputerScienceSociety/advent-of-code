let reproduce = (fish: number[], days: number) => {
  fish = Array.from(fish)

  while (days > 0) {
    let newborns = fish[0]
    for (let t = 0; t < 8; t += 1) fish[t] = fish[t + 1]
    fish[6] += newborns
    fish[8] = newborns
    days -= 1
  }

  return fish.reduce((sum, n) => sum + n, 0)
}

fetch(new URL('./input', import.meta.url))
  .then(response => response.text())
  .then(input => {
    let fish = input
      .split(',')
      .map(Number)
      .reduce((fish, t) => (fish[t] += 1, fish), [0, 0, 0, 0, 0, 0, 0, 0, 0])

    console.log('Part One:', reproduce(fish, 80))
    console.log('Part Two:', reproduce(fish, 256))
  })
