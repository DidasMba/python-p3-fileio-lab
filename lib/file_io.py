# lib/file_io.py

def write_file(file_name, file_content):
    """
    Write content to a .txt file.

    Parameters:
    - file_name (str): The name of the file (including file extension).
    - file_content (str): The content to be written to the file.
    """
  def write_file(file_name, file_content):
    """
    Write the given file_content to a file with the specified file_name.

    Parameters:
    - file_name (str): The name or path of the file to be written.
    - file_content (str): The content to be written to the file.
    """
    # Ensure the file_name has a .txt extension
    if not file_name.endswith('.txt'):
        file_name += '.txt'

    try:
        # Open the file for writing
        with open(file_name, 'w') as file:
            # Write the content to the file
            file.write(file_content)
        print(f"File '{file_name}' has been successfully written.")
    except Exception as e:
        print(f"Error writing to file '{file_name}': {e}")

# Example usage:
file_name = "example_file"
file_content = "This is an example content."

# Call the function with the provided arguments
write_file(file_name, file_content)
