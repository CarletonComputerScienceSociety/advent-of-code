use regex::Regex;

pub struct Instruction {}

#[aoc_generator(day7)]
pub fn input_generator(input: &str) -> Vec<i32> {
    // 16,1,2,0,4,2,7,1,2,14
    input
        .split(",")
        .map(|x| x.parse::<i32>().unwrap())
        .collect()
}

#[aoc(day7, part1)]
pub fn solve_part1(input: &[i32]) -> i32 {
    // You quickly make a list of the horizontal position of each crab (your
    // puzzle input). Crab submarines have limited fuel, so you need to find a
    // way to make all of their horizontal positions match while requiring them
    // to spend as little fuel as possible.

    // For example, consider the following horizontal positions:

    // 16,1,2,0,4,2,7,1,2,14

    // This means there's a crab with horizontal position 16, a crab with
    // horizontal position 1, and so on.

    // Each change of 1 step in horizontal position of a single crab costs 1
    // fuel. You could choose any horizontal position to align them all on, but
    // the one that costs the least fuel is horizontal position 2:

    //     Move from 16 to 2: 14 fuel Move from 1 to 2: 1 fuel Move from 2 to 2:
    //     0 fuel Move from 0 to 2: 2 fuel Move from 4 to 2: 2 fuel Move from 2
    //     to 2: 0 fuel Move from 7 to 2: 5 fuel Move from 1 to 2: 1 fuel Move
    //     from 2 to 2: 0 fuel Move from 14 to 2: 12 fuel

    // This costs a total of 37 fuel. This is the cheapest possible outcome;
    // more expensive outcomes include aligning at position 1 (41 fuel),
    // position 3 (39 fuel), or position 10 (71 fuel).

    // Determine the horizontal position that the crabs can align to using the
    // least fuel possible. How much fuel must they spend to align to that
    // position?

    let mut min_fuel = std::i32::MAX;
    let mut min_position = 0;

    for i in *input.iter().min().unwrap()..*input.iter().max().unwrap() {
        let mut fuel = 0;
        for x in input.iter() {
            fuel += (i - x).abs();
        }
        if fuel < min_fuel {
            min_fuel = fuel;
            min_position = i;
        }
    }

    min_fuel
}

fn get_sum(n: i32) -> i32 {
    let mut sum = 0;
    for i in 0..=n {
        sum += i;
    }
    sum
}

#[aoc(day7, part2)]
pub fn solve_part2(input: &[i32]) -> i32 {
    //     The crabs don't seem interested in your proposed solution. Perhaps you
    //     misunderstand crab engineering?

    // As it turns out, crab submarine engines don't burn fuel at a constant rate.
    // Instead, each change of 1 step in horizontal position costs 1 more unit of
    // fuel than the last: the first step costs 1, the second step costs 2, the
    // third step costs 3, and so on.

    // As each crab moves, moving further becomes more expensive. This changes the
    // best horizontal position to align them all on; in the example above, this
    // becomes 5:

    //     Move from 16 to 5: 66 fuel Move from 1 to 5: 10 fuel Move from 2 to 5: 6
    //     fuel Move from 0 to 5: 15 fuel Move from 4 to 5: 1 fuel Move from 2 to 5:
    //     6 fuel Move from 7 to 5: 3 fuel Move from 1 to 5: 10 fuel Move from 2 to
    //     5: 6 fuel Move from 14 to 5: 45 fuel

    // This costs a total of 168 fuel. This is the new cheapest possible outcome;
    // the old alignment position (2) now costs 206 fuel instead.

    // Determine the horizontal position that the crabs can align to using the least
    // fuel possible so they can make you an escape route! How much fuel must they
    // spend to align to that position?

    let mut min_fuel = std::i32::MAX;
    let mut min_position = 0;

    for i in *input.iter().min().unwrap()..*input.iter().max().unwrap() {
        let mut fuel = 0;
        for x in input.iter() {
            fuel += get_sum((i - x).abs());
        }
        if fuel < min_fuel {
            min_fuel = fuel;
            min_position = i;
        }
    }

    min_fuel
}
