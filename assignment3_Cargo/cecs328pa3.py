# Rianne Papa

def aircraft_max_revenue(cargo, capacity):
    cargo_length = len(cargo)
    c = [[0 for i in range(capacity+1)] for j in range(cargo_length+1)]
    
    for i in range(1,cargo_length+1):
        for j in range(capacity+1):
            weight, value = cargo[i-1]
            if weight <= j:
                c[i][j] = max(c[i-1][j],value + c[i-1][j-weight])
            else:
                c[i][j] = c[i-1][j]

    return c[cargo_length][capacity]

def main():
    print()
main()