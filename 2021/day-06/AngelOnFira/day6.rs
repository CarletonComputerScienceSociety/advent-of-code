use regex::Regex;

pub struct Instruction {}

#[aoc_generator(day6)]
pub fn input_generator(input: &str) -> Vec<i32> {
    // 3,4,3,1,2
    input
        .split(',')
        .map(|x| x.parse::<i32>().unwrap())
        .collect()
}

#[aoc(day6, part1)]
pub fn solve_part1(input: &[i32]) -> i32 {
    // A lanternfish that creates a new fish resets its timer to 6, not 7
    // (because 0 is included as a valid timer value). The new lanternfish
    // starts with an internal timer of 8 and does not start counting down until
    // the next day.

    // Realizing what you're trying to do, the submarine automatically produces
    // a list of the ages of several hundred nearby lanternfish (your puzzle
    // input). For example, suppose you were given the following list:

    // 3,4,3,1,2

    // This list means that the first fish has an internal timer of 3, the
    // second fish has an internal timer of 4, and so on until the fifth fish,
    // which has an internal timer of 2. Simulating these fish over several days
    // would proceed as follows:

    let mut fish = input.to_vec();

    for i in 0..80 {
        let mut to_add = 0;
        for j in 0..fish.len() {
            fish[j] -= 1;
            if fish[j] == -1 {
                fish[j] = 6;
                to_add += 1;
            }
        }

        for _ in 0..to_add {
            fish.push(8);
        }
    }

    fish.iter().count() as i32
}

#[aoc(day6, part2)]
pub fn solve_part2(input: &[i32]) -> i64 {
    let mut fish = input.to_vec();

    let mut health: [i64; 9] = [0, 0, 0, 0, 0, 0, 0, 0, 0];

    for x in fish {
        health[x as usize] += 1;
    }

    for i in 0..256 {
        dbg!(health);
        let old = health[0];

        for j in 0..8 {
            health[j] = health[j + 1];
        }

        health[6] += old;
        health[8] = old;
    }

    health.iter().sum::<i64>()
}
