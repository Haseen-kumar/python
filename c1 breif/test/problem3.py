import os

def print_directory_contents(directory):
    # List all files and directories in the specified directory
    contents = os.listdir(directory)
    
    # Print each item in the directory
    for item in contents:
        print(item)

# Example usage:
directory_path = '/games' # Replace with the directory path you want to list

print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)