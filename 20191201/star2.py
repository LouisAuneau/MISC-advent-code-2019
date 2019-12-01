import math

def fuel_needed(mass: int) -> int:
    fuel = math.floor(mass/3) - 2
    return 0 if fuel < 0 else fuel + fuel_needed(fuel)

with open('masses.txt') as masses:
    print(sum(list(map(lambda x : fuel_needed(int(x)), masses.readlines()))))

