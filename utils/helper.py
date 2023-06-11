def text_to_markdown(text : str, file_path : str) -> None:
    with open(file_path, 'w') as file:
        file.write(text)
    
def open_markdown(file_path : str) -> str:
    with open(file_path, 'r') as file:
        return file.read()