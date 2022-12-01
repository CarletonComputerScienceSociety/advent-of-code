use std::collections::HashMap;

use regex::Regex;

pub struct Instruction {
    pub from: String,
    pub to: String,
}

#[aoc_generator(day14)]
pub fn input_generator(input: &str) -> (String, HashMap<String, String>) {
    // CHBBKPHCPHPOKNSNCOVB
    //
    // SP -> K
    // BB -> H
    // BH -> S
    // BS -> H
    // PN -> P
    // OB -> S
    // ON -> C
    // HK -> K
    // BN -> V
    // OH -> F
    // OF -> C
    // SN -> N
    // PF -> H

    let mut map = HashMap::new();

    let re = Regex::new(r"(\w+) -> (\w+)").unwrap();
    for cap in re.captures_iter(input) {
        map.insert(cap[1].to_string(), cap[2].to_string());
    }

    (input.lines().next().unwrap().to_string(), map)
}

#[aoc(day14, part1)]
pub fn solve_part1(input: &(String, HashMap<String, String>)) -> i32 {
    let mut curr_string: Vec<char> = input.0.chars().collect();
    let map = input.1.clone();
    for i in 0..10 {
        // Iterate over each window of len 2
        let new_string = curr_string
            .windows(2)
            .map(|s| {
                let insert_char = map.get(&s.iter().collect::<String>()).unwrap();

                // s[0], insert_char
                format!("{}{}", s[0], insert_char)
            })
            .collect::<String>();

        // return new_string and the last character of curr_string
        curr_string = format!("{}{}", new_string, curr_string[curr_string.len() - 1])
            .chars()
            .collect();
    }

    let element_freq = curr_string.iter().fold(HashMap::new(), |mut acc, c| {
        *acc.entry(c).or_insert(0) += 1;
        acc
    });

    let most_common_element_count = element_freq.values().max().unwrap();
    let least_common_element_count = element_freq.values().min().unwrap();

    most_common_element_count - least_common_element_count
}

#[aoc(day14, part2)]
pub fn solve_part2(input: &(String, HashMap<String, String>)) -> i128 {
    let mut curr_string: Vec<char> = input.0.chars().collect();
    let map = input.1.clone();

    let mut count_map: HashMap<String, i128> = HashMap::new();

    for pair in curr_string.windows(2) {
        let comb = pair.iter().collect::<String>();

        count_map.entry(comb.clone()).or_insert(0);
        // Increase the count of the pair
        *count_map.get_mut(&comb).unwrap() += 1;
    }

    let mut old_count_map: HashMap<String, i128> = count_map.clone();
    for i in 0..40 {
        let mut new_count_map = HashMap::new();

        // Iterate over every item in the old_count_map
        for (key, value) in old_count_map.iter() {
            let mid = map.get(&key.clone()).unwrap();
            let first_half = format!("{}{}", key.chars().next().unwrap(), mid);
            let second_half = format!("{}{}", mid, key.chars().last().unwrap());

            // new_count_map.entry(key.clone()).or_insert(0);
            // *new_count_map.get_mut(&key.clone()).unwrap() += value;

            new_count_map.entry(first_half.clone()).or_insert(0);
            *new_count_map.get_mut(&first_half).unwrap() += value;

            new_count_map.entry(second_half.clone()).or_insert(0);
            *new_count_map.get_mut(&second_half).unwrap() += value;
        }

        dbg!(new_count_map.clone());

        old_count_map = new_count_map;
    }

    // Count up the number of occurrences of characters in keys multiplied by the value
    let letter_hashmap = old_count_map
        .iter()
        .fold(HashMap::new(), |mut acc, (key, value)| {
            for c in key.chars().rev() {
                acc.entry(c).or_insert(0);
                *acc.get_mut(&c).unwrap() += *value;
                break;
            }
            acc
        });

    dbg!(letter_hashmap.clone());

    let most_common_element_count = *letter_hashmap.values().max().unwrap() as i128;
    let least_common_element_count = *letter_hashmap.values().min().unwrap() as i128;

    most_common_element_count - least_common_element_count
}
