#!/usr/bin/python

import os

def main():

    input = map(lambda x: x.strip(), open("../advent-2016/12-input.txt").readlines())
    variables = set()

    func_str = ""

    for i, line in enumerate(input):
        parts = line.split()
        map(lambda x: variables.add(x), filter(lambda x: x.isalpha(), parts[1:]))
        if parts[0] == "cpy":
            func_str += "    line{lineno}: {var} = {val};\n".format(lineno=i, var=parts[2], val=parts[1])
        if parts[0] == "inc":
            func_str += "    line{lineno}: {var}++;\n".format(lineno=i, var=parts[1])
        if parts[0] == "dec":
            func_str += "    line{lineno}: {var}--;\n".format(lineno=i, var=parts[1])
        if parts[0] == "jnz":
            func_str += "    line{lineno}: if( {var} != 0 ) goto line{branch};\n".format(lineno=i, var=parts[1], branch=(i + int(parts[2])))

    fd = open("12-tmp.c", "w")
    fd.write("#include <stdio.h>\n\nint answer(int initc) {\n");
    fd.write("    int " + ", ".join(map(lambda x: "c = initc" if x == "c" else x + " = 0", variables)) + ";\n\n")
    fd.write(func_str);
    fd.write("    return a;\n");
    fd.write('}\n\nint main() {\n    printf("Answer 1: %d\\n", answer(0));\n    printf("Answer 2: %d\\n", answer(1));\n}\n');
    fd.close()

    os.system("cc 12-tmp.c && ./a.out")

if __name__ == "__main__":
    main()
