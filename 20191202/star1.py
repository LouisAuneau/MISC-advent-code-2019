from interpreter import interpreter

# Main
with open('program.txt', 'r') as file:
    # Read input program
    program = list(map(int, file.readline().strip().split(",")))

    # Reset the input program
    program[1] = 12
    program[2] = 2

    # Interpreter
    print(interpreter(program)[0])


        
