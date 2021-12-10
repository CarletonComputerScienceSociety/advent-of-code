use std::thread::current;

pub struct Instruction {}

#[aoc_generator(day10)]
pub fn input_generator(input: &str) -> Vec<Vec<char>> {
    // [({(<(())[]>[[{[]{<()<>>
    // [(()[<>])]({[<{<<[]>>(
    // {([(<{}[<>[]}>{[]{[(<()>
    // (((({<>}<{<{<>}{[]{[]{}
    // [[<[([]))<([[{}[[()]]]
    // [{[{({}]{}}([{[{{{}}([]
    // {<[[]]>}<{[{[{[]{()[[[]
    // [<(<(<(<{}))><([]([]()
    // <{([([[(<>()){}]>(<<{{
    // <{([{{}}[<[[[<>{}]]]>[]]

    input.lines().map(|line| line.chars().collect()).collect()
}

#[aoc(day10, part1)]
pub fn solve_part1(input: &[Vec<char>]) -> i32 {
    // parse invalid closing brackets

    // ): 3 points.
    // ]: 57 points.
    // }: 1197 points.
    // >: 25137 points.

    // Stop at the first incorrect closing character on each corrupted line.

    let mut score = 0;

    input
        .iter()
        .map(|line| match parse_chunk(line, 0) {
            Ok(_) => 0,
            Err(None) => 0,
            Err(Some(amount)) => amount,
        })
        .sum()
}

fn parse_chunk(input: &Vec<char>, pos: usize) -> Result<usize, Option<i32>> {
    let first_char = input[pos];

    let closing_test = match first_char {
        ')' => Err(Some(3)),
        ']' => Err(Some(57)),
        '}' => Err(Some(1197)),
        '>' => Err(Some(25137)),
        _ => Ok(0),
    }?;

    // While we don't have our closing character, keep parsing
    let this_closing_char = match first_char {
        '(' => ')',
        '[' => ']',
        '{' => '}',
        '<' => '>',
        _ => unimplemented!(),
    };

    // If the next character isn't our closing character, recurse
    let mut next_pos = pos + 1;
    if next_pos == input.len() {
        return Err(None);
    }
    while input[next_pos] != this_closing_char {
        next_pos = parse_chunk(input, next_pos)?;
        if next_pos == input.len() {
            return Err(None);
        }
    }

    // If we have our closing character, return the next position
    Ok(next_pos + 1)
}

#[aoc(day10, part2)]
pub fn solve_part2(input: &[Vec<char>]) -> i128 {
    let new_lines = input
        .iter()
        .filter(|line| match parse_chunk(line, 0) {
            Err(Some(_)) => false,
            _ => true,
        })
        .map(|x| x.clone())
        .collect::<Vec<Vec<char>>>();

    // dbg!(new_lines.clone());

    let mut scores = new_lines
        .iter()
        .map(|line| {
            let mut pos = 0;
            loop {
                let ret_val = match complete_chunk(line, pos, &mut Vec::new()) {
                    Ok(x) => {
                        pos = x;
                        None
                    }
                    Err(x) => {
                        println!("{}", x.clone().iter().rev().collect::<String>());
                        Some(x.iter().rev().fold(0, |acc, x| {
                            acc * 5
                                + match x {
                                    ')' => 1,
                                    ']' => 2,
                                    '}' => 3,
                                    '>' => 4,
                                    _ => unreachable!(),
                                }
                        }))
                    }
                };

                if ret_val.is_some() {
                    return ret_val.unwrap();
                }
            }
        })
        .collect::<Vec<i128>>();

    scores.sort();

    dbg!(scores.clone());

    // Get the middle score
    let middle_index = (scores.len() - 1) / 2;
    scores[middle_index]
}

fn complete_chunk(
    input: &Vec<char>,
    pos: usize,
    curr_incomplete: &mut Vec<char>,
) -> Result<usize, Vec<char>> {
    let first_char = input[pos];

    // dbg!(input.clone());
    // dbg!(first_char);
    // dbg!(curr_incomplete.clone());

    // While we don't have our closing character, keep parsing
    let this_closing_char = match first_char {
        '(' => ')',
        '[' => ']',
        '{' => '}',
        '<' => '>',
        _ => unimplemented!(),
    };

    curr_incomplete.push(this_closing_char);

    // If the next character isn't our closing character, recurse
    let mut next_pos = pos + 1;
    if next_pos >= input.len() {
        return Err(curr_incomplete.to_vec());
    }
    while input[next_pos] != this_closing_char {
        next_pos = complete_chunk(input, next_pos, curr_incomplete)?;
        if next_pos >= input.len() {
            return Err(curr_incomplete.to_vec());
        }
    }

    curr_incomplete.pop();

    if next_pos == input.len() {
        return Err(curr_incomplete.to_vec());
    }

    // dbg!(next_pos + 1);

    // If we have our closing character, return the next position
    Ok(next_pos + 1)
}
