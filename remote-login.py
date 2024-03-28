
import win32wnet
import os

def connect_to_remote_drive(remote_host, username, password, remote_drive_letter='Z:'):
    remote_path = f"\\\\{remote_host}\\"
    try:
        win32wnet.WNetAddConnection2(0, None, remote_path, None, username, password)
        print(f"Connected to {remote_path} as {remote_drive_letter}")
        return True
    except Exception as e:
        print(f"Failed to connect to {remote_path}: {e}")
        return False

def disconnect_from_remote_drive(remote_drive_letter='Z:'):
    try:
        win32wnet.WNetCancelConnection2(remote_drive_letter, True)
        print(f"Disconnected from {remote_drive_letter}")
        return True
    except Exception as e:
        print(f"Failed to disconnect from {remote_drive_letter}: {e}")
        return False

# Example usage
remote_computer = '172.16.19.61\dicom'
username = 'Oncology\sougatamaity'
password = 'sougata'

# Connect to remote computer
if connect_to_remote_drive(remote_computer, username, password):
    print("connected...")
    # Now you can perform operations on the remote computer using the mapped drive
    # For example:
    # os.listdir('Z:\\')  # List files in the remote computer's C: drive
    # os.system('Z:\\path\\to\\executable.exe')  # Execute a program on the remote computer
    
    # Disconnect from the remote computer when done
    disconnect_from_remote_drive()
