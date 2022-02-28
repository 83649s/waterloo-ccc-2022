import string

instructions = str(input())
formated_instructions = []

for i in range(len(instructions)):
    instruction = ''
    for j in string.ascii_uppercase:
        if instructions[i] == j:
            instruction += instructions[i]

    if instructions[i] == '+':
        instruction += ' tighten '
    elif instructions[i] == '-':
        instruction += ' loosen '
    
    for j in string.digits:
        if instructions[i] == j:
            instruction += j
    
    formated_instructions.append(instruction)

formated_buffer = ''
i = 0
while i < len(formated_instructions) - 1:
    for j in string.digits:
        for k in string.ascii_uppercase:
            if formated_instructions[i] == j and formated_instructions[i + 1] == k:
                formated_buffer += formated_instructions[i]
                formated_buffer += '\n'
                i += 1
                break
    formated_buffer += formated_instructions[i]
    i += 1

formated_buffer += formated_instructions[-1]
print(formated_buffer)