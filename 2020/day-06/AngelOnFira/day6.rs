use std::collections::HashMap;

#[aoc_generator(day6)]
fn parse_input_day6(input: &str) -> Vec<(HashMap<char, i32>, i32)> {
    let mut curr_group: HashMap<char, i32> = HashMap::new();
    let mut groups: Vec<(HashMap<char, i32>, i32)> = Vec::new();

    let mut voter_count = 0;
    for line in input.lines() {
        if line == "" {
            groups.push((curr_group.clone(), voter_count));
            curr_group = HashMap::new();
            voter_count = 0;
        } else {
            voter_count += 1;
            for character in line.chars() {
                *curr_group.entry(character).or_insert(0) += 1;
            }
        }
    }
    groups.push((curr_group.clone(), voter_count));

    groups.to_owned()
}

#[aoc(day6, part1)]
pub fn solve_part1(input: &Vec<(HashMap<char, i32>, i32)>) -> i32 {
    input.iter().map(|group| group.0.len() as i32).sum()
}

#[aoc(day6, part2)]
pub fn solve_part2(input: &Vec<(HashMap<char, i32>, i32)>) -> i32 {
    input
        .iter()
        .map(|group| group.0.values().filter(|&value| value == &group.1).count() as i32)
        .sum()
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
