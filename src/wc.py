import argparse
import sys
import os

def count_bytes(file_path):
    '''Counts the number of bytes in a given file.'''
    try:
        with open(file_path, 'rb') as file: #Open in binary mode to count bytes accurately.
            byte_content = file.read()
            return len(byte_content)
    except FileNotFoundError:
        print(f'python_wc_clone: {file_path}: No such file or directory.')
        sys.exit(1)

def count_lines(file_path):
    '''Counts the number of lines in the given file.'''
    try:
        with open(file_path, 'r') as file: #Open in text mode to count lines.
            return sum(1 for line in file)
    except FileNotFoundError:
        print(f'python_wc_clone: {file_path}: No such file or directory.')
        sys.exit(1)

def main():
    #Argument parser setup.
    parser = argparse.ArgumentParser(description = 'python_wc_clone: word, line, character, and byte count.')
    parser.add_argument('-c', action='store_true', help='Count and print the number of bytes in a file.')
    parser.add_argument('-l', action='store_true', help='Count and print the number of lines in a file.')
    parser.add_argument('file', nargs='?', help='Path to the file to process.')

    #Parse the arguments.
    args=parser.parse_args()
    file_input=args.file
    #Initialize empty output.
    output=[]

    #Capture the order of arguments by using the command-line args directly.
    flags_in_order=sys.argv[1:-1]

    if not file_input:
        print('Error: You must provide a file path.')
        sys.exit(1)
    
    #Process the arguments in the order provided by the user.
    for flag in flags_in_order:
        if flag=='-c':
            byte_count=count_bytes(file_input)
            output.append(f'{byte_count}')
        elif flag=='-l':
            line_count=count_lines(file_input)
            output.append(f'{line_count}')
    
    #Append the filename to the output.
    output.append(file_input)

    #Print result.
    print(' '.join(output))

if __name__=='__main__':
    main()
# Checks whether script is being run as the main program, not when imported as a module elsewhere.