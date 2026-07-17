import os

def get_file_info(working_dir="calculator", dir="."):
    abs_working_dir = os.path.abspath(working_dir)
    abs_dir = ""
    if dir is None:
        abs_dir = os.path.abspath(working_dir)
    else:
        abs_dir = os.path.abspath(os.path.join(working_dir, dir))
    if not abs_dir.startswith(abs_working_dir):
        return f"Error: \"{abs_dir}\" is not a directory"

    final_response = ""
    contents = os.listdir(abs_dir)
    for content in contents:
        content_path = os.path.join(abs_dir, content)
        is_dir = os.path.isdir(content_path)
        size = os.path.getsize(content_path)
        final_response += f"- {content}: file_size={size}, is_dir={is_dir}\n"
    return final_response



schema_get_file_info = {
        "type": "function",
        "function": {
            "name": "get_file_info",
            "description": "Lists files in the specified directory with their sizes, constrained to the working directory.",
            "parameters": {
                "type": "object",
                "properties": {
                    "dir": {
                        "type": "string",
                        "description": "The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself."
                    }
                },
                "required": ["dir"]
            }
        }
}
