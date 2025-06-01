def factorial(n):
    if n < 0:
        return "ფაქტორიალი მხოლოდ არანეგატიური რიცხვებისთვის გამოითვლება"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

factorial(8)
