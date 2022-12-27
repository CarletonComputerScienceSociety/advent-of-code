use crate::input_snag::get_input;
use std::collections::HashMap;

pub fn part1() -> Result<i32, Box<dyn std::error::Error>>{
    let puzzle_input: String = get_input(2)?;
    let choice_scores: HashMap<&str, i32> = HashMap::from([
        ("X", 1),
        ("Y", 2),
        ("Z", 3)
    ]);
    let victory_conditions: HashMap<&str, &str> = HashMap::from([
        ("A", "Y"),
        ("B", "Z"),
        ("C", "X")
    ]);
    let draw_conditions: HashMap<&str, &str> = HashMap::from([
        ("A", "X"),
        ("B", "Y"),
        ("C", "Z")
    ]);

    let result = puzzle_input
        .lines()
        .fold(0, |acc, line| {
            let components: Vec<&str> = line.split(" ").collect();
            let choice_score = choice_scores.get(components[1]).unwrap();
            let outcome_score: i32;
            if victory_conditions.get(components[0]).unwrap() == &components[1] { 
                outcome_score = 6; 
            } 
            else if draw_conditions.get(components[0]).unwrap() == &components[1] {
                outcome_score = 3;
            }
            else { 
                outcome_score = 0; 
            };
            acc + choice_score + outcome_score
        });
    Ok(result)
}

pub fn part2() -> Result<i32, Box<dyn std::error::Error>>{
    let puzzle_input: String = get_input(2)?;
    let choice_scores: HashMap<&str, i32> = HashMap::from([
        ("A", 1),
        ("B", 2),
        ("C", 3)
    ]);
    let victory_conditions: HashMap<&str, &str> = HashMap::from([
        ("A", "B"),
        ("B", "C"),
        ("C", "A")
    ]);
    let defeat_conditions: HashMap<&str, &str> = HashMap::from([
        ("A", "C"),
        ("B", "A"),
        ("C", "B")
    ]);

    let result = puzzle_input
        .lines()
        .fold(0, |acc, line| {
            let components: Vec<&str> = line.split(" ").collect();
            let choice_score: i32;
            let outcome_score: i32;
            match components[1] {
                "X" => {
                    outcome_score = 0;
                    let choice = *defeat_conditions.get(components[0]).unwrap();
                    choice_score = *choice_scores.get(choice).unwrap();
                },
                "Y" => {
                    outcome_score = 3;
                    choice_score = *choice_scores.get(components[0]).unwrap();
                },
                "Z" => {
                    outcome_score = 6;
                    let choice = *victory_conditions.get(components[0]).unwrap();
                    choice_score = *choice_scores.get(choice).unwrap();
                },
                _ => { 
                    outcome_score = 0;
                    choice_score = 0;
                }
            }
            acc + choice_score + outcome_score
        });
    Ok(result)
}