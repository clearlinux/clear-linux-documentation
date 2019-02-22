'''
Usage: python code-blocks.py path/to/file.rst

Default output is to stdout

Parses bash code blocks out of rst file for instruction testing.
'''
import sys

def code_blocks(filename):
    with open(filename, 'r') as fd:
        c_indent = ''
        in_section = []
        for line in fd:
            indent = line[:len(line) - len(line.lstrip())]
            if 'code-block:: bash' in line:
                in_section = [line.strip()]
                c_indent = ''
            elif in_section:
                if not c_indent and line.strip():
                    c_indent = indent
                if not (len(indent) >= len(c_indent)) and line.strip():
                    yield in_section[2:]
                    in_section = []
                else:
                    in_section.append(line[len(c_indent):].rstrip())

def main():
    for code_block in code_blocks(sys.argv[1]):
        print('\n'.join(code_block) + '\n')

if __name__ == '__main__':
    main()
