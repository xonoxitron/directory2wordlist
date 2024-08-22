import os
import sys

def list_directory_contents(directory, output_file):
    with open(output_file, 'w') as f:
        for root, dirs, files in os.walk(directory):
            for name in dirs:
                full_path = os.path.join(root, name)
                relative_path = os.path.relpath(full_path, directory)
                print(relative_path)
                f.write(relative_path + '\n')
            for name in files:
                full_path = os.path.join(root, name)
                relative_path = os.path.relpath(full_path, directory)
                print(relative_path)
                f.write(relative_path + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("directory2wordlist Generate custom wordlists from directory structures for effective target enumeration. 🚀📂🔍")
        print("Usage: python directory2wordlist.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    output_file = 'paths.txt'
    
    if not os.path.isdir(directory):
        print(f"The specified directory {directory} does not exist.")
        sys.exit(1)
    
    list_directory_contents(directory, output_file)
    print(f"Directory contents have been written to {output_file}")
