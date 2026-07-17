import os
import subprocess

def run_python_file(working_dir: str, file_path: str, args=[]):
    abs_working_dir = os.path.abspath(working_dir)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f"Error: \"{file_path}\" is not in the working dir"

    if not os.path.isfile(abs_file_path):
        return f"Error: \"{file_path}\" is not a file"
    
    if not file_path.endswith(".py"):
        return f"Error: \"{file_path}\" is not a python file"
    
    try:
        final_args = ["python", file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True
        )
        final_string =  f"""
STDOUT: {output.stdout}
STDERR: {output.stderr}
\n
"""
        if output.stdout  == b"" and output.stderr == b"":
            final_string += "No Output Produced.\n"
        if output.returncode != 0:
            final_string += f"Process exited with code {output.returncode}"
        return final_string
    except Exception as e:
        return f"Error: executing Python file: {e}"




schema_run_python_file = {
        "type": "function",
        "function": {
            "name": "run_python_file",
            "description": "Runs a python file. Accepts additional CLI args as an optional array.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The file to run, relative the working directory."
                    },
                    "args": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        },
                        "description": "An optional array of strings to be used as the CLI args for the python file."
                    }
                },
                "required": ["file_path"]
            }
        }
}
