def fatorial(n: int) -> int:
    if n == 1 or n == 0:
        return 1
    return n * fatorial(n - 1)


if __name__ == "__main__":
    fat = fatorial(int(input('Digite o número para calculo do Fatorial:')))
    print(fat)