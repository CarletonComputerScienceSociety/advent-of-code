use std::{
    cmp::max,
    collections::{HashMap, HashSet},
    iter::FromIterator,
};

use itertools::Itertools;
use num_traits::Signed;
use regex::Regex;

type InputType = Vec<(String, i32)>;

#[aoc_generator(day9)]
fn parse_input_day9(input: &str) -> InputType {
    // U 1
    // L 2
    // U 2
    // D 2
    // L 2
    // U 1
    // D 1
    // U 2
    // D 1
    // U 2
    // D 1
    // R 2
    // U 2

    input
        .lines()
        .map(|x| {
            (
                x.split(" ").collect::<Vec<&str>>()[0].to_string(),
                x.split(" ").collect::<Vec<&str>>()[1]
                    .parse::<i32>()
                    .unwrap(),
            )
        })
        .collect()
}

#[aoc(day9, part1)]
pub fn solve_part1(input: &InputType) -> i32 {
    let mut pos = (0, 0);
    let mut map = HashMap::new();

    let mut tail_visited_positions = HashSet::new();

    let mut tail_pos = (0, 0);

    for instruction in input {
        for _ in 0..instruction.1 {
            match instruction.0.as_str() {
                "U" => {
                    pos.1 += 1;
                    map.insert(pos, 0);
                }
                "D" => {
                    pos.1 -= 1;
                    map.insert(pos, 0);
                }
                "L" => {
                    pos.0 -= 1;
                    map.insert(pos, 0);
                }
                "R" => {
                    pos.0 += 1;
                    map.insert(pos, 0);
                }
                _ => {}
            }

            // Make sure the tail is at most 1 away from the head. If it's further,
            // move it closer.

            let manhattan_distance = max((pos.0 - tail_pos.0).abs(), (pos.1 - tail_pos.1).abs());

            if manhattan_distance > 1 {
                // Move the tail closer to the head
                if instruction.0.as_str() == "L" || instruction.0.as_str() == "R" {
                    if pos.0 > tail_pos.0 {
                        tail_pos.0 += 1;
                        tail_pos.1 = pos.1;
                    } else if pos.0 < tail_pos.0 {
                        tail_pos.0 -= 1;
                        tail_pos.1 = pos.1;
                    }
                } else if instruction.0.as_str() == "D" || instruction.0.as_str() == "U" {
                    if pos.1 > tail_pos.1 {
                        tail_pos.1 += 1;
                        tail_pos.0 = pos.0;
                    } else if pos.1 < tail_pos.1 {
                        tail_pos.1 -= 1;
                        tail_pos.0 = pos.0;
                    }
                }
            }

            // Draw the map in the range -10 to 10
            for y in -5..=5 {
                for x in -5..=5 {
                    if (x, y) == pos {
                        print!("H");
                    } else if (x, y) == tail_pos {
                        print!("T");
                    } else if (x, y) == (0, 0) {
                        print!("s");
                    } else {
                        print!(".");
                    }
                }
                println!();
            }

            println!();
            println!();
            tail_visited_positions.insert(tail_pos);
        }
    }

    // Return the number of places the tail has been
    tail_visited_positions.len() as i32
}

#[aoc(day9, part2)]
pub fn solve_part2(input: &InputType) -> i32 {
    // The snake is 10 long
    let mut snake_body = vec![
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ];

    let mut tail_visited_positions = HashSet::new();

    for instruction in input {
        for _ in 0..instruction.1 {
            // Move the first body part
            match instruction.0.as_str() {
                "U" => {
                    snake_body[0].1 += 1;
                }
                "D" => {
                    snake_body[0].1 -= 1;
                }
                "L" => {
                    snake_body[0].0 -= 1;
                }
                "R" => {
                    snake_body[0].0 += 1;
                }
                _ => {}
            }

            for i in 0..snake_body.len() {
                // Skip the head
                if i == 0 {
                    continue;
                }

                let manhattan_distance = max(
                    (snake_body[i].0 - snake_body[i - 1].0).abs(),
                    (snake_body[i].1 - snake_body[i - 1].1).abs(),
                );

                let lead = snake_body[i - 1];
                let follow = snake_body[i];

                // If we're not touching on either, move closer diagonally
                if snake_body[i].0 != snake_body[i - 1].0
                    && snake_body[i].1 != snake_body[i - 1].1
                    && manhattan_distance > 1
                {
                    if lead.0 > follow.0 && lead.1 > follow.1 {
                        snake_body[i].0 += 1;
                        snake_body[i].1 += 1;
                    } else if lead.0 > follow.0 && lead.1 < follow.1 {
                        snake_body[i].0 += 1;
                        snake_body[i].1 -= 1;
                    } else if lead.0 < follow.0 && lead.1 > follow.1 {
                        snake_body[i].0 -= 1;
                        snake_body[i].1 += 1;
                    } else if lead.0 < follow.0 && lead.1 < follow.1 {
                        snake_body[i].0 -= 1;
                        snake_body[i].1 -= 1;
                    }
                }
                // Otherwise, if only one column is the same, move closer vertically
                else if (snake_body[i].0 != snake_body[i - 1].0
                    || snake_body[i].1 != snake_body[i - 1].1)
                    && manhattan_distance > 1
                {
                    if lead.0 > follow.0 {
                        snake_body[i].0 += 1;
                    } else if lead.0 < follow.0 {
                        snake_body[i].0 -= 1;
                    } else if lead.1 > follow.1 {
                        snake_body[i].1 += 1;
                    } else if lead.1 < follow.1 {
                        snake_body[i].1 -= 1;
                    }
                }
            }

            // Make sure the tail is at most 1 away from the head. If it's further,
            // move it closer.

            // Draw the map in the range -10 to 10
            for y in -10..=10 {
                for x in -10..=10 {
                    let mut test = true;
                    for (i, body_part) in snake_body.iter().enumerate() {
                        if (x, y) == *body_part {
                            print!("{}", i);
                            test = false;
                            break;
                        }
                    }

                    if test {
                        print!(".");
                    }
                }
                println!();
            }

            println!();
            println!();
            tail_visited_positions.insert(snake_body[snake_body.len() - 1]);
        }
    }

    // Return the number of places the tail has been
    tail_visited_positions.len() as i32
}
