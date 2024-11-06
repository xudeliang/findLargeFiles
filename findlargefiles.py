import os

def find_large_files(directory, size_limit=500 * 1024 * 1024):
    large_files = []
    # Walk through all directories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get the file size
                file_size = os.path.getsize(file_path)
                # Check if file size is greater than the specified limit
                if file_size > size_limit:
                    large_files.append((file_path, file_size))
            except (OSError, FileNotFoundError):
                # Some files might not be accessible, ignore them
                continue
    return large_files

# Call the function on the root directory
large_files = find_large_files('/')

# Print all files larger than 500MB
for file_path, size in large_files:
    print(f"{file_path} - {size / (1024 * 1024):.2f} MB")
