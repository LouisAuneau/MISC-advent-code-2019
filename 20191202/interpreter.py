from typing import List

def interpreter(program: List[int]) -> List[int]:
    for i in range(0, len(program), 4):
        opcode = program[i]

        if opcode == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
        elif opcode == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
        elif opcode == 99:
            return program
        else:
            raise ValueError(f"Unknown opcode {opcode} at position {i}.")