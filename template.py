import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'CNNChickenClassifier'

list_of_files = [
    '.github/workflows/.gitkeep',
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Using pathlib.Path
    
    # Create directory if it doesn't exist
    if filepath.parent != Path('.'):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Creating directory: {filepath.parent} for the file {filepath.name}")
    
    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()  # Create empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
