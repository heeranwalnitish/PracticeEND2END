import os
import logging
from pathlib import Path

logging.basicConfig(level= logging.INFO, format= "[%(asctime)s: %(message)s:]")

project_name = "TextSummarizz"

list_of_files = [
    "github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "setup.py",
    "main.py",
    "requirements.txt",
    "NOTEBOOK/trails.ipynb"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory:{filedir} fot the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as file_obj:
            pass
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")