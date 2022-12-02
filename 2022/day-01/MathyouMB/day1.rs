use std::fs::File;
use std::io::prelude::*;

fn main() {
    // get the data from file
    let mut file = File::open("input.txt")
        .expect("File not found");

    let mut data = String::new();

    file.read_to_string(&mut data)
        .expect("Error while reading file");
    
    // sum the calorie counts of each elf
    let mut v: Vec<i32> = Vec::new();
    let mut sum = 0;
    for line in data.lines() {        
        if line.is_empty() {
            v.push(sum);
            sum = 0;
        } else {
            sum += line.parse::<i32>().unwrap();
        }
    }

    // get three highest calorie counts
    v.sort();
    v.reverse();
    v.truncate(3);

    // get the sum of the three highest calorie counts
    let mut sum = 0;
    for i in &v {
        sum += i;
    }

    // print highest elf calorie count
    println!("P1: {}", v[0]);

    // print the sum
    println!("P2: {}", sum);
}
