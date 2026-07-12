import os

def get_dir_info(working_dir, dir=None):
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
    

    print(abs_working_dir)
    print(abs_dir)
    print(contents)