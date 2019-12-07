from interpreter import interpreter

with open('program.txt', 'r') as file:
    # Read input program
    program = list(map(int, file.readline().strip().split(",")))
    target = 19690720

    for noon in range(0, 100):
        for verb in range(0, 100):
            program_tmp = program.copy()

            program_tmp[1] = noon
            program_tmp[2] = verb

            if(interpreter(program_tmp)[0] == target):
                print(100*noon + verb)
                exit()