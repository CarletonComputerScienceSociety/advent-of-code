fn main() {
    println!("Pt. 1: {}", vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        .windows(2)
        .filter(|x| x[0] < x[1])
        .count());

    println!("Pt. 2: {}", vec![199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        .windows(3)
        .map(|x| x.iter().sum())
        .collect::<Vec<i32>>()
        .windows(2)
        .filter(|x| x[0] < x[1])
        .count());
}
