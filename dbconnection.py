
import sqlite3


# Function to create the database and tables
def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('DRAW RTStruct Export.sqlite')

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Create Study table with foreign key reference
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS FileTransfer(
            id INTEGER PRIMARY KEY,
            PatientUID INTEGER,
            PatientNmame TEXT NOT NULL,
            SOPInstanceUID TEXT,
            SourcePath TEXT,
            StudyDate DATE,
            ModifiedFileName TEXT,
            DestinationPath TEXT,
            ExportDate DATE
        )
    ''')

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# create_database()


def insert_data(patient_uid, patient_name, sop_instance_uid, source_path, study_date, modified_file_name, destination_path, export_date):
    conn = sqlite3.connect('DRAW RTStruct Export.sqlite')
    cursor = conn.cursor()
    # SQL query to insert data into the table
    insert_query = '''
        INSERT INTO FileTransfer (PatientUID, PatientNmame, SOPInstanceUID, SourcePath, StudyDate, ModifiedFileName, DestinationPath, ExportDate)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    '''
    # Data to insert
    data_to_insert = (patient_uid, patient_name, sop_instance_uid, source_path, study_date, modified_file_name, destination_path, export_date)

    # Execute the query with the data
    cursor.execute(insert_query, data_to_insert)
    conn.commit()
    conn.close()


# Example usage
# Assuming you have a SQLite connection and cursor already established
# conn = sqlite3.connect('your_database.db')
# cursor = conn.cursor()

# Example data
# patient_uid = 123
# patient_name = "John Doe"
# sop_instance_uid = "12345"
# source_path = "/path/to/source"
# modified_date = "2024-03-27"
# modified_file_name = "file.txt"
# destination_path = "/path/to/destination"
# export_date = "2024-03-27"

# # Call the function to insert data
# insert_data(patient_uid, patient_name, sop_instance_uid, source_path, modified_date, modified_file_name, destination_path, export_date)

# Commit the transaction if using SQLite
# conn.commit()

# Close the connection if needed
# conn.close()


create_database()