let bingo = (boards, draws, last = false) => {
  let winner, result = 0

  game:
  for (let draw of draws)
    for (let board of boards)
      for (let row of board)
        for (let [i, cell] of row.entries()) {
          if (cell.value == draw) cell.marked = true
          if (
            row.every(cell => cell.marked) ||
            board.map(row => row[i]).every(cell => cell.marked)
          ) {
            winner = { draw, board }
            if (last) boards = boards.filter(b => b != board)
            else break game
          }
        }

  for (let row of winner.board)
    for (let cell of row)
      if (!cell.marked) result += cell.value

  return result * winner.draw
}

fetch(new URL('./input', import.meta.url))
  .then(response => response.text())
  .then(input => {
    let [header, ...remainder] = input.split('\n').filter(Boolean)
    let draws = header.split(',').map(Number)
    let boards = Array
      .from(
        { length: Math.ceil(remainder.length / 5) },
        (_, i) => remainder.slice(i * 5, (i + 1) * 5)
      )
      .map(board =>
        board.map(row =>
          row
            .split(/\s+/)
            .filter(Boolean)
            .map(value => ({ value: Number(value), marked: false }))
        )
      )

    console.log('Part One:', bingo(boards, draws))
    console.log('Part Two:', bingo(boards, draws, true))
  })
