use regex::Regex;
use std::collections::HashMap;

#[aoc_generator(day4)]
fn parse_input_day4(input: &str) -> Vec<HashMap<String, String>> {
    let mut curr_map: HashMap<String, String> = HashMap::new();
    let mut all_passports: Vec<HashMap<String, String>> = Vec::new();
    for line in input.lines() {
        if line == "" {
            all_passports.push(curr_map.clone());
            curr_map = HashMap::new();
        } else {
            for field in line.split(" ") {
                let field_split: Vec<String> = field
                    .split(":")
                    .map(|x| x.to_string())
                    .collect::<Vec<String>>();
                curr_map.insert(field_split[0].clone(), field_split[1].clone());
            }
        }
    }
    all_passports.push(curr_map.clone());

    // let re = Regex::new(r"(?P<lower>.*)-(?P<upper>.*) (?P<letter>.*): (?P<password>.*)").unwrap();

    all_passports.to_owned()
}

#[aoc(day4, part1)]
pub fn solve_part1(input: &Vec<HashMap<String, String>>) -> i32 {
    input
        .iter()
        .filter(|passport| {
            vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
                .iter()
                .all(|&field| passport.contains_key(field))
        })
        .count() as i32
}

#[aoc(day4, part2)]
pub fn solve_part2(input: &Vec<HashMap<String, String>>) -> i32 {
    input
        .iter()
        .filter(|passport| {
            vec!["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
                .iter()
                .all(|&field| match passport.get(field) {
                    Some(value) => match field {
                        "byr" => Regex::new(r"^19[2-9][\d]|200[0-2]$")
                            .unwrap()
                            .is_match(value),
                        "iyr" => Regex::new(r"^201[\d]|2020$").unwrap().is_match(value),
                        "eyr" => Regex::new(r"^202[\d]|2030$").unwrap().is_match(value),
                        "hgt" => Regex::new(r"^1[5-8][\d]cm|19[0-3]cm|59in|6[\d]in|7[0-6]in$")
                            .unwrap()
                            .is_match(value),
                        "hcl" => Regex::new(r"^#[\da-f]{6}$").unwrap().is_match(value),
                        "ecl" => vec!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                            .iter()
                            .any(|&color| color == value),
                        "pid" => Regex::new(r"^[\d]{9}$").unwrap().is_match(value),
                        _ => true,
                    },
                    None => false,
                })
        })
        .count() as i32
}

#[cfg(test)]
mod tests {
    // use super::solve_part1 as part1;
    // use super::solve_part2 as part2;
}
