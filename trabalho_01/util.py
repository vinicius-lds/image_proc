import os
import re


def fetch_input(path=['.']):
    input_data = []
    input_sizes = []
    for (_, _, files) in os.walk(os.path.join(path)):
        for filename in files:
            if not filename.endswith('.py'):
                with open(os.path.join(path, filename)) as f:
                    content = f.read()
                    content = content.split('\n')
                    curr_input = None
                    input_start_pattern = re.compile('[0-9]+')
                    input_line_pattern = re.compile('[0-9]+\s[0-9]+')
                    for line in content:
                        if not line:
                            continue
                        elif input_line_pattern.match(line):
                            arr = line.split(' ')
                            x, y = int(arr[0]), int(arr[1])
                            curr_input.append((x, y))
                        elif input_start_pattern.match(line):
                            if curr_input != None:
                                input_data.append(curr_input)
                            curr_input = []
                            input_sizes.append(int(line))
                        else:
                            raise Exception('Error parsing input')
                    input_data.append(curr_input)
    if len(input_data) != len(input_sizes):
        raise Exception('Error parsing input')
    for i in range(len(input_data)):
        if len(input_data[i]) != input_sizes[i]:
            raise Exception('Error parsing input')
        if 0 > input_sizes[i] < 3:
            raise Exception('Error parsing input')
        if input_sizes[i] == 0 and len(input_sizes) - 1 != i:
            raise Exception('Error parsing input')
    if input_sizes[-1] == 0:
        del input_data[-1]
    return input_data
