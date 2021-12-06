use std::fs;

fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    let inputs: Vec<(&str, i64)> = contents.split("\n").map(|a| {
        let mut both = a.split(" ");
        let direction = both.next().unwrap();
        let distance = str_to_num(both.next().unwrap());
        (direction, distance)
    }).collect();

    part_one(&inputs);
    part_two(&inputs);
}

fn str_to_num(input: &str) -> i64{
    String::from(input).parse().expect("Failed to parse input as number")
}

fn part_one(inputs: &Vec<(&str, i64)>) {
    let mut horizontal: i64 = 0;
    let mut depth: i64 = 0;
    for (direction, distance) in inputs {
        match *direction{
            "forward" => horizontal += distance,
            "up" => depth -= distance,
            "down" => depth += distance,
            _ => {}
        }
    }
    println!("{}", horizontal * depth);
}

fn part_two(inputs: &Vec<(&str, i64)>) {
    let mut aim: i64 = 0;
    let mut horizontal: i64 = 0;
    let mut depth: i64 = 0;
    for (direction, distance) in inputs {
        match *direction {
            "forward" => {
                horizontal += distance;
                depth += aim * distance;
            },
            "up" => aim -= distance,
            "down" => aim += distance,
            _ => {}
        }
    }
    println!("{}", horizontal * depth);
}