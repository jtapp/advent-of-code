use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    // plus 1 for the path of this file
    if args.len() != 2 + 1 {
        println!("Usage: provide a day and part as arguments. Like `cargo run -- 3 a`");
        return;
    }
    let day: u32 = args[1]
        .parse()
        .expect("Please provide an integer Day to run");
    let part: char = args[2].parse().expect("Please specify a part 'a' or 'b'");
    dbg!(day);
    dbg!(part);
}
