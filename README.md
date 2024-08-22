# directory2wordlist 🚀📂🔍

**directory2wordlist** is a Python tool designed for penetration testers and security professionals. It scans a specified directory and generates a custom wordlist based on the directory structure and file names. This wordlist can be used to enumerate targets by checking for the presence of directories and files on a web server or other target systems.

## Features

- Recursively list all directories and files within a specified directory.
- Output results to a file (`paths.txt` by default).
- Generate custom wordlists for directory and file enumeration.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/xonoxitron/directory2wordlist.git
   ```

2. Navigate to the project directory:

   ```bash
   cd directory2wordlist
   ```

> **Note:** Python 3.6 or higher is required.

## Usage

1. To list the contents of a directory and save the output to `paths.txt`:

   ```bash
   python directory2wordlist.py <directory>
   ```

   Replace `<directory>` with the path to the directory you want to list.

2. The results will be saved in `paths.txt` within the current directory.

3. Example:

   ```bash
   python directory2wordlist.py /path/to/directory
   ```

   Output:

   ```plaintext
   subdir1/
   subdir1/file1.txt
   subdir2/
   subdir2/file2.txt
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
