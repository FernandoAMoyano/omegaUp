def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    p = int(input())

    if p == 0:
        result = [str(num) for num in numbers if num % 2 == 0]
    else:
        result = [str(num) for num in numbers if num % 2 != 0]

    print(" ".join(result))


if __name__ == "__main__":
    main()
