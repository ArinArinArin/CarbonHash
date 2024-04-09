import hashlib
import os

def hash_directory(path):
    # Create a hash object
    sha_hash = hashlib.sha256()
    
    # Walk through the directory
    for root, dirs, files in os.walk(path):
        # Sort the file names to ensure consistent order
        files.sort()
        # Read all files and update hash
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, 'rb') as f:
                    # Update the hash with the file content
                    sha_hash.update(f.read())
                # Update the hash with the file path to include it in the hash
                sha_hash.update(file_path.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return sha_hash.hexdigest()

# Point to the desired folder (replace with the actual path)
folder_path = '/Users/christianrobinson/Documents/Methodology/SCSA_prototype_data 2/2024/03/28'

# Generate and print the hash
print(hash_directory(folder_path))
