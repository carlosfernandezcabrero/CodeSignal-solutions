fn solution(n: i32) -> Vec<i32> {
    fn get_weakness(n: i32) -> i32 {
        (1..=n).filter(|&i| n % i == 0).count() as i32
    }

    let mut max_weakness = 0;
    let mut num_max_weakness = 0;

    let mut weaknesses = std::collections::HashMap::new();
    for i in 1..=n {
        weaknesses.insert(i, get_weakness(i));
    }

    for i in (1..=n).rev() {
        if i - 1 < max_weakness {
            break;
        }

        let weakness = weaknesses[&i];
        let mut weakness_count = 0;

        for (&k, &v) in weaknesses.iter() {
            if k < i && v > weakness {
                weakness_count += 1;
            }
        }

        if weakness_count > max_weakness {
            max_weakness = weakness_count;
            num_max_weakness = 1;
        } else if weakness_count == max_weakness {
            num_max_weakness += 1;
        }
    }

    [max_weakness, num_max_weakness].to_vec()
}
