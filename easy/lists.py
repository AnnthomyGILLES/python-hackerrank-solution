class IllegalArgumentError(ValueError):
    pass


def get_instruction(instructions, list_to_modify):
    if len(instructions) > 3:
        raise IllegalArgumentError("Too much arguments")

    if len(instructions) == 1:
        if 'pop' in instructions:
            list_to_modify.pop()
        elif 'print' in instructions:
            print(list_to_modify)
        elif 'sort' in instructions:
            list_to_modify.sort()
        elif 'reverse' in instructions:
            list_to_modify.reverse()

    if len(instructions) == 2:
        if 'remove' in instructions:
            list_to_modify.remove(int(instructions[1]))
        elif 'append' in instructions:
            list_to_modify.append(int(instructions[1]))

    if len(instructions) == 3:
        if 'insert' in instructions:
            list_to_modify.insert(int(instructions[1]), int(instructions[2]))
            
if __name__ == '__main__':
    liste = list()
    N = int(input())
    instructions = [ [x for x in input().split()] for item in range(N)]
    for instruction in instructions:
        get_instruction(instruction, liste)
