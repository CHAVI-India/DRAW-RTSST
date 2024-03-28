
import os
import shutil
import pydicom
from loguru import logger
from datetime import datetime



start_of_day = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
log_filename = os.path.join("logs", f"{start_of_day.strftime('%Y-%m-%d')}.log")
# os.makedirs(log_directory, exist_ok=True)  # Create the directory if it doesn't exist
# log_filename = os.path.join(log_directory, "logfile.log")

# Configure Loguru logger in append mode
logger.add(
    log_filename, mode="a", level="DEBUG", 
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
    )

# logger.add("log/{time:YYYY-MM-DD}.log", rotation="00:00", retention="1 day", format="{time:YYYY-MM-DD HH:mm:ss} - {level} - {message}")


def find_pred_rt_files(root_folder, send_remote_folder):
    for protocol_folder in os.listdir(root_folder):
        protocol_folder_path = os.path.join(root_folder, protocol_folder)
        for folder_name, subfolders, files in os.walk(protocol_folder_path):
            if "results" not in folder_name:
                continue
            for file in files:
                if file.endswith('.dcm'):  # Corrected this line
                    file_path = os.path.join(folder_name, file)
                    # Read DICOM file
                    ds = pydicom.dcmread(file_path)
                    # Get patient ID and replace backslashes with underscores
                    patient_id = ds.PatientID.replace("/", "_")
                    modality = ds.Modality
                    sop = ds.SOPInstanceUID

                    if modality == "RTSTRUCT":
                        # Check if a folder with patient ID exists
                        patient_folder = os.path.join(send_remote_folder, patient_id)
                        if os.path.exists(patient_folder):
                            dest_path = os.path.join(patient_folder, file)  # Destination path with original file name
                            newname = f"DRAW_{patient_id}_{sop}.dcm"
                            dest_path_newname = os.path.join(patient_folder, newname)
                            try:
                                if not os.path.exists(dest_path_newname):
                                    shutil.copy2(file_path, dest_path)  # Copying the file with original name to destination folder
                                    newname = f"DRAW_{patient_id}_{sop}.dcm"  # New name without folder name prefix
                                    new_path = os.path.join(patient_folder, newname)  # Full path to the new name in destination folder
                                    os.rename(dest_path, new_path)  # Renaming the file within the destination folder
                                    logger.debug(f"File copied and renamed in destination folder: {new_path}")
                                else:
                                    logger.info(f"file path already exists")
                            except FileExistsError:
                                logger.info(f"File already exists in destination folder: {dest_path}")
                        else:
                            logger.warning(f"Folder with patient ID does not exist: {patient_id}")


root_path = "Z:\\CHAVI\\test\\input"
# root_path = "D:\\totalsegmentator\\a9t_v2\\kgp.segmentation\\output"
remote_folder = "Z:\\CHAVI\\test\\output"
# remote_folder = "Z:\\import"
find_pred_rt_files(root_path, remote_folder)
