import subprocess
import tempfile
import os

def test_count_bytes():
    #Create a temporary file with specific content.
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(b'Hello, World!')
        temp_file_name = temp_file.name

    #Run the wc.py script with the -c option and the temporary file.
    result = subprocess.run(['python', 'src/wc.py', '-c', temp_file_name], capture_output=True, text=True)

    #Get the output from the script (strip to remove extra spaces/newlines).
    output = result.stdout.strip()

    #Manually calculate the expected byte count.
    expected_byte_count = len(b'Hello, World!')

    #Assert that the output matches the expected format and byte count.
    assert output == f'{expected_byte_count} {temp_file_name}'

    #Clean up the temporary file.
    os.remove(temp_file_name)