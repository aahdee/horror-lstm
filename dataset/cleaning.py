#cleaning the inputs, adapted from processing community day's code

cleaned_lines = []

for line in open('source_input.txt', 'r'):
    line = line.splitlines()[0].strip()

    #remove the headers and empty lines
    result1 = line.find('HEADER,')
    result2 = line.find('Chapter')
    if ((result1 == -1) and (result2 == -1) and not line == ''):
        line = line + '\n'
        cleaned_lines.append(line)

with open('../info/input.txt', 'w') as file:
    for line in cleaned_lines:
        file.write(line)
