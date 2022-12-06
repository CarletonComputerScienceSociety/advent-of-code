use std::{fs::File, io::{BufReader, BufRead}};

fn read_input(source: String) -> Vec<String> {
    let file = File::open(source).expect("No such file");
    let buf = BufReader::new(file);
    buf.lines()
       .map(|l| l.expect("Could not parse line"))
       .collect()
}

fn part1 (input: &Vec<String>) -> u32 {
    let mut sum:u32 = 0;
    input.into_iter()
         .for_each(|l| {
            match l.as_str() {
                "A X" => sum += 1 + 3,
                "A Y" => sum += 2 + 6,
                "A Z" => sum += 3 + 0,

                "B X" => sum += 1 + 0,
                "B Y" => sum += 2 + 3,
                "B Z" => sum += 3 + 6,

                "C X" => sum += 1 + 6,
                "C Y" => sum += 2 + 0,
                "C Z" => sum += 3 + 3,

                _ => sum = sum,
            }
         });
    return sum
}

fn part2(input: &Vec<String>) -> u32 {
    let mut sum: u32 = 0;
    input.into_iter()
         .for_each(|l| {
            match l.as_str() {
                "A X" => sum += 3 + 0,
                "A Y" => sum += 1 + 3,
                "A Z" => sum += 2 + 6,

                "B X" => sum += 1 + 0,
                "B Y" => sum += 2 + 3,
                "B Z" => sum += 3 + 6,

                "C X" => sum += 2 + 0,
                "C Y" => sum += 3 + 3,
                "C Z" => sum += 1 + 6,

                _ => sum = sum,
            }
         });

    return sum;
}

fn main() {
    let data = read_input("input".to_owned());

    let p1 = part1(&data);
    let p2 = part2(&data);

    print!("Part1 = {}\n", p1);
    print!("Part2 = {}\n", p2);
}

