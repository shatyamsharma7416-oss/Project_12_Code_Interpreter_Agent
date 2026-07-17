import os

def write_file(working_dir, file_path, content):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: \"{file_path}\" is not in the working dir"
    
    parent_dir = os.path.dirname(abs_file_path)
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Could not create  parent dirs: {parent_dir} = {e}"
    
    if not os.path.isfile(abs_file_path):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f"Could not create  parent dirs: {parent_dir} = {e}"
        
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f"Successfully wrote to \"{file_path}\" ({len(content)} chracters written)"
        
    except Exception as e:
        return f"Failed to write to \"{file_path}\", {e}"
        



schema_write_file = {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Overwrites an existing file or write to a new file if it doesn't exist (and creare required parent dirs safely.)",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the file to write."
                    },
                    "content": {
                        "type": "string",
                        "description": "The contents to write to the file as a string."
                    }
                },
                "required": ["file_path", "content"]
            }
        }
}
