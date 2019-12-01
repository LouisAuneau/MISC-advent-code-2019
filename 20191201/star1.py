import math

with open('masses.txt') as masses:
    print(sum(list(map(lambda x : math.floor(int(x)/3) - 2, masses.readlines()))))