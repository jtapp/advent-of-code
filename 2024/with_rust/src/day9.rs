pub fn day9a(lines: Vec<String>) {
    let mut is_file: bool = true;
    let mut total: u64 = 0;
    let mut file_id: u64 = 0;
    let mut end_file_id: u64 = 0; // TODO
    for (i, c) in lines[0].chars().enumerate() {
        // TODO end early when end_file_id == file_id or smthing
        let big_i = i as u64;
        let size = c.to_digit(10).expect("Not a digit");
        for _ in 0..size {
            if is_file {
                total += big_i * file_id;
            } else {
                total += big_i * end_file_id;
                end_file_id = 0; // TODO
            }
        }
        if !is_file {
            file_id += 1
        }
        is_file = !is_file;
    }
    dbg!(total);
}
