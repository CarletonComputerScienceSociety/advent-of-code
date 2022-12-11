use std::{
    collections::{HashMap, HashSet},
    iter::FromIterator,
};

use itertools::Itertools;
use num_traits::Signed;
use regex::Regex;

type InputType = Vec<i128>;

#[aoc_generator(day11)]
fn parse_input_day11(input: &str) -> InputType {
    // Chars
    // input.chars().collect()

    // Map to ints
    // input.lines().map(|x| x.parse::<i128>().unwrap()).collect()

    Vec::new()

    // Regex
    // input.lines().map(|x| {}).collect()
}

// Monkey 0:
//   Starting items: 89, 73, 66, 57, 64, 80
//   Operation: new = old * 3
//   Test: divisible by 13
//     If true: throw to monkey 6
//     If false: throw to monkey 2

// Monkey 1:
//   Starting items: 83, 78, 81, 55, 81, 59, 69
//   Operation: new = old + 1
//   Test: divisible by 3
//     If true: throw to monkey 7
//     If false: throw to monkey 4

// Monkey 2:
//   Starting items: 76, 91, 58, 85
//   Operation: new = old * 13
//   Test: divisible by 7
//     If true: throw to monkey 1
//     If false: throw to monkey 4

// Monkey 3:
//   Starting items: 71, 72, 74, 76, 68
//   Operation: new = old * old
//   Test: divisible by 2
//     If true: throw to monkey 6
//     If false: throw to monkey 0

// Monkey 4:
//   Starting items: 98, 85, 84
//   Operation: new = old + 7
//   Test: divisible by 19
//     If true: throw to monkey 5
//     If false: throw to monkey 7

// Monkey 5:
//   Starting items: 78
//   Operation: new = old + 8
//   Test: divisible by 5
//     If true: throw to monkey 3
//     If false: throw to monkey 0

// Monkey 6:
//   Starting items: 86, 70, 60, 88, 88, 78, 74, 83
//   Operation: new = old + 4
//   Test: divisible by 11
//     If true: throw to monkey 1
//     If false: throw to monkey 2

// Monkey 7:
//   Starting items: 81, 58
//   Operation: new = old + 5
//   Test: divisible by 17
//     If true: throw to monkey 3
//     If false: throw to monkey 5

struct Monkey {
    starting_items: Vec<i128>,
    operation: Operation,
    inspection_count: i128,
    test: Test,
}

enum Operation {
    Multiply(i128),
    Add(i128),
    Square,
}

struct Test {
    divisor: i128,
    true_monkey: usize,
    false_monkey: usize,
}

#[aoc(day11, part1)]
pub fn solve_part1(input: &InputType) -> i128 {
    let monkey_0 = Monkey {
        starting_items: vec![89, 73, 66, 57, 64, 80],
        operation: Operation::Multiply(3),
        test: Test {
            divisor: 13,
            true_monkey: 6,
            false_monkey: 2,
        },
        inspection_count: 0,
    };

    let monkey_1 = Monkey {
        starting_items: vec![83, 78, 81, 55, 81, 59, 69],
        operation: Operation::Add(1),
        test: Test {
            divisor: 3,
            true_monkey: 7,
            false_monkey: 4,
        },
        inspection_count: 0,
    };

    let monkey_2 = Monkey {
        starting_items: vec![76, 91, 58, 85],
        operation: Operation::Multiply(13),
        test: Test {
            divisor: 7,
            true_monkey: 1,
            false_monkey: 4,
        },
        inspection_count: 0,
    };

    let monkey_3 = Monkey {
        starting_items: vec![71, 72, 74, 76, 68],
        operation: Operation::Square,
        test: Test {
            divisor: 2,
            true_monkey: 6,
            false_monkey: 0,
        },
        inspection_count: 0,
    };

    let monkey_4 = Monkey {
        starting_items: vec![98, 85, 84],
        operation: Operation::Add(7),
        test: Test {
            divisor: 19,
            true_monkey: 5,
            false_monkey: 7,
        },
        inspection_count: 0,
    };

    let monkey_5 = Monkey {
        starting_items: vec![78],
        operation: Operation::Add(8),
        test: Test {
            divisor: 5,
            true_monkey: 3,
            false_monkey: 0,
        },
        inspection_count: 0,
    };

    let monkey_6 = Monkey {
        starting_items: vec![86, 70, 60, 88, 88, 78, 74, 83],
        operation: Operation::Add(4),
        test: Test {
            divisor: 11,
            true_monkey: 1,
            false_monkey: 2,
        },
        inspection_count: 0,
    };

    let monkey_7 = Monkey {
        starting_items: vec![81, 58],
        operation: Operation::Add(5),
        test: Test {
            divisor: 17,
            true_monkey: 3,
            false_monkey: 5,
        },
        inspection_count: 0,
    };

    let mut monkeys = vec![
        monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7,
    ];

    let mut worry_level = 0;

    for round in 0..20 {
        for i in 0..monkeys.len() {
            // Go over each item in this monkey's inventory
            while monkeys[i].starting_items.len() > 0 {
                // Get the first item
                let item = monkeys[i].starting_items.remove(0);
                monkeys[i].inspection_count += 1;

                // Turn up the worry
                worry_level = match monkeys[i].operation {
                    Operation::Multiply(x) => item * x,
                    Operation::Add(x) => item + x,
                    Operation::Square => item * item,
                };

                // Turn down the worry
                worry_level /= 3;

                let true_monkey = monkeys[i].test.true_monkey;
                let false_monkey = monkeys[i].test.false_monkey;

                // Pass it on
                if worry_level % monkeys[i].test.divisor == 0 {
                    monkeys[true_monkey].starting_items.push(worry_level);
                } else {
                    monkeys[false_monkey].starting_items.push(worry_level);
                }
            }
        }

        // Print out all of the monkeys' held items
        for i in 0..monkeys.len() {
            println!("Monkey {}: {:?}", i, monkeys[i].starting_items);
        }
    }

    // Multiply the inspection count of the top 2 monkeys
    let mut counts = monkeys
        .iter()
        .map(|m| m.inspection_count)
        .collect::<Vec<i128>>();
    counts.sort();
    counts.iter().rev().take(2).product()
}

#[aoc(day11, part2)]
pub fn solve_part2(input: &InputType) -> i128 {
    let monkey_0 = Monkey {
        starting_items: vec![89, 73, 66, 57, 64, 80],
        operation: Operation::Multiply(3),
        test: Test {
            divisor: 13,
            true_monkey: 6,
            false_monkey: 2,
        },
        inspection_count: 0,
    };

    let monkey_1 = Monkey {
        starting_items: vec![83, 78, 81, 55, 81, 59, 69],
        operation: Operation::Add(1),
        test: Test {
            divisor: 3,
            true_monkey: 7,
            false_monkey: 4,
        },
        inspection_count: 0,
    };

    let monkey_2 = Monkey {
        starting_items: vec![76, 91, 58, 85],
        operation: Operation::Multiply(13),
        test: Test {
            divisor: 7,
            true_monkey: 1,
            false_monkey: 4,
        },
        inspection_count: 0,
    };

    let monkey_3 = Monkey {
        starting_items: vec![71, 72, 74, 76, 68],
        operation: Operation::Square,
        test: Test {
            divisor: 2,
            true_monkey: 6,
            false_monkey: 0,
        },
        inspection_count: 0,
    };

    let monkey_4 = Monkey {
        starting_items: vec![98, 85, 84],
        operation: Operation::Add(7),
        test: Test {
            divisor: 19,
            true_monkey: 5,
            false_monkey: 7,
        },
        inspection_count: 0,
    };

    let monkey_5 = Monkey {
        starting_items: vec![78],
        operation: Operation::Add(8),
        test: Test {
            divisor: 5,
            true_monkey: 3,
            false_monkey: 0,
        },
        inspection_count: 0,
    };

    let monkey_6 = Monkey {
        starting_items: vec![86, 70, 60, 88, 88, 78, 74, 83],
        operation: Operation::Add(4),
        test: Test {
            divisor: 11,
            true_monkey: 1,
            false_monkey: 2,
        },
        inspection_count: 0,
    };

    let monkey_7 = Monkey {
        starting_items: vec![81, 58],
        operation: Operation::Add(5),
        test: Test {
            divisor: 17,
            true_monkey: 3,
            false_monkey: 5,
        },
        inspection_count: 0,
    };

    let mut monkeys = vec![
        monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7,
    ];

    let divisors_product = monkeys
        .iter()
        .map(|monkey| monkey.test.divisor)
        .product::<i128>();

    let mut worry_level = 0;

    for round in 0..10000 {
        for i in 0..monkeys.len() {
            // Go over each item in this monkey's inventory
            while monkeys[i].starting_items.len() > 0 {
                // Get the first item
                let item = monkeys[i].starting_items.remove(0);
                monkeys[i].inspection_count += 1;

                // Turn up the worry
                worry_level = match monkeys[i].operation {
                    Operation::Multiply(x) => item * x,
                    Operation::Add(x) => item + x,
                    Operation::Square => item * item,
                };

                // Turn down the worry
                // worry_level /= 3;

                let true_monkey = monkeys[i].test.true_monkey;
                let false_monkey = monkeys[i].test.false_monkey;

                // Mod the worry level by the divisor_product before testing
                worry_level %= divisors_product;

                // Pass it on
                if worry_level % monkeys[i].test.divisor == 0 {
                    monkeys[true_monkey].starting_items.push(worry_level);
                } else {
                    monkeys[false_monkey].starting_items.push(worry_level);
                }
            }
        }

        // Print out all of the monkeys' held items
        for i in 0..monkeys.len() {
            println!("Monkey {}: {:?}", i, monkeys[i].starting_items);
        }
    }

    // Multiply the inspection count of the top 2 monkeys
    let mut counts = monkeys
        .iter()
        .map(|m| m.inspection_count)
        .collect::<Vec<i128>>();
    counts.sort();
    counts.iter().rev().take(2).product()
}
