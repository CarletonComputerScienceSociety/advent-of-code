use regex::Regex;

#[aoc_generator(day2)]
fn parse_input_day2(input: &str) -> Vec<(i32, i32, char, String)> {
    let re = Regex::new(r"(?P<lower>.*)-(?P<upper>.*) (?P<letter>.*): (?P<password>.*)").unwrap();

    input
        .lines()
        .map(|password| {
            let data = re.captures(password).unwrap();
            (
                data["lower"].parse::<i32>().unwrap(),
                data["upper"].parse::<i32>().unwrap(),
                data["letter"].parse::<char>().unwrap(),
                data["password"].parse::<String>().unwrap(),
            )
        })
        .collect()
}

#[aoc(day2, part1)]
pub fn solve_part1(input: &Vec<(i32, i32, char, String)>) -> i32 {
    input
        .iter()
        .filter(|password| {
            let count = password
                .3
                .chars()
                .filter(|letter| *letter == password.2)
                .count() as i32;
            count >= password.0 && count <= password.1
        })
        .count() as i32
}

#[aoc(day2, part2)]
pub fn solve_part2(input: &Vec<(i32, i32, char, String)>) -> i32 {
    input
        .iter()
        .filter(|password| {
            (password.3.chars().nth((password.0 - 1) as usize).unwrap() == password.2)
                ^ (password.3.chars().nth((password.1 - 1) as usize).unwrap() == password.2)
        })
        .count() as i32
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
