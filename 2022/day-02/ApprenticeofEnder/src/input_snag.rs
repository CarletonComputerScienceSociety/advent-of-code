use reqwest::blocking::{Response, Client};
use reqwest::header::{HeaderMap,HeaderValue, COOKIE};
use std::env;

pub fn get_input(day: u8) -> Result<String, Box<dyn std::error::Error>>{
    let args: Vec<String> = env::args().collect();

    let session_key: &String = &args[1];

    let url: String = format!("https://adventofcode.com/2022/day/{}/input", day);
    let mut headers: HeaderMap = HeaderMap::new();
    let session_cookie: String = format!("session={}", session_key);
    headers.insert(COOKIE, HeaderValue::from_str(session_cookie.as_str()).unwrap());
    let http_client: Client = Client::builder().default_headers(headers).build()?;
    let puzzle_res: Response = http_client.get(url).send()?;
    let puzzle_input: String = puzzle_res.text()?;
    Ok(puzzle_input)
}