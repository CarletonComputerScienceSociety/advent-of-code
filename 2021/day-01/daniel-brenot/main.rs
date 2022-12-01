use std::{fs, env, str::Split};


fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    let inputs: Vec<u64> = contents.split("\n").map(|a| str_to_num(a)).collect();

    part_one(&inputs);
    part_two(&inputs);
}

fn str_to_num(input: &str) -> u64{
    String::from(input).parse().expect("Failed to parse input as number")
}

/// I wrote this before i knew about .windows, and figured not to rewrite it with the new
/// method since i learned it from another contestant and the code i would make would be
/// the same as theirs. I'll know for next time :)
fn part_one(inputs: &Vec<u64>) {
    let mut inputs = inputs.iter();
    let mut increases = 0;
    let mut last_measurement = inputs.next().unwrap();
    // Split the file up on newlines
    for measurement in inputs {
        if measurement > last_measurement { increases += 1; }
        last_measurement = measurement;
    }
    println!("{}", increases);
}

/// In this part, I must give some credit to AngelOnFira.
/// I didn't know about the .windows method, and it made this much simpler
fn part_two(inputs: &Vec<u64>) {
    let sums = inputs.windows(3).map(|a| a.iter().sum());
    let increases = sums.collect::<Vec<u64>>().windows(2).filter(|a| { a[0] < a[1]}).count();
    println!("{}", increases);
}