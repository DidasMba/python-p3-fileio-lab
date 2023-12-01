# lib/file_io.py

def write_file(file_name, file_content):
    """
    Write content to a .txt file.

    Parameters:
    - file_name (str): The name of the file (including file extension).
    - file_content (str): The content to be written to the file.
    """
    with open(file_name + ".txt", "w") as file:
        file.write(file_content)

def append_to_file(file_name, append_content):
    """
    Append content to a .txt file.

    Parameters:
    - file_name (str): The name of the file (including file extension).
    - append_content (str): The content to be appended to the file.
    """
    with open(file_name + ".txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    """
    Read and return the content of a .txt file.

    Parameters:
    - file_name (str): The name of the file (including file extension).

    Returns:
    - str: The content of the file.
    """
    with open(file_name + ".txt", "r") as file:
        return file.read()
