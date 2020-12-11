use std::collections::HashSet;

#[aoc_generator(day8)]
fn parse_input_day8(input: &str) -> Vec<(String, i32)> {
    input
        .lines()
        .map(|input| {
            let instruction: Vec<String> = input.split(" ").map(|x| x.to_string()).collect();
            (
                instruction[0].to_owned(),
                instruction[1].parse::<i32>().unwrap(),
            )
        })
        .collect()
}

#[aoc(day8, part1)]
pub fn solve_part1(input: &Vec<(String, i32)>) -> i32 {
    let mut counter = 0;
    let mut acc = 0;
    let mut seen = HashSet::new();

    while counter < input.len() {
        let instruction = input[counter].clone();
        let value = instruction.1;
        match &instruction.0[..] {
            "nop" => counter += 1,
            "acc" => {
                acc += value;
                counter += 1;
            }
            "jmp" => counter += value as usize,
            _ => unreachable!(),
        }
        if !seen.insert(counter) {
            return acc as i32;
        }
    }
    unreachable!()
}

#[aoc(day8, part2)]
pub fn solve_part2(input: &Vec<(String, i32)>) -> i32 {
    let mut mut_input = input.clone();
    for i in 0..mut_input.len() {
        let mut counter = 0;
        let mut acc = 0;
        let mut seen = HashSet::new();
        match &mut_input[i].0[..] {
            "nop" => mut_input[i].0 = "jmp".to_string(),
            "jmp" => mut_input[i].0 = "nop".to_string(),
            _ => continue,
        }
        let mut found = true;
        while counter < mut_input.len() {
            let instruction = mut_input[counter].clone();
            let value = instruction.1;
            match &instruction.0[..] {
                "nop" => counter += 1,
                "acc" => {
                    acc += value;
                    counter += 1;
                }
                "jmp" => counter += value as usize,
                _ => unreachable!(),
            }
            if !seen.insert(counter) {
                found = false;
                break;
            }
        }
        if found {
            return acc;
        }
        match &mut_input[i].0[..] {
            "nop" => mut_input[i].0 = "jmp".to_string(),
            "jmp" => mut_input[i].0 = "nop".to_string(),
            _ => unreachable!(),
        }
    }
    unreachable!()
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
