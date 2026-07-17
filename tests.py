from functions.get_file_info import get_dir_info
from functions.get_file_content import file_content
from functions.write_file import write_code_file
from functions.run_python_file import run_code


def main():
    working_dir = "calculator"
    print(get_dir_info(dir="."))

main()

