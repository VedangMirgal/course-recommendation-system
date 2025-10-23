import nbformat
import os
import shutil
from datetime import datetime

# Folder containing your notebooks
notebook_folder = r"C:\Users\vedan\OneDrive\Desktop\ml_IBM\course-recommendation-system"

# Create a backup folder with timestamp
backup_folder = os.path.join(notebook_folder, "backup_" + datetime.now().strftime("%Y%m%d_%H%M%S"))
os.makedirs(backup_folder, exist_ok=True)
print(f"Backup folder created at: {backup_folder}\n")

# Loop through all .ipynb files in the folder
for filename in os.listdir(notebook_folder):
    if filename.endswith(".ipynb"):
        file_path = os.path.join(notebook_folder, filename)
        backup_path = os.path.join(backup_folder, filename)
        try:
            # Backup the original notebook
            shutil.copy(file_path, backup_path)
            
            # Read the notebook as nbformat 4
            nb = nbformat.read(file_path, as_version=4)
            
            # Clear outputs and execution counts
            for cell in nb.cells:
                if 'outputs' in cell:
                    cell['outputs'] = []
                if 'execution_count' in cell:
                    cell['execution_count'] = None
            
            # Write the cleaned notebook back
            nbformat.write(nb, file_path)
            print(f"[✓] Fixed notebook: {filename}")
        except Exception as e:
            print(f"[✗] Failed to process {filename}: {e}")

print("\nAll notebooks have been processed. Original files are backed up, and fixed versions are ready for GitHub.")
