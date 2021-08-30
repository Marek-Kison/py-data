import statistics

data = [1.3, 2.7, 0.8, 4.1, 5.2]

average = statistics.mean(data)

filter_fun = filter(lambda x: x > average, data)


if __name__ == '__main__':
    print(f"average is :", average)
    print(filter_fun)
    print("change to list")
    print(list(filter_fun))
