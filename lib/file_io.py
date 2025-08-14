def write_file(file_name, file_content):
    """Write the given content to a .txt file with the given file_name."""
    with open(f"{file_name}.txt", "w") as f:
        f.write(file_content)

def append_file(file_name, append_content):
    """Append the given content to a .txt file with the given file_name."""
    with open(f"{file_name}.txt", "a") as f:
        f.write(append_content)

def read_file(file_name):
    """Read and return the content of the .txt file with the given file_name."""
    with open(f"{file_name}.txt", "r") as f:
        return f.read()
