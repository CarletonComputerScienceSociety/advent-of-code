use std::{cmp::min, collections::HashSet};

use itertools::Itertools;
use regex::Regex;

#[aoc_generator(day4)]
fn parse_input_day4(input: &str) -> Vec<(i32, i32, i32, i32)> {
    // 21-81,20-96
    // 14-80,14-79
    // 87-89,7-88
    let re = Regex::new(r"(?P<a>\d+)-(?P<b>\d+),(?P<c>\d+)-(?P<d>\d+)").unwrap();

    input
        .lines()
        .map(|pairs| {
            let data = re.captures(pairs).unwrap();
            (
                data["a"].parse::<i32>().unwrap(),
                data["b"].parse::<i32>().unwrap(),
                data["c"].parse::<i32>().unwrap(),
                data["d"].parse::<i32>().unwrap(),
            )
        })
        .collect()
}

#[aoc(day4, part1)]
pub fn solve_part1(input: &Vec<(i32, i32, i32, i32)>) -> i64 {
    input
        .iter()
        .filter(|x| {
            let range_a = (x.0..=x.1).collect::<HashSet<_>>();
            let range_b = (x.2..=x.3).collect::<HashSet<_>>();

            range_a.intersection(&range_b).count() == min(range_a.len(), range_b.len())
        })
        .count() as i64
}

#[aoc(day4, part2)]
pub fn solve_part2(input: &Vec<(i32, i32, i32, i32)>) -> i64 {
    input
        .iter()
        .filter(|x| {
            (x.0..=x.1)
                .collect::<HashSet<_>>()
                .intersection(&(x.2..=x.3).collect::<HashSet<_>>())
                .count()
                > 0
        })
        .count() as i64
}
