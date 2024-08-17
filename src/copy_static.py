import os
import shutil

def copy_dir(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for filename in os.listdir(source_dir_path):
        source_file_path = os.path.join(source_dir_path, filename)
        dest_file_path = os.path.join(dest_dir_path, filename)
        print(f"* {source_file_path} -> {dest_file_path}")
        if os.path.isfile(source_file_path):
            shutil.copy(source_file_path, dest_file_path)
        else:
            copy_dir(source_file_path, dest_file_path)
