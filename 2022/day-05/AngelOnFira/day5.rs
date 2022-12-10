use regex::Regex;

type InputType = Vec<(i32, i32, i32)>;

#[aoc_generator(day5)]
fn parse_input_day5(input: &str) -> InputType {
    // move 2 from 2 to 8
    // move 2 from 1 to 6
    // move 8 from 7 to 1
    // move 7 from 5 to 4
    // move 1 from 6 to 4
    input
        .lines()
        .map(|x| {
            let re = Regex::new(r"move (\d+) from (\d+) to (\d+)").unwrap();
            let nums = re
                .captures(x)
                .unwrap()
                .iter()
                .skip(1)
                .map(|x| x.unwrap().as_str().parse::<i32>().unwrap())
                .collect::<Vec<i32>>();

            (nums[0], nums[1] - 1, nums[2] - 1)
        })
        .collect()
}

//                         [R] [J] [W]
//             [R] [N]     [T] [T] [C]
// [R]         [P] [G]     [J] [P] [T]
// [Q]     [C] [M] [V]     [F] [F] [H]
// [G] [P] [M] [S] [Z]     [Z] [C] [Q]
// [P] [C] [P] [Q] [J] [J] [P] [H] [Z]
// [C] [T] [H] [T] [H] [P] [G] [L] [V]
// [F] [W] [B] [L] [P] [D] [L] [N] [G]
//  1   2   3   4   5   6   7   8   9

#[aoc(day5, part1)]
pub fn solve_part1(input: &InputType) -> String {
    // Set up the initial state
    let mut state = vec![
        // R Q G P C F
        vec!["R", "Q", "G", "P", "C", "F"],
        // P C T W
        vec!["P", "C", "T", "W"],
        // C M P H B
        vec!["C", "M", "P", "H", "B"],
        // R P M S Q T L
        vec!["R", "P", "M", "S", "Q", "T", "L"],
        // N G V Z J H P
        vec!["N", "G", "V", "Z", "J", "H", "P"],
        // J P D
        vec!["J", "P", "D"],
        // R T J F Z P G L
        vec!["R", "T", "J", "F", "Z", "P", "G", "L"],
        // J T P F C H L N
        vec!["J", "T", "P", "F", "C", "H", "L", "N"],
        // W C T H Q Z V G
        vec!["W", "C", "T", "H", "Q", "Z", "V", "G"],
    ];

    for (amount, from, to) in input {
        for _ in 0..*amount {
            let element = state[*from as usize].remove(0);
            state[*to as usize].insert(0, element);
        }
    }

    let mut output = String::new();
    for column in state.iter() {
        output.push_str(column[0]);
    }

    output
}

#[aoc(day5, part2)]
pub fn solve_part2(input: &InputType) -> String {
    // Set up the initial state
    let mut state = vec![
        // R Q G P C F
        vec!["R", "Q", "G", "P", "C", "F"],
        // P C T W
        vec!["P", "C", "T", "W"],
        // C M P H B
        vec!["C", "M", "P", "H", "B"],
        // R P M S Q T L
        vec!["R", "P", "M", "S", "Q", "T", "L"],
        // N G V Z J H P
        vec!["N", "G", "V", "Z", "J", "H", "P"],
        // J P D
        vec!["J", "P", "D"],
        // R T J F Z P G L
        vec!["R", "T", "J", "F", "Z", "P", "G", "L"],
        // J T P F C H L N
        vec!["J", "T", "P", "F", "C", "H", "L", "N"],
        // W C T H Q Z V G
        vec!["W", "C", "T", "H", "Q", "Z", "V", "G"],
    ];

    for (amount, from, to) in input {
        let mut queue = Vec::new();
        for _ in 0..*amount {
            let element = state[*from as usize].remove(0);

            queue.push(element);
        }

        for element in queue.iter().rev() {
            state[*to as usize].insert(0, element);
        }
    }

    let mut output = String::new();
    for column in state.iter() {
        output.push_str(column[0]);
    }

    output
}
