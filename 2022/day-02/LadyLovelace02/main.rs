use std::fs::File;
use std::io::{BuffRead, BuffReader};

fn calcScore(pIn: char, oIn: char) -> i32 {
    let mut score = 0;
    //repersent the options numerically, each beats the one to the left wrapping around
    //rock:1, paper:2, scissors:3
    let opponent = (oIn as u32) - 64;
    let player = (pIn as u32) - 87;
    score += player;
    if player == opponent {
        score += 3//draw
    }
    else if player-1 == opponent {
        score += 6;//win
    }
    else if player+2 == opponent {
        score += 6;//win
        //happens when rock beats scissors
    }
    return score;
}

fn calcScore2(outcome: char, oIn: char) -> i32 {
    let mut score = 0;
    //repersent the options numerically, each beats the one to the left wrapping around
    //rock:1, paper:2, scissors:3
    let opponent = (oIn as u32) - 64;
    let outcome = (outcome as u32) - 87;
    if (outcome == 1) {
        //loose
        let player = opponent-1;
        if (player == 0) {
            player = 3;
        }
    }
    else if (outcome == 2) {
        //draw
        score += 3;
        let player = opponent;
    }
    else {
        //win
        score += 6;
        player = opponent+1;
        if (player == 4) {
            player = 1;
        }
    }
    score += player;
    return score;
}

fn part1() -> i32 {
    let file = File::open("input.txt").expect("error opening file");
    let reader = BufReader::new(file);
    let totalScore:i32 = 0;
    //read line by line
    for (line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let oIn = line[0];
        let pIn = line[2];
        totalScore += calcScore(pIn, oIn);
    }
    return totalScore;
}

fn part2() -> i32 {
    let file = File::open("input.txt").expect("error opening file");
    let reader = BufReader::new(file);
    let totalScore:i32 = 0;
    //read line by line
    for (line) in reader.lines().enumerate() {
        let line = line.unwrap();
        let oIn = line[0];
        let outcome = line[2];
        totalScore += calcScore2(outcome, oIn);
    }
    return totalScore;
}

fn main() {
    println("{}", part1());
    println("{}", part2());
}
