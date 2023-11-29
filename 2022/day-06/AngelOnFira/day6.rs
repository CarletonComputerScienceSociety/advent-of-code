use std::{collections::HashSet, iter::FromIterator};

use regex::Regex;

type InputType = Vec<char>;

#[aoc_generator(day6)]
fn parse_input_day6(input: &str) -> InputType {
    input.chars().collect()
}

#[aoc(day6, part1)]
pub fn solve_part1(input: &InputType) -> i32 {
    input[1..]
        .windows(4)
        .position(|x| x.iter().collect::<HashSet<&char>>().len() == 4)
        .unwrap() as i32
        + 5
}

#[aoc(day6, part2)]
pub fn solve_part2(input: &InputType) -> i32 {
    input[1..]
        .windows(14)
        .position(|x| x.iter().collect::<HashSet<&char>>().len() == 14)
        .unwrap() as i32
        + 15
}
