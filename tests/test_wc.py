import subprocess
import tempfile
import os

#Idea - test to validate flag order in output matches input? Come back to this.

def test_count_bytes():
    '''Test the -c option (byte count).'''
    #Create a temporary file with specific content.
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Hello, World!')
        temp_file_name = temp_file.name

    #Run the wc.py script with the -c option and the temporary file.
    result=subprocess.run(['python', 'src/wc.py', '-c', temp_file_name], capture_output=True, text=True)

    #Get the output from the script (strip to remove extra spaces/newlines).
    output=result.stdout.strip()

    #Manually calculate the expected byte count.
    expected_byte_count=len(b'Hello, World!')

    #Assert that the output matches the expected format and byte count.
    assert output==f'{expected_byte_count} {temp_file_name}'

    #Clean up the temporary file.
    os.remove(temp_file_name)

def test_count_lines():
    '''Test the -l option (line count).'''
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write('Hello\nWorld\nPython\n')
        temp_file_name=temp_file.name
    
    result=subprocess.run(['python', 'src/wc.py', '-l', temp_file_name], capture_output=True, text=True)

    output=result.stdout.strip()

    expected_line_count=3

    assert output==f'{expected_line_count} {temp_file_name}'

    os.remove(temp_file_name)

def test_count_words():
    '''Test the -w option (word count).'''
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write('Hello world\nThis is a test\nPython is the best.')
        temp_file_name=temp_file.name
    
    result=subprocess.run(['python', 'src/wc.py', '-w', temp_file_name], capture_output=True, text=True)

    output=result.stdout.strip()
    expected_word_count=10

    assert output==f'{expected_word_count} {temp_file_name}'

    os.remove(temp_file_name)

def test_count_characters():
    '''Test the -m option (character count).'''
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write('Hello world.\nThis is a test of character counting.')
        temp_file_name=temp_file.name

    result=subprocess.run(['python', 'src/wc.py', '-m', temp_file_name], capture_output=True, text=True)

    output=result.stdout.strip()
    expected_character_count=50

    assert output==f'{expected_character_count} {temp_file_name}'

    os.remove(temp_file_name)

def test_default_flag_behavior():
    '''Test the default flag behavior (-c, -l, -w printed to the command line.)'''
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        temp_file.write('Hello world.\nThis is a test of flag behavior.')
        temp_file_name=temp_file.name
    
    result=subprocess.run(['python', 'src/wc.py', temp_file_name], capture_output=True, text=True)

    output=result.stdout.strip()
    expected_byte_count=len('Hello world.\nThis is a test of flag behavior.')
    expected_line_count=2
    expected_word_count=9

    assert output==f'{expected_byte_count} {expected_line_count} {expected_word_count} {temp_file_name}'

    os.remove(temp_file_name)