use std::{
    collections::{HashMap, HashSet},
    iter::FromIterator,
};

use itertools::Itertools;
use regex::Regex;

type InputType = HashMap<(i32, i32), i32>;

#[aoc_generator(day8)]
fn parse_input_day8(input: &str) -> InputType {
    // Chars
    // input.chars().collect()

    // Map to ints
    // input.lines().map(|x| x.parse::<i32>().unwrap()).collect()

    // Regex
    input
        .lines()
        .enumerate()
        .map(|(x, tree_height)| {
            tree_height
                .chars()
                .enumerate()
                .fold(HashMap::new(), |mut acc, (y, tree)| {
                    acc.insert((x as i32, y as i32), tree.to_digit(10).unwrap() as i32);
                    acc
                })
        })
        .fold(HashMap::new(), |mut acc, x| {
            acc.extend(x);
            acc
        })
}

#[aoc(day8, part1)]
pub fn solve_part1(input: &InputType) -> i32 {
    // Find the max of the x and y of the hashmap
    let max_x = input.iter().map(|x| x.0 .1).max().unwrap();

    let max_y = input.iter().map(|x| x.0 .0).max().unwrap();

    // Go over every number in the hashmap, see if everything to either the
    // left, right, up or down is smaller than it. If so, return true.
    input
        .iter()
        .filter(|(pos, tree)| {
            // Check left
            let mut left = true;
            for x in 1..=pos.1 {
                if input.get(&(pos.0, pos.1 - x)).unwrap() >= tree {
                    left = false;
                    break;
                }
            }

            // Check right
            let mut right = true;
            for x in 1..=max_y - pos.1 {
                if input.get(&(pos.0, pos.1 + x)).unwrap() >= tree {
                    right = false;
                    break;
                }
            }

            // Check up
            let mut up = true;
            for x in 1..=pos.0 {
                if input.get(&(pos.0 - x, pos.1)).unwrap() >= tree {
                    up = false;
                    break;
                }
            }

            // Check down
            let mut down = true;
            for x in 1..=max_x - pos.0 {
                if input.get(&(pos.0 + x, pos.1)).unwrap() >= tree {
                    down = false;
                    break;
                }
            }

            left || right || up || down
        })
        .count() as i32
}

#[aoc(day8, part2)]
pub fn solve_part2(input: &InputType) -> i32 {
    // Do the same as part one, but instead of looking from the edge, look as
    // far as you can in each direction and multiply the number of trees that
    // can be seen

    // Find the max of the x and y of the hashmap
    let max_x = input.iter().map(|x| x.0 .1).max().unwrap();

    let max_y = input.iter().map(|x| x.0 .0).max().unwrap();

    // Go over every number in the hashmap, see if everything to either the
    // left, right, up or down is smaller than it. If so, return true.
    input
        .iter()
        .map(|(pos, tree)| {
            // Check left
            let mut left_count = 0;
            for x in 1..=pos.1 {
                if input.get(&(pos.0, pos.1 - x)).unwrap() >= tree {
                    left_count += 1;
                    break;
                }
                left_count += 1;
            }

            // Check right
            let mut right_count = 0;
            for x in 1..=max_y - pos.1 {
                if input.get(&(pos.0, pos.1 + x)).unwrap() >= tree {
                    right_count += 1;
                    break;
                }
                right_count += 1;
            }

            // Check up
            let mut up_count = 0;
            for x in 1..=pos.0 {
                if input.get(&(pos.0 - x, pos.1)).unwrap() >= tree {
                    up_count += 1;
                    break;
                }
                up_count += 1;
            }

            // Check down
            let mut down_count = 0;
            for x in 1..=max_x - pos.0 {
                if input.get(&(pos.0 + x, pos.1)).unwrap() >= tree {
                    down_count += 1;
                    break;
                }
                down_count += 1;
            }

            left_count * right_count * up_count * down_count
        })
        .max()
        .unwrap()
}
