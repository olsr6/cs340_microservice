# REQUIRED IMPORTS
import subprocess
import sys

# REQUIRED VARIABLES (CHANGE THESE)
source_path = r"C:\Users\olson\OneDrive\Documents\CS361\Microservice\example.txt"
destination_path = r"C:\Users\olson\Downloads"

# REQUIRED SUBPROCESS CALL
result = subprocess.run([sys.executable, "microservice.py", source_path, destination_path], check=True, stdout=subprocess.PIPE, text=True)
confirmation = result.stdout.strip()
    
print(confirmation)