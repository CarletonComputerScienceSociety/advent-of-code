use std::{
    collections::{HashMap, HashSet},
    iter::FromIterator,
};

use itertools::Itertools;
use num_traits::Signed;
use regex::Regex;

type InputType = Vec<instruction>;

#[derive(Debug)]
pub enum instruction {
    addx(i32),
    noop,
}

#[aoc_generator(day10)]
fn parse_input_day8(input: &str) -> InputType {
    // Chars
    // input.chars().collect()

    // Map to ints
    input
        .lines()
        .map(|x| {
            if x.starts_with("noop") {
                instruction::noop
            } else {
                instruction::addx(
                    x.split(" ").collect::<Vec<&str>>()[1]
                        .parse::<i32>()
                        .unwrap(),
                )
            }
        })
        .collect()
}

#[aoc(day10, part1)]
pub fn solve_part1(input: &InputType) -> i32 {
    let mut memory = [1; 4];

    let mut cycle_count = 1;

    let mut sum_strength = 0;

    let strength_check = [20, 60, 100, 140, 180, 220];

    for instruction in input {
        match instruction {
            instruction::addx(x) => {
                cycle_count += 1;
                if strength_check.contains(&cycle_count) {
                    sum_strength += memory[0] * cycle_count;
                    println!("{}: {:?}", cycle_count, memory);
                }

                memory[0] += x;
                cycle_count += 1;
                if strength_check.contains(&cycle_count) {
                    sum_strength += memory[0] * cycle_count;
                    println!("{}: {:?}", cycle_count, memory);
                }
            }
            instruction::noop => {
                cycle_count += 1;
                if strength_check.contains(&cycle_count) {
                    sum_strength += memory[0] * cycle_count;
                    println!("{}: {:?}", cycle_count, memory);
                }
            }
        }
    }
    sum_strength
}

#[aoc(day10, part2)]
pub fn solve_part2(input: &InputType) -> i32 {
    let mut memory = [1; 4];

    let mut cycle_count = 1;

    for instruction in input {
        match instruction {
            instruction::addx(x) => {
                cycle_count += 1;
                if (cycle_count - 1) % 40 == memory[0] - 1
                    || (cycle_count - 1) % 40 == memory[0]
                    || (cycle_count - 1) % 40 == memory[0] + 1
                {
                    print!("#");
                } else {
                    print!(".")
                }
                if (cycle_count-1) % 40 == 0 {
                    println!("");
                }

                memory[0] += x;
                cycle_count += 1;
                if (cycle_count - 1) % 40 == memory[0] - 1
                    || (cycle_count - 1) % 40 == memory[0]
                    || (cycle_count - 1) % 40 == memory[0] + 1
                {
                    print!("#");
                } else {
                    print!(".")
                }
                if (cycle_count-1) % 40 == 0 {
                    println!("");
                }
            }
            instruction::noop => {
                cycle_count += 1;
                if (cycle_count - 1) % 40 == memory[0] - 1
                    || (cycle_count - 1) % 40 == memory[0]
                    || (cycle_count - 1) % 40 == memory[0] + 1
                {
                    print!("#");
                } else {
                    print!(".")
                }
                if (cycle_count-1) % 40 == 0 {
                    println!("");
                }
            }
        }
    }
    println!("");

    0
}
