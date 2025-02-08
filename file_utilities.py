import os
import datetime
import pandas as pd
import numpy as np
import shutil
from pathlib import Path
import json



def makedir(main_path, dir_name):
    """
    Create a directory if it doesn't exist.

    Parameters:
        main_path (str): The base path where the directory will be created.
        dir_name (str): The name of the directory to create.

    Returns:
        Path: The full path of the directory.
    """
    full_path = Path(f"{main_path}/{dir_name}")
    if not full_path.is_dir():
        full_path.mkdir()
    return full_path

def copy_files(source, destination):
    """
    Copy a file from the source to the destination.

    Parameters:
        source (str or Path): The path of the file to copy.
        destination (str or Path): The destination path where the file will be copied.
    """
    shutil.copy(source, destination)


def get_files(path, file_identifier):
    """
    Get a list of files in a directory that match a specific pattern.

    Parameters:
        path (Path): The directory path to search in.
        file_identifier (str): The pattern to match (e.g., '*.txt', '*.csv').

    Returns:
        list: A list of matching file paths.
    """
    return list(path.glob(file_identifier))

def read_json(param_file):
    """
    Read a JSON file and return its content as a dictionary.

    Parameters:
        param_file (str or Path): The path to the JSON file.

    Returns:
        dict: The content of the JSON file.
    """
    with open(param_file, 'r') as json_file:
        return json.load(json_file)

def get_input(choice_dict):
    """
    Display a menu of options and get user input to select one.

    Parameters:
        choice_dict (dict): A dictionary where keys are option numbers (as strings) and values are option descriptions.

    Returns:
        str: The selected option's name.
    """
    print("Available options:")
    for key, value in choice_dict.items():
        print(f"{key} = {value}")
    print()

    try:
        user_input = int(input("\nEnter a task number to select: "))
        name = choice_dict.get(str(user_input))

        if name:
            print(f"\nThe option with number {user_input} is '{name}'.")
        else:
            print(f"\nNo option was found with number {user_input}.")
        return name
    except ValueError:
        print("\nInvalid input. Please enter a number.")
        return None
