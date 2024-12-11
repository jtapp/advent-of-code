use std::collections::HashMap;

pub fn day8b(lines: Vec<String>) {
    let width = lines.len() as i16;
    let height = lines[0].len() as i16;
    let mut ants = HashMap::new();
    for (x, line) in lines.iter().enumerate() {
        for (y, c) in line.as_bytes().iter().enumerate() {
            if *c != b'.' {
                let locations: &mut Vec<(i16, i16)> = ants.entry(*c).or_insert(Vec::new());
                locations.push((x as i16, y as i16))
            }
        }
    }
    // dbg!(ants);
    let mut antinodes = HashMap::new();
    for (c, locs) in ants {
        for (i, (x1, y1)) in locs.iter().enumerate() {
            for (x2, y2) in &locs[i..] {
                let dx = (x2 - x1) as i16;
                let dy = (y2 - y1) as i16;
                if dx == 0 && dy == 0 {
                    continue;
                }
                let mut xa1 = *x1 as i16;
                let mut ya1 = *y1 as i16;
                while 0 <= xa1 && xa1 < width && 0 <= ya1 && ya1 < height {
                    let antinodes_here: &mut Vec<u8> =
                        antinodes.entry((xa1, ya1)).or_insert(Vec::new());
                    antinodes_here.push(c);
                    xa1 -= dx;
                    ya1 -= dy;
                }
                let mut xa2 = *x2 as i16;
                let mut ya2 = *y2 as i16;
                while 0 <= xa2 && xa2 < width && 0 <= ya2 && ya2 < height {
                    let antinodes_here: &mut Vec<u8> =
                        antinodes.entry((xa2, ya2)).or_insert(Vec::new());
                    antinodes_here.push(c);
                    xa2 += dx;
                    ya2 += dy;
                }
            }
        }
    }
    // dbg!(&antinodes);
    dbg!(antinodes.len());
}
