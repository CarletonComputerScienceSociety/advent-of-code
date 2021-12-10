type State = [x: number, y: number, aim: number]
type Mode = '1' | '2'
type Direction = 'forward' | 'down' | 'up'
type Command = [mode: Mode, direction: Direction, delta: number]
type Move = (state: State, command: Command) => State
type Dive = (commands: Command[], state?: State) => number

let move: Move = ([x, y, aim], [mode, direction, delta]) => {
  switch (mode) {
    case '1': switch (direction) {
      case 'forward': return [x + delta, y, aim]
      case 'down': return [x, y + delta, aim]
      case 'up': return [x, y - delta, aim]
    }
    case '2': switch (direction) {
      case 'forward': return [x + delta, y + aim * delta, aim]
      case 'down': return [x, y, aim + delta]
      case 'up': return [x, y, aim - delta]
    }
  }
}

let dive: Dive = (commands, state = [0, 0, 0]) => {
  let [x, y] = commands.reduce(move, state)
  return x * y
}

import('./input.json', { assert: { type: 'json' } }).then(
  (rows: [Direction, number][]) => {
    console.log('Part One:', dive(rows.map(row => ['1', ...row])))
    console.log('Part Two:', dive(rows.map(row => ['2', ...row])))
  }
)
