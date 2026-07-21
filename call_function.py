from functions.get_file_content import get_file_content
from functions.get_file_info import get_file_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
import json

working_directory = "calculator"
def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.arguments})\n")
    else:
        print(f" - Calling function: {function_call_part.name}\n")

    # 1. Safely parse the JSON string into a Python dictionary
    try:
        args_dict = json.loads(function_call_part.arguments)
    except (json.JSONDecodeError, TypeError) as e:
        return {"Error": f"Invalid JSON arguments: {str(e)}"}

    result = ""
    if function_call_part.name == "get_file_content":
        result = get_file_content(working_directory, **args_dict)
    if function_call_part.name == "get_file_info":
        result = get_file_info(working_directory, **args_dict)
    if function_call_part.name == "run_python_file":
        result = run_python_file(working_directory, **args_dict)
    if function_call_part.name == "write_file":
        result = write_file(working_directory, **args_dict)
    if result == "":
        return {"Error": f"Unknown function: {function_call_part.name}"}
    
    return {
                "role": "tool",  # Must match the ID given by the model
                "name": function_call_part.name,
                "content": result,   # Must be a string (usually JSON serialized)
            }

