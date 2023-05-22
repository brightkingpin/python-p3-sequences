#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_seq = []
    a, b = 0, 1

    for _ in range(length):
        fibonacci_seq.append(a)
        a, b = b, a + b

    print(fibonacci_seq)
