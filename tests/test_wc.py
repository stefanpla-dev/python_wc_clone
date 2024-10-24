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