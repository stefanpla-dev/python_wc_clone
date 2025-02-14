import argparse
import sys
import os
from db import log_file_processing
import time

def count_bytes(file_path, from_stdin=False):
    '''Counts the number of bytes in a given file.'''
    if from_stdin:
        return len(file_path.encode('utf-8'))
    else:
        try:
            with open(file_path, 'rb') as file: #Open in binary mode to count bytes accurately.
                byte_content = file.read()
                return len(byte_content)
        except FileNotFoundError:
            print(f'python_wc_clone: {file_path}: No such file or directory.')
            sys.exit(1)

def count_lines(file_path, from_stdin=False):
    '''Counts the number of lines in the given file.'''
    if from_stdin:
        return sum(1 for line in file_path.splitlines())
    else:
        try:
            with open(file_path, 'r', encoding='utf-8') as file: #Open in text mode to count lines.
                return sum(1 for line in file) #Process line by line instead of loading the entire file into memory at once. 
        except FileNotFoundError:
            print(f'python_wc_clone: {file_path}: No such file or directory.')
            sys.exit(1)

def count_words(file_path, from_stdin=False):
    '''Counts the number of words in the given file.'''
    if from_stdin:
        return sum(len(line.split()) for line in file_path.splitlines())
    else:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return sum(len(line.split()) for line in file) 
        except FileNotFoundError:
            print(f'python_wc_clone: {file_path}: No such file or directory.')
            sys.exit(1)

def count_characters(file_path, from_stdin=False):
    '''Count the number of characters in the given file.'''
    if from_stdin:
        return sum(len(line) for line in file_path.splitlines())
    else:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return sum(len(line) for line in file)
        except FileNotFoundError:
            print(f'python_wc_clone: {file_path}: No such file or directory.')
            sys.exit(1)

def main():
    #Argument parser setup.
    parser = argparse.ArgumentParser(description = 'python_wc_clone: word, line, character, and byte count.')
    parser.add_argument('-c', action='store_true', help='Count and print the number of bytes in a file.')
    parser.add_argument('-l', action='store_true', help='Count and print the number of lines in a file.')
    parser.add_argument('-w', action='store_true', help='Count and print the number of words in a file.')
    parser.add_argument('-m', action='store_true', help='Count and print the number of characters in a file.')
    parser.add_argument('file', nargs='?', help='Path to the file to process.')

    #Parse the arguments.
    args=parser.parse_args()
    
    if not args.file:
        file_input=sys.stdin.read()
    else:
        file_input=args.file
    
    #Capture the flag order based on user input.
    flags_in_order=[arg for arg in sys.argv[1:-1] if arg in ['-c', '-l', '-w', '-m']]

    #If no flags are provided, set default flags to -c, -l, -w.
    if not flags_in_order:
        flags_in_order=['-c', '-l', '-w']

    # Track strat time to measure execution duration.
    start_time = time.time()
    
    #Initialize empty output.
    output=[]

    #Process the arguments in the order provided by the user.
    for flag in flags_in_order:
        if flag=='-c':
            byte_count=count_bytes(file_input, from_stdin=(not args.file))
            output.append(f'{byte_count}')
        elif flag=='-l':
            line_count=count_lines(file_input, from_stdin=(not args.file))
            output.append(f'{line_count}')
        elif flag=='-w': 
            word_count=count_words(file_input, from_stdin=(not args.file))
            output.append(f'{word_count}')
        elif flag=='-m':
            character_count=count_characters(file_input, from_stdin=(not args.file))
            output.append(f'{character_count}')

    #Calculate the execution duration.
    execution_duration=time.time() - start_time

    #Insert the log entry into the database.
    log_file_processing(
        file_path=(file_input if args.file else '(stdin)'),
        file_size=len(file_input) if not args.file else os.path.getsize(file_input),
        line_count=line_count if 'line_count' in locals() else None,
        word_count=word_count if 'word_count' in locals() else None,
        character_count=character_count if 'character_count' in locals() else None,
        byte_count=byte_count if 'byte_count' in locals() else None,
        execution_duration=execution_duration,
    )
    
    #Append the filename to the output.
    output.append('(stdin)' if not args.file else args.file)

    #Print result.
    print(' '.join(output))

# Check whether script is being run as the main program, not when imported as a module elsewhere.
if __name__=='__main__':
    main()