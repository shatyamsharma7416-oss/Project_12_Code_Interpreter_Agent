import os
import tomllib

with open("config.toml", "rb") as file:
    config = tomllib.load(file)

MAX_CHARS = config["MAX_CHARS"]

def get_file_content(working_dir, file_path):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: {file_path} is not in the working directory"
    
    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file"
    
    file_content_string = ""
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if len(file_content_string) >= MAX_CHARS:
                file_content_string += (f'[...file "{file_path}" truncated at 10000 characters]')

        return file_content_string
    except Exception as e:
        return f"Exception reading file: {e}"




schema_get_file_content = {
        "type": "function",
        "function": {
            "name": "get_file_content",
            "description": "Gets the contents of the given file as a string, constrained to the working directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file, from the working directory."
                    }
                },
                "required": ["file_path"]
            }
        }
}
