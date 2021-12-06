use std::fs;


fn main() {
    let filename = "input.txt";
    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");
    let inputs: Vec<u8> = contents.split(",").map(|a| str_to_num(a)).collect();

    //part_one(inputs);
    part_two(inputs);
}

fn str_to_num(input: &str) -> u8{
    String::from(input).parse().expect("Failed to parse input as number")
}

fn part_one(inputs: Vec<u8>) {
    simulate(inputs, 80);
}

fn part_two(inputs: Vec<u8>) {
    simulate(inputs, 256);
}

fn simulate(inputs: Vec<u8>, days: u32) {
    let mut sums: [u64; 9] = [0,0,0,0,0,0,0,0,0];
    for i in inputs {
        sums[i as usize] += 1;
    }
    for day in 0..days {
        let new_fish = sums[0];
        sums[0] = 0;
        for i in 1..sums.len() {
            sums[i-1] += sums[i];
            sums[i] = 0;
        }
        sums[6] += new_fish;
        sums[8] = new_fish;
    }
    println!("{}", sums.iter().sum::<u64>());
}