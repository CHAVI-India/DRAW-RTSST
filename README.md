
# DRAW RTSST

DRAW RTSST is a tool designed for managing and transferring auto-segmented predicted RTStructure DICOM files. It operates based on a schedule, scanning a specified root folder (PredRT Output) for DICOM files, identifying RTSTRUCT files, and copying them to a designated remote folder while applying specific naming conventions (DRAW_{HospitalID}_{Sop}.dcm). Additionally, it logs various operations performed during the process and saves important information in a .sqlite database.
## Features

- **DICOM File Parsing**: Utilizes the `pydicom` library to extract relevant metadata from DICOM files.
- **Logging**: Utilizes the `loguru` library for logging operations, providing insights into file management actions and potential errors.
- **Remote Transfer**: Copies identified RTSTRUCT files to a remote folder, ensuring efficient data transfer.
- **Data Integrity**: Maintaining a mechanisms to avoid duplication of files and maintains data integrity during transfer.
- **SQLite Database Integration**: Utilizes SQLite database for storing information about file transfers, facilitating tracking and management.

## Setup and Configuration

1. **Dependencies**: Ensure you have the necessary Python libraries installed. You can install them using `pip`:

    ```bash
    pip install pydicom loguru
    ```

2. **Database Setup**: The script uses an SQLite database to store information about file transfers. Ensure you have SQLite installed and execute the `create_database` function from `dbconnection.py` to create the necessary tables. Update database connection parameters as needed.

3. **Configuration**: Customize the configuration parameters in the script according to your environment. Modify `root_path` to point to the root folder containing DICOM files and `remote_folder` to specify the destination folder for remote transfer.


## Usage

Run the script `find_pred_rt_files.py` with appropriate permissions and ensure the necessary access permissions for reading from the root folder and writing to the remote folder. The script will automatically scan the specified root folder, identify RTSTRUCT files, and transfer them to the remote folder while maintaining data integrity.

```bash
python run.py
```

## Schedule-Based Operation

To enable schedule-based operation, you can integrate the script with task scheduling tools available for your operating system. For example, on Unix-like systems, you can use cron jobs to schedule the script to run at specific intervals.

## Logging

Log files are generated daily in the `logs` directory, with filenames following the format `YYYY-MM-DD.log`. Log entries include timestamps, log levels (DEBUG, INFO, WARNING, ERROR), and messages detailing file management operations and any encountered issues.

## Database

The SQLite database `DRAW RTStruct Export.sqlite` stores information about file transfers. The database consists of the following fields in the `FileTransfer` table:

- `id` (INTEGER, PRIMARY KEY): Unique identifier for each record.
- `PatientUID` (INTEGER): Patient's unique identifier.
- `PatientName` (TEXT, NOT NULL): Patient's name.
- `SOPInstanceUID` (TEXT): SOP Instance UID of the DICOM file.
- `SourcePath` (TEXT): Path of the source DICOM file.
- `StudyDate` (DATE): Date of the study.
- `ModifiedFileName` (TEXT): Name of the file after modification.
- `DestinationPath` (TEXT): Path of the destination folder.
- `ExportDate` (DATE): Date of export.

## Contributing

Contributions to enhance the functionality, improve performance, or fix issues are welcome. Please fork the repository, make your changes, and submit a pull request.
