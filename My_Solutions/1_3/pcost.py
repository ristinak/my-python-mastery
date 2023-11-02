sum = 0
with open("Data/portfolio.dat", "r") as f:
    for line in f:
        elements = line.split()
        sum += int(elements[1]) * float(elements[2])
print(sum)