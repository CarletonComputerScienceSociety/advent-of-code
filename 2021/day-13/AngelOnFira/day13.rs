use std::collections::{HashMap, HashSet};

use regex::Regex;

#[aoc_generator(day13)]
pub fn input_generator(input: &str) -> (HashSet<(i32, i32)>, Vec<(char, i32)>) {
    // 6,10
    // 0,14
    // 9,10
    // 0,3
    // 10,4
    // 4,11
    // 6,0
    // 6,12
    // 4,1
    // 0,13
    // 10,12
    // 3,4
    // 3,0
    // 8,4
    // 1,10
    // 2,14
    // 8,10
    // 9,0

    // fold along y=7
    // fold along x=5

    // get all coordinates into a hashmap
    let mut coords = HashSet::new();
    let re = Regex::new(r"(\d+),(\d+)").unwrap();
    for cap in re.captures_iter(input) {
        let x = cap[1].parse::<i32>().unwrap();
        let y = cap[2].parse::<i32>().unwrap();
        coords.insert((x, y));
    }

    // get all fold coordinates into a list
    let mut folds = Vec::new();
    let re = Regex::new(r"fold along (\w+)=(\d+)").unwrap();
    for cap in re.captures_iter(input) {
        let axis = cap[1].chars().next().unwrap();
        let val = cap[2].parse::<i32>().unwrap();
        folds.push((axis, val));
    }

    // dbg!(coords.clone());
    // dbg!(folds.clone());

    (coords, folds)
}

#[aoc(day13, part1)]
pub fn solve_part1(input: &(HashSet<(i32, i32)>, Vec<(char, i32)>)) -> i32 {
    // fold from the first instruction, count number of new points in set
    let (coords, folds) = input;
    let mut new_coords: HashSet<(i32, i32)> = HashSet::new();
    let mut cur_coords = coords.clone();

    // Print out the map
    for y in 0..=14 {
        for x in 0..=14 {
            if coords.contains(&(x, y)) {
                print!("#");
            } else {
                print!(".");
            }
        }
        println!();
    }

    for (axis, val) in folds {
        dbg!(axis, val);
        let mut new_cur_coords = HashSet::new();
        for coord in cur_coords.iter() {
            let (x, y) = coord;
            match axis {
                'x' => {
                    if &*x > val {
                        new_cur_coords.insert((val - (*x - val), *y));
                    } else {
                        new_cur_coords.insert((*x, *y));
                    }
                }
                'y' => {
                    if &*y > val {
                        new_cur_coords.insert((*x, val - (*y - val)));
                    } else {
                        new_cur_coords.insert((*x, *y));
                    }
                }
                _ => panic!("invalid axis"),
            }
        }

        // Print out the map
        for y in 0..=14 {
            for x in 0..=14 {
                if new_cur_coords.contains(&(x, y)) {
                    print!("#");
                } else {
                    print!(".");
                }
            }
            println!();
        }

        new_coords.extend(new_cur_coords.iter());
        cur_coords = new_cur_coords;
        break;
    }

    cur_coords.len() as i32
}

#[aoc(day13, part2)]
pub fn solve_part2(input: &(HashSet<(i32, i32)>, Vec<(char, i32)>)) -> i32 {
    // fold from the first instruction, count number of new points in set
    let (coords, folds) = input;
    let mut new_coords: HashSet<(i32, i32)> = HashSet::new();
    let mut cur_coords = coords.clone();

    // Print out the map
    for y in 0..=14 {
        for x in 0..=14 {
            if coords.contains(&(x, y)) {
                print!("#");
            } else {
                print!(".");
            }
        }
        println!();
    }

    for (axis, val) in folds {
        dbg!(axis, val);
        let mut new_cur_coords = HashSet::new();
        for coord in cur_coords.iter() {
            let (x, y) = coord;
            match axis {
                'x' => {
                    if &*x > val {
                        new_cur_coords.insert((val - (*x - val), *y));
                    } else {
                        new_cur_coords.insert((*x, *y));
                    }
                }
                'y' => {
                    if &*y > val {
                        new_cur_coords.insert((*x, val - (*y - val)));
                    } else {
                        new_cur_coords.insert((*x, *y));
                    }
                }
                _ => panic!("invalid axis"),
            }
        }

        // Print out the map
        for y in 0..=100 {
            for x in 0..=100 {
                if new_cur_coords.contains(&(x, y)) {
                    print!("#");
                } else {
                    print!(".");
                }
            }
            println!();
        }

        new_coords.extend(new_cur_coords.iter());
        cur_coords = new_cur_coords;
    }

    cur_coords.len() as i32
}
