fn main() {
    println!("Hello, world!");

    let mut number = 1;

    while number != 4 {
        println!("{}", number);
        number += 1;
    }

    println!("Exit");


    let mut i = 0;

    while i < 10 {
        i += 1;
    }

    let a = [10, 20, 30, 40, 50];
    for i in a.iter() {
        println!("i={}", i);
    }

    let s = ['R','U','N','O','O','B'];
    let mut i = 0;

    loop {
        let ch = s[i];
        if ch == 'O' {
            break;
        }

        println!("\'{}\'", ch);
        i += 1;
    }

    i = 0;

    let location = loop {
        let ch = s[i];
        if ch == 'O' {
            break i;
        }
        i += 1;
    };

    println!("\'O\' is index is {}", location);
}
