use std::collections::{HashMap, HashSet, VecDeque};

#[aoc_generator(day12)]
pub fn input_generator(input: &str) -> HashMap<String, Vec<String>> {
    // hl-WP
    // vl-fo
    // vl-WW
    // WP-start
    // vl-QW
    // fo-wy
    // WW-dz
    // dz-hl
    // fo-end
    // VH-fo
    // ps-vl
    // FN-dz
    // WP-ps
    // ps-start
    // WW-hl
    // end-QW
    // start-vl
    // WP-fo
    // end-FN
    // hl-QW
    // WP-dz
    // QW-fo
    // QW-dz
    // ps-dz

    // This is a list of how all of the caves are connected. You start in the
    // cave named start, and your destination is the cave named end. An entry
    // like b-d means that cave b is connected to cave d - that is, you can move
    // between them.

    // Your goal is to find the number of distinct paths that start at start,
    // end at end, and don't visit small caves more than once. There are two
    // types of caves: big caves (written in uppercase, like A) and small caves
    // (written in lowercase, like b). It would be a waste of time to visit any
    // small cave more than once, but big caves are large enough that it might
    // be worth visiting them multiple times. So, all paths you find should
    // visit small caves at most once, and can visit big caves any number of
    // times.

    let mut return_map: HashMap<String, Vec<String>> = HashMap::new();

    for line in input.lines() {
        let mut path = line.split("-");

        let first = path.next().unwrap();
        let second = path.next().unwrap();

        return_map
            .entry(first.to_string())
            .or_insert(vec![])
            .push(second.to_string());
        return_map
            .entry(second.to_string())
            .or_insert(vec![])
            .push(first.to_string());
    }

    return_map
}

pub fn recursive_seach(
    map: &HashMap<String, Vec<String>>,
    current_pos: &String,
    visited: &mut HashSet<String>,
    // queue: &mut VecDeque<String>,
) -> usize {
    // dbg!(current_pos);
    // dbg!(queue.clone());
    if current_pos == "end" {
        return 1;
    }

    // Check if current room is not upper case and we've already been here

    if current_pos.chars().next().unwrap().is_lowercase() && visited.contains(current_pos) {
        return 0;
    }

    // if visited.contains(current_pos) && !current_pos.chars().any(|c| c.is_uppercase()) {
    //     return 0;
    // }

    // Add current room to visited
    visited.insert(current_pos.to_string());

    let mut queue = VecDeque::new();

    // Add all neighbors to queue
    for neighbor in map.get(current_pos).unwrap().iter() {
        queue.push_back(neighbor.to_string());
    }

    // Recurse on all neighbors
    let mut count = 0;
    while let Some(room) = queue.pop_front() {
        count += recursive_seach(map, &room, &mut visited.clone());
    }

    count
}

#[aoc(day12, part1)]
pub fn solve_part1(input: &HashMap<String, Vec<String>>) -> i32 {
    let mut visited = HashSet::new();
    let mut queue: VecDeque<String> = VecDeque::new();

    // queue.push_back("start".to_string());

    recursive_seach(input, &"start".to_string(), &mut visited.clone()) as i32
}

pub fn recursive_seach_2(
    map: &HashMap<String, Vec<String>>,
    current_pos: &String,
    visited: &mut HashMap<String, i32>,
    // queue: &mut VecDeque<String>,
) -> usize {
    // dbg!(current_pos);
    // dbg!(queue.clone());
    if current_pos == "end" {
        return 1;
    }

    if current_pos == "start" && visited.contains_key(current_pos) {
        return 0;
    }

    // Check if current room is not upper case and we've already been here

    let is_lower_case = current_pos.chars().next().unwrap().is_lowercase();
    let is_in_visited = visited.contains_key(current_pos);
    let are_any_lowercase_greater = visited
        .iter()
        .any(|(k, v)| k.chars().next().unwrap().is_lowercase() && *v > 1);

    if is_lower_case && is_in_visited && are_any_lowercase_greater {
        return 0;
    }

    // Add current room to visited and increment count
    visited.entry(current_pos.to_string()).or_insert(0);
    visited
        .entry(current_pos.to_string())
        .and_modify(|e| *e += 1);

    let mut queue = VecDeque::new();

    // Add all neighbors to queue
    for neighbor in map.get(current_pos).unwrap().iter() {
        queue.push_back(neighbor.to_string());
    }

    // Recurse on all neighbors
    let mut count = 0;
    while let Some(room) = queue.pop_front() {
        count += recursive_seach_2(map, &room, &mut visited.clone());
    }

    count
}

#[aoc(day12, part2)]
pub fn solve_part2(input: &HashMap<String, Vec<String>>) -> i32 {
    let mut visited = HashMap::new();
    let mut queue: VecDeque<String> = VecDeque::new();

    // queue.push_back("start".to_string());

    recursive_seach_2(input, &"start".to_string(), &mut visited.clone()) as i32
}
