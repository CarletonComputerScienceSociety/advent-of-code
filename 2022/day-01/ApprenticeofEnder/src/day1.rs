use crate::input_snag::get_input;

pub fn part1() -> Result<i32, Box<dyn std::error::Error>>{
    let puzzle_input: String = get_input(1)?;
    let mut calorie_counts: Vec<i32> = vec![0];

    puzzle_input.split("\n").into_iter().for_each(|line| {
        if line == "" {
            calorie_counts.push(0);
        }
        else {
            let last_calorie_count = calorie_counts.len() - 1;
            calorie_counts[last_calorie_count] += line.parse::<i32>().unwrap();
        }
    });
    Ok(*calorie_counts.iter().max().unwrap())
}

pub fn part2() -> Result<i32, Box<dyn std::error::Error>>{
    let puzzle_input: String = get_input(1)?;
    let mut calorie_counts: Vec<i32> = vec![0];

    puzzle_input.split("\n").into_iter().for_each(|line| {
        if line == "" {
            calorie_counts.push(0);
        }
        else {
            let last_calorie_count = calorie_counts.len() - 1;
            calorie_counts[last_calorie_count] += line.parse::<i32>().unwrap();
        }
    });
    calorie_counts.sort();
    let top_3_sum: i32 = calorie_counts.iter().rev().take(3).sum();
    Ok(top_3_sum)
}