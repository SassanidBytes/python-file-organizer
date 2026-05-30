# 📁 File Organizer

A professional CLI tool that automatically sorts files into subfolders by type.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Tests](https://img.shields.io/badge/Tests-5%20passed-brightgreen)

## Features

- Organizes files into categories: Images, Documents, Music, Videos, Code, Archives
- `--dry-run` mode to preview changes without moving files
- `--verbose` mode for detailed logging
- Clean summary after every run
- 100% tested with pytest

## Installation

```bash
git clone https://github.com/SassanidBytes/python-file-organizer.git
cd python-file-organizer
pip install -e .
```

## Usage

```bash
# Organize a folder
file-organizer /path/to/folder

# Preview without moving files
file-organizer /path/to/folder --dry-run

# Detailed output
file-organizer /path/to/folder --verbose
```

## Project Structure


src/file_organizer/
├── config.py      # Extension → category mapping
├── organizer.py   # Core logic
├── cli.py         # Command-line interface
tests/
└── test_organizer.py


## License

MIT