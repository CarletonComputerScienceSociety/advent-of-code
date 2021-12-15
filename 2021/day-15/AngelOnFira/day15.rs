use std::collections::{HashMap, HashSet, VecDeque};

use itertools::Itertools;
use regex::Regex;

pub struct Instruction {}

#[aoc_generator(day15)]
pub fn input_generator(input: &str) -> Vec<Vec<i32>> {
    //1163751742
    //1381373672
    //2136511328
    //3694931569
    //7463417111
    //1319128137
    //1359912421
    //3125421639
    //1293138521
    //2311944581

    input
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(10).unwrap() as i32).collect())
        .collect()
}

#[aoc(day15, part1)]
pub fn solve_part1(input: &Vec<Vec<i32>>) -> i32 {
    // Find the way from the top left to the bottom right of the grid with the
    // lowest score of numbers in the path
    //
    // Use dijkstra's algorithm

    let mut grid = input.clone();
    let mut minimium_distance_to_pos = HashMap::new();

    // Initialize the grid with the first element
    let mut queue: Vec<(i32, (usize, usize))> = Vec::new();
    let mut visited = HashSet::new();
    queue.push((0, (0, 0)));

    while queue.len() > 0 {
        // Remove from queue
        queue.sort_by(|a, b| a.0.cmp(&b.0));
        let (distance, pos) = queue.remove(0);
        // let mut distance = minimium_distance_to_pos.get(&(x, y)).unwrap_or(&0).clone();

        let x = pos.0;
        let y = pos.1;

        // Add the neighbors to the queue
        let dirs: Vec<(i32, i32)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];

        for dir in dirs {
            let new_x = x + dir.0 as usize;
            let new_y = y + dir.1 as usize;

            if new_x < 0 || new_y < 0 || new_x >= grid.len() || new_y >= grid[0].len() {
                continue;
            }

            if visited.contains(&(new_x, new_y)) {
                continue;
            }

            let new_distance = distance + grid[new_x][new_y];
            minimium_distance_to_pos.insert((new_x, new_y), new_distance);
            queue.push((new_distance, (new_x, new_y)));
            visited.insert((new_x, new_y));
        }
    }

    *minimium_distance_to_pos
        .get(&(grid[0].len() - 1, grid.len() - 1))
        .unwrap()
}

#[aoc(day15, part2)]
pub fn solve_part2(input: &Vec<Vec<i32>>) -> i32 {
    // The entire cave is actually five times larger in both dimensions than you
    // thought; the area you originally scanned is just one tile in a 5x5 tile
    // area that forms the full map. Your original map tile repeats to the right
    // and downward; each time the tile repeats to the right or downward, all of
    // its risk levels are 1 higher than the tile immediately up or left of it.
    // However, risk levels above 9 wrap back around to 1.

    let mut grid: Vec<Vec<i32>> = Vec::new();

    for y in 0..5 * input.len() {
        let mut row: Vec<i32> = Vec::new();
        for x in 0..5 * input[0].len() {
            let reference = input[y % input.len()][x % input[0].len()];
            let mult = y / input.len() + x / input[0].len();
            let mut num = (reference + mult as i32);
            if num > 9 {
                num -= 9;
            }
            row.push(num);
        }
        grid.push(row);
    }

    // Print the grid

    for y in 0..grid.len() {
        for x in 0..grid[0].len() {
            print!("{}", grid[y][x]);
        }
        println!();
    }

    let mut minimium_distance_to_pos = HashMap::new();

    // Initialize the grid with the first element
    let mut queue: Vec<(i32, (usize, usize))> = Vec::new();
    let mut visited = HashSet::new();
    queue.push((0, (0, 0)));

    while queue.len() > 0 {
        // Remove from queue
        queue.sort_by(|a, b| a.0.cmp(&b.0));
        let (distance, pos) = queue.remove(0);
        // let mut distance = minimium_distance_to_pos.get(&(x, y)).unwrap_or(&0).clone();

        let x = pos.0;
        let y = pos.1;

        // Add the neighbors to the queue
        let dirs: Vec<(i32, i32)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];

        for dir in dirs {
            let new_x = x + dir.0 as usize;
            let new_y = y + dir.1 as usize;

            if new_x < 0 || new_y < 0 || new_x >= grid.len() || new_y >= grid[0].len() {
                continue;
            }

            if visited.contains(&(new_x, new_y)) {
                continue;
            }

            let new_distance = distance + grid[new_x][new_y];
            minimium_distance_to_pos.insert((new_x, new_y), new_distance);
            queue.push((new_distance, (new_x, new_y)));
            visited.insert((new_x, new_y));
        }
    }

    *minimium_distance_to_pos
        .get(&(grid[0].len() - 1, grid.len() - 1))
        .unwrap()
}
