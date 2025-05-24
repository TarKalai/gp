def fibonacci_recursive(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main() -> None:
    result = fibonacci_recursive(13)
    print("Hello from gp!: ", result)


if __name__ == "__main__":
    main()
