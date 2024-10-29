import sqlite3
from datetime import datetime

DATABASE_NAME = 'file_processing_log.db'

def connect_to_db():
    '''Establishes a connection to the SQLite database and creates the table if it doesn't exist'''
    conn=sqlite3.connect(DATABASE_NAME)
    create_table_query='''
    CREATE TABLE IF NOT EXISTS FileProcessingLog(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_path TEXT NOT NULL,
        processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        file_size INTEGER,
        execution_duration REAL,
        line_count INTEGER,
        word_count INTEGER,
        character_count INTEGER,
        byte_count INTEGER
    );
    '''
    conn.execute(create_table_query)
    conn.commit()
    return conn

def log_file_processing(file_path, file_size, line_count, word_count, character_count, byte_count, execution_duration):
    '''Inserts a new record into the FileProcessingLog table.'''
    conn=connect_to_db()
    insert_query='''
    INSERT INTO FileProcessingLog (file_path, file_size, line_count, word_count, character_count, byte_count, execution_duration)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    '''
    conn.execute(insert_query, (file_path, file_size, line_count, word_count, character_count, byte_count, execution_duration))
    conn.commit()
    conn.close()

def fetch_all_logs():
    '''Fetches all logs from the FileProcessingLog table.'''
    conn=connect_to_db()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM FileProcessingLog')
    rows=cursor.fetchall()
    conn.close()
    return rows
