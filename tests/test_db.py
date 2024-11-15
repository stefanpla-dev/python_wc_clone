import sqlite3 
import pytest
from src.db import log_file_processing, fetch_all_logs

def text_log_file_processing():
    # Clear previous test data.
    conn=sqlite3.connect('file_processing_log.db')
    conn.execute('DELETE FROM FileProcessingLog')
    conn.commit()
    conn.close()

    #Log a test file processing event
    log_file_processing(
        file_path='text_file.txt',
        file_size=100,
        line_count=10,
        word_count=20,
        character_count=50,
        byte_count=100,
        execution_duration=0.5
    )

    #Fetch all logs and verify the test entry.
    logs=fetch_all_logs()
    assert len(logs)==1
    log=log[0]
    assert log[1]=='test_file.txt'
    assert log[2] is not None
    assert log[3]==100
    assert log[4]==10
    assert log[5]==20
    assert log[6]==50
    assert log[7]==100
    assert log[8]==0.5