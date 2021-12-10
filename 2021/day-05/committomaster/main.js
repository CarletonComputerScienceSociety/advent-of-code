let countOverlaps = (lines, diagonal = false) => {
  let result = 0
  let length = 1000
  let grid = Array.from({ length }, () => Array.from({ length }, () => 0))

  for (let [[x1, y1], [x2, y2]] of lines) {
    if (y1 == y2)
      for (let i = Math.min(x1, x2); i <= Math.max(x1, x2); ++i)
        grid[y1][i] += 1

    if (x1 == x2)
      for (let j = Math.min(y1, y2); j <= Math.max(y1, y2); ++j)
        grid[j][x1] += 1

    if (diagonal && Math.abs(x1 - x2) == Math.abs(y1 - y2))
      for (let i = Math.min(x1, x2); i <= Math.max(x1, x2); ++i)
        for (let j = Math.min(y1, y2); j <= Math.max(y1, y2); ++j)
          if (Math.abs(x1 - i) == Math.abs(y1 - j)) grid[j][i] += 1
  }

  for (let i = 0; i < length; ++i)
    for (let j = 0; j < length; ++j)
      if (grid[i][j] > 1) result += 1

  return result
}

fetch(new URL('./input', import.meta.url))
  .then(response => response.text())
  .then(input => {
    let lines = input
      .split('\n')
      .map(line => line.split(' -> ').map(pair => pair.split(',').map(Number)))

    console.log('Part One:', countOverlaps(lines))
    console.log('Part Two:', countOverlaps(lines, true))
  })
