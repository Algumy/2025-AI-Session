def multiplies_of_3_and_5(n):
    return sum(i for i in range(n) if i % 3 == 0 or i % 5 == 0)

print(multiplies_of_3_and_5(1000))