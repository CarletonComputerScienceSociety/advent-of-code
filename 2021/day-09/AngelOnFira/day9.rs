use std::collections::HashSet;

use regex::Regex;

pub struct Instruction {}

#[aoc_generator(day9)]
pub fn input_generator(input: &str) -> Vec<Vec<i32>> {
    // 5456898789432369879876542123489327657987856789656799875436567999109876543212345679832223569876567892
    // 4345987678953459767989654345678916549876545689345987654323499878998765432101234599741012456997456901
    // 3239876565694569653298797656989301234998659793239998789019988769889887643542345987632124669984345893
    // 2198765464689698932129898987993212356799798910198999898998767456778998755643959876545234798763234689
    // 1019874323494987891034999698954324467892987891987899987859654327867899876659898989876345679854347792

    // parse into vector of vectors as single numbers

    let mut result: Vec<Vec<i32>> = Vec::new();
    for line in input.lines() {
        let mut line_vec: Vec<i32> = Vec::new();
        for character in line.chars() {
            line_vec.push(character.to_digit(10).unwrap() as i32);
        }
        result.push(line_vec);
    }
    result
}

#[aoc(day9, part1)]
pub fn solve_part1(input: &[Vec<i32>]) -> i32 {
    // Your first goal is to find the low points - the locations that are lower
    // than any of its adjacent locations. Most locations have four adjacent
    // locations (up, down, left, and right); locations on the edge or corner of
    // the map have three or two adjacent locations, respectively. (Diagonal
    // locations do not count as adjacent.)

    // In the above example, there are four low points, all highlighted: two are
    // in the first row (a 1 and a 0), one is in the third row (a 5), and one is
    // in the bottom row (also a 5). All other locations on the heightmap have
    // some lower adjacent location, and so are not low points.

    // The risk level of a low point is 1 plus its height. In the above example,
    // the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk
    // levels of all low points in the heightmap is therefore 15.

    // What is the sum of the risk levels of the low points?

    let mut sum = 0;
    for i in 0..input.len() {
        for j in 0..input[i].len() {
            let mut low_point = true;
            if i > 0 {
                if input[i - 1][j] <= input[i][j] {
                    low_point = false;
                }
            }
            if i < input.len() - 1 {
                if input[i + 1][j] <= input[i][j] {
                    low_point = false;
                }
            }
            if j > 0 {
                if input[i][j - 1] <= input[i][j] {
                    low_point = false;
                }
            }
            if j < input[i].len() - 1 {
                if input[i][j + 1] <= input[i][j] {
                    low_point = false;
                }
            }
            if low_point {
                dbg!(input[i][j]);
                sum += input[i][j] + 1;
            }
        }
    }
    sum
}

fn find_basin_size(map: Vec<Vec<i32>>, curr_x: usize, curr_y: usize) -> i32 {
    let mut size = 0;
    let mut to_search: Vec<(usize, usize)> = Vec::new();
    to_search.push((curr_x, curr_y));

    let mut already_searched: HashSet<(usize, usize)> = HashSet::new();

    while to_search.len() > 0 {
        let (x, y) = to_search.pop().unwrap();
        if already_searched.contains(&(x, y)) {
            continue;
        }
        already_searched.insert((x, y));
        size += 1;
        if x > 0 {
            if map[x - 1][y] != 9 && !already_searched.contains(&(x - 1, y)) {
                to_search.push((x - 1, y));
            }
        }
        if x < map.len() - 1 {
            if map[x + 1][y] != 9 && !already_searched.contains(&(x + 1, y)) {
                to_search.push((x + 1, y));
            }
        }
        if y > 0 {
            if map[x][y - 1] != 9 && !already_searched.contains(&(x, y - 1)) {
                to_search.push((x, y - 1));
            }
        }
        if y < map[x].len() - 1 {
            if map[x][y + 1] != 9 && !already_searched.contains(&(x, y + 1)) {
                to_search.push((x, y + 1));
            }
        }
    }
    size
}

#[aoc(day9, part2)]
pub fn solve_part2(input: &[Vec<i32>]) -> i32 {
    // a basin is a region of the map that is lower than any of its adjacent

    let mut found_basins: HashSet<(usize, usize)> = HashSet::new();

    let mut found_basin_sizes: Vec<i32> = Vec::new();

    let mut sum = 0;
    for i in 0..input.len() {
        for j in 0..input[i].len() {
            // If we have already found a basin, skip this point
            if found_basins.contains(&(i, j)) {
                continue;
            }
            let mut low_point = true;
            if i > 0 {
                if input[i - 1][j] <= input[i][j] {
                    low_point = false;
                }
            }
            if i < input.len() - 1 {
                if input[i + 1][j] <= input[i][j] {
                    low_point = false;
                }
            }
            if j > 0 {
                if input[i][j - 1] <= input[i][j] {
                    low_point = false;
                }
            }
            if j < input[i].len() - 1 {
                if input[i][j + 1] <= input[i][j] {
                    low_point = false;
                }
            }
            if low_point {
                found_basin_sizes.push(find_basin_size(input.to_vec(), i, j));
            }
        }
    }

    // multiply the largest 3 together and return
    found_basin_sizes.sort();
    found_basin_sizes.reverse();
    found_basin_sizes[0..3].iter().product::<i32>()
}
