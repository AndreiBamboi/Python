import sys

def sqrt(x):
    if x < 0:
        raise ValueError(
            "Nu merge bos cu" f"numar negativ {x}"
        )
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess)/ 2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except (ValueError,ZeroDivisionError) as e:
        print(e, file=sys.stderr)


if __name__ == '__main__':
    main()