mod day1;
mod input_snag;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 2 {
        println!("Whoops! You need to provide a session ID as an argument! Like this: cargo run -- <hex session id>");
        return;
    }

    println!("Day 1 Part 1: {}", day1::part1().unwrap());
    println!("Day 1 Part 2: {}", day1::part2().unwrap());
}
