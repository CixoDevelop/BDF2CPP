import sys

def csv_to_array(csv_data):
    """
    This function converting csv formatted string to python array. Array store
    nested arrays, or string when csv store comment.
    :csv_data: String in CSV format
    :return: C array string
    """

    data = list()
    
    for line in csv_data.split("\n"):
        if len(line.strip()) == 0:
            continue

        if line.strip()[0] == "#":  
            data.append(line)
            continue

        data.append(list())
        for part in line.split(","):
            if part != '':
                data[-1].append(part)

    return data


def get_array_size(data):
    """
    This function return array size. This calc len of array elements, that is 
    not comments (not string), and maximum length of nested array.
    :data: Array to calc
    :return: Calculated length of lines and rows (return lines, rows)
    """

    lines = 0
    rows = 0

    for line in data:
        if isinstance(line, str):
            continue
        
        lines += 1

        if rows < len(line):
            rows = len(line)

    return lines, rows


def convert_to_c(csv_data):
    """
    This function convert csv formated string into c array string.
    :csv_data: Csv string
    :return: C array string
    """

    data = csv_to_array(csv_data)
    lines, rows = get_array_size(data)
    c_code = "bool csv_content"
    c_code += "[" + str(lines) + "][" + str(rows) + "]" + " = {\n"

    for line in data:
        if isinstance(line, str):
            c_code += "\t//" + line[1:] + "\n"
            continue

        c_code += "\t{"
        
        for part in line:
            c_code += part + ", "
        
        c_code = c_code[:-2] + "},\n"
    
    return c_code[:-2] + "\n};"


def main():
    """
    This function get params from command line, and printing converted data, 
    or help text.
    """

    if len(sys.argv) <= 1:
        print("Run csv2cpp.py [csv filename] > [cpp filename]")
        exit(0)
    
    filename = sys.argv[1]

    with open(filename) as file:
        print(convert_to_c(file.read()))


if __name__ == "__main__":
    main()
