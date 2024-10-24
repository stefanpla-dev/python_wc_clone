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
    output=[]

    #Handle -c flag for byte count.
    if args.c:
        if not file_input:
            print('Error: You must provide a file path when using the -c option.')
            sys.exit(1)
        byte_count=count_bytes(file_input)
        output.append(f'{byte_count}')

    #Handle -l flag for line count.
    if args.l:
        if not file_input:
            print('Error: You must provide a file path when using the -l option.')
            sys.exit(1)
        line_count=count_lines(file_input)
        output.append(f'{line_count}')

    #Add file name to the output.
    output.append(args.file)
    #Print result.
    print(' '.join(output))

if __name__=='__main__':
    main()
# Checks whether script is being run as the main program, not when imported as a module elsewhere.