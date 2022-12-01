use std::{collections::HashSet, io::BufRead};

use regex::Regex;

pub struct Instruction {}

#[aoc_generator(day8)]
pub fn input_generator(input: &str) -> Vec<Vec<String>> {
    // fgcae ebafc cabdef eg abecfg abgfed feg gafdc bceg ebgcadf | defagbc faecg cfdag gecb
    // eagd cad fgadbc aefdcg dcebfg fcegd cbeaf ad dbgfeca defca | cfdeg gdcabf fcgde afgced
    // gfdeca aeb eb fbdag eafdc adfbe cefdab bdaegcf efbc ecadgb | eb dbafe eab faecd
    // facbdge efdg gcafd daegc caegb aecfdb ade ed gafbdc dgfeac | de abcdef faedcg dfgca

    // split into 11 strings

    input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|word| word.to_string())
                .collect()
        })
        .collect()
}

#[aoc(day8, part1)]
pub fn solve_part1(input: &[Vec<String>]) -> i32 {
    // dbg!(input);
    let mut count = 0;

    for line in input {
        // Create sets of each letter

        // Only count after the pipe

        for word in &line[10..] {
            let mut letters: HashSet<char> = HashSet::new();
            for letter in word.chars() {
                letters.insert(letter);
            }
            let check = vec![2, 3, 4, 7];
            if check.contains(&letters.len()) {
                count += 1;
            }
        }
    }
    count
}

#[aoc(day8, part2)]
pub fn solve_part2(input: &[Vec<String>]) -> i32 {
    // dbg!(input);
    let mut count = 0;

    for line in input {
        // Create sets of each letter

        // Only count after the pipe

        let mut wordlist: [HashSet<char>; 10] = [
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
            HashSet::new(),
        ];

        for word in &line[..=10] {
            let mut letters: HashSet<char> = HashSet::new();
            for letter in word.chars() {
                letters.insert(letter);
            }

            let check = vec![2, 3, 4, 7];
            if check.contains(&letters.len()) {
                match letters.len() {
                    2 => wordlist[1] = letters.clone(),
                    3 => wordlist[7] = letters.clone(),
                    4 => wordlist[4] = letters.clone(),
                    7 => wordlist[8] = letters.clone(),
                    _ => {}
                }
            }
        }

        for word in &line[..=10] {
            let mut letters: HashSet<char> = HashSet::new();
            for letter in word.chars() {
                letters.insert(letter);
            }

            if !wordlist.contains(&letters) {
                // 9 is 4 and 7
                // if letters == wordlist[4].union(&wordlist[7]).map(|x| x.clone()).collect() {
                //     wordlist[9] = letters.clone();
                // }
                // 2 can combine 4 to get 8
                if letters.len() == 5 as usize
                    && wordlist[8]
                        == letters
                            .clone()
                            .union(&wordlist[4])
                            .map(|x| x.clone())
                            .collect()
                {
                    wordlist[2] = letters.clone();
                }
                // 6 can combine 1 to get 8
                else if letters.len() == 6 as usize
                    && wordlist[8]
                        == letters
                            .clone()
                            .union(&wordlist[1])
                            .map(|x| x.clone())
                            .collect()
                {
                    wordlist[6] = letters.clone();
                }
            }
        }

        // done 1, 7, 4, 8, 2, 6
        // need 0, 5, 3, 9

        for word in &line[..=10] {
            let mut letters: HashSet<char> = HashSet::new();
            for letter in word.chars() {
                letters.insert(letter);
            }

            if !wordlist.contains(&letters) {
                // Get 6 and 0
                // if letters
                //     .difference(&letters.union(&wordlist[7]).map(|x| x.clone()).collect())
                //     .count()
                //     == 0
                // {
                //     // Same is 0
                //     dbg!("zero");
                //     wordlist[0] = letters.clone();
                // } else {
                //     // Different is 6
                //     wordlist[6] = letters.clone();
                // }

                // 5 and 2 are 8
                if letters.len() == 5
                    && wordlist[8]
                        == letters
                            .clone()
                            .union(&wordlist[2])
                            .map(|x| x.clone())
                            .collect()
                {
                    wordlist[5] = letters.clone();
                }
            }
        }

        for word in &line[..=10] {
            let mut letters: HashSet<char> = HashSet::new();
            for letter in word.chars() {
                letters.insert(letter);
            }

            if !wordlist.contains(&letters) {
                // Last 5 is 3
                if letters.len() == 5 {
                    wordlist[3] = letters.clone();
                }

                if letters.len() == 6 {
                    // If letters and 4 are 8, it's 0, otherwise it's 9

                    if wordlist[8]
                        == letters
                            .clone()
                            .union(&wordlist[4])
                            .map(|x| x.clone())
                            .collect()
                    {
                        wordlist[0] = letters.clone();
                    } else {
                        wordlist[9] = letters.clone();
                    }
                }
            }
        }

        for word in &line[..=9] {
            let mut letters: HashSet<char> = HashSet::new();
            for letter in word.chars() {
                letters.insert(letter);
            }

            if !wordlist.contains(&letters) {
                wordlist[0] = letters.clone();
            }
        }
        let mut temp = 0;

        for (i, word) in line[11..].iter().enumerate() {
            let mut letters: HashSet<char> = HashSet::new();
            for letter in word.chars() {
                letters.insert(letter);
            }
            let num = wordlist.iter().position(|x| x.clone() == letters).unwrap();

            temp += num * vec![1000, 100, 10, 1][i];
        }
        dbg!(temp);
        count += temp;

        // dbg!(wordlist);
    }
    count as i32
}
