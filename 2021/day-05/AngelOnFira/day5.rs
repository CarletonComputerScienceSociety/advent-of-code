use std::{
    cmp::{max, min},
    collections::HashMap,
};

use regex::Regex;

#[derive(Debug, PartialEq, Eq, Hash, Clone, Copy)]
pub struct Instruction {
    pub x1: i32,
    pub y1: i32,
    pub x2: i32,
    pub y2: i32,
}

#[aoc_generator(day5)]
pub fn input_generator(input: &str) -> Vec<Instruction> {
    // 498,436 -> 498,932
    // 173,176 -> 845,848
    // 927,799 -> 927,418
    // 576,67 -> 801,67
    // 908,147 -> 743,147
    // 300,478 -> 300,224
    // 286,979 -> 286,310
    // 230,435 -> 729,934
    // 260,602 -> 260,56
    // 82,686 -> 655,113
    // 460,918 -> 460,224
    // 191,820 -> 454,820
    // 964,483 -> 964,772

    input
        .lines()
        .map(|line| {
            let re = Regex::new(r"(\d+),(\d+) -> (\d+),(\d+)").unwrap();
            let caps = re.captures(line).unwrap();
            Instruction {
                x1: caps[1].parse::<i32>().unwrap(),
                y1: caps[2].parse::<i32>().unwrap(),
                x2: caps[3].parse::<i32>().unwrap(),
                y2: caps[4].parse::<i32>().unwrap(),
            }
        })
        .collect()
}

// Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

//     An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
//     An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

// For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

// In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

// To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

// Consider only horizontal and vertical lines. At how many points do at least two lines overlap?

#[aoc(day5, part1)]
pub fn solve_part1(input: &[Instruction]) -> i32 {
    let mut grid: HashMap<(i32, i32), i32> = HashMap::new();

    for instruction in input {
        println!("{:?}", instruction);
        let x1 = instruction.x1;
        let y1 = instruction.y1;
        let x2 = instruction.x2;
        let y2 = instruction.y2;

        if x1 == x2 {
            for y in min(y1, y2)..=max(y1, y2) {
                grid.entry((x1, y)).and_modify(|e| *e += 1).or_insert(1);
            }
        } else if y1 == y2 {
            for x in min(x1, x2)..=max(x1, x2) {
                grid.entry((x, y1)).and_modify(|e| *e += 1).or_insert(1);
            }
        }
    }

    // print out the grid
    for y in 0..=9 {
        for x in 0..=9 {
            print!("{}", grid.get(&(x, y)).unwrap_or(&0));
        }
        println!();
    }

    grid.values().filter(|&e| *e >= 2).count() as i32
}

#[aoc(day5, part2)]
pub fn solve_part2(input: &[Instruction]) -> i32 {
    let mut grid: HashMap<(i32, i32), i32> = HashMap::new();

    for instruction in input {
        // println!("{:?}", instruction);
        let x1 = instruction.x1;
        let y1 = instruction.y1;
        let x2 = instruction.x2;
        let y2 = instruction.y2;

        if x1 == x2 {
            for y in min(y1, y2)..=max(y1, y2) {
                grid.entry((x1, y)).and_modify(|e| *e += 1).or_insert(1);
            }
        } else if y1 == y2 {
            for x in min(x1, x2)..=max(x1, x2) {
                grid.entry((x, y1)).and_modify(|e| *e += 1).or_insert(1);
            }
        } else {
            // Unfortunately, considering only horizontal and vertical lines doesn't
            // give you the full picture; you need to also consider diagonal lines.

            // Because of the limits of the hydrothermal vent mapping system,
            // the lines in your list will only ever be horizontal, vertical, or
            // a diagonal line at exactly 45 degrees. In other words:

            // An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3. An
            // entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.

            // Find the left point

            let left_x = min(x1, x2);
            let left_y;
            let right_x;
            let right_y;
            if left_x == x1 {
                left_y = y1;
                right_x = x2;
                right_y = y2;
            } else {
                left_y = y2;
                right_x = x1;
                right_y = y1;
            }

            if left_y < right_y {
                for x in left_x..=right_x {
                    grid.entry((x, left_y + (x - left_x)))
                        .and_modify(|e| *e += 1)
                        .or_insert(1);
                }
            } else {
                for x in left_x..=right_x {
                    grid.entry((x, left_y - (x - left_x)))
                        .and_modify(|e| *e += 1)
                        .or_insert(1);
                }
            }
        }
    }

    // print out the grid
    for y in 0..=9 {
        for x in 0..=9 {
            print!("{}", grid.get(&(x, y)).unwrap_or(&0));
        }
        println!();
    }

    grid.values().filter(|&e| *e >= 2).count() as i32
}
