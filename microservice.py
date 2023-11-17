import sys
import os
import shutil

if __name__ == "__main__":

    # ARGUMENTS CHECK
    if len(sys.argv) != 3:
        print("Usage: python file_mover.py <source_path> <destination_folder>")
        exit()

    # HANDLE ARGUMENTS
    source_path = os.path.normpath(sys.argv[1])
    destination_path = os.path.normpath(sys.argv[2])

    # CHECK IF SOURCE IS FILE
    if not os.path.isfile(source_path):
        print(f"Error: '{source_path}' is not a file.")
        exit()

    # MOVE FILE
    try:
        file_name = os.path.basename(source_path)
        dest_path = os.path.join(destination_path, file_name)

        shutil.move(source_path, dest_path)
        print("File " + source_path + " moved to " + destination_path)

    # ERROR CHECK
    except Exception as e:
        print(f"Error: {e}")
