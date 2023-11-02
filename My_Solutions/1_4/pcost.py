def portfolio_cost(filename: str) -> float:
    total_cost = 0.0
    with open(filename, "r") as f:
        for line in f:
            elements = line.split()
            try:
                amount = int(elements[1])
                cost = float(elements[2])
                total_cost += amount * cost
            except ValueError as e:
                print(f"Couldn't parse {line}Reason: {e}")
    return total_cost


print(portfolio_cost("Data/portfolio3.dat"))
