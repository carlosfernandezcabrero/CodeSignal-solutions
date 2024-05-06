fn solution(L: i32, R: i32) -> i32 {
    let mut comfortable_numbers: i32 = 0;

    for i in L..R + 1 {
        let soa_i = soa(i);

        for j in i + 1..R + 1 {
            let soa_j = soa(j);

            if j >= i - soa_i && j <= i + soa_i && i >= j - soa_j && i <= j + soa_j {
                comfortable_numbers += 1;
            }
            if j > i + soa_i {
                break;
            }
        }
    }

    comfortable_numbers
}

fn soa(number: i32) -> i32 {
    let mut sum: i32 = 0;

    for c in number.to_string().chars() {
        sum += c.to_digit(10).unwrap() as i32;
    }

    sum
}
