from functools import reduce


product = 1
moj_list = [1, 2, 3, 4]
for cislo in moj_list:
    product *= cislo

product2 = reduce((lambda x, y: x * y), [1, 2, 3, 4])

if __name__ == "__main__":
    print(product)  # 24
    print(product2)  # 24
