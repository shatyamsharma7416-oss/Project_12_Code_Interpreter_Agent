from functions.get_file_info import get_dir_info
from openai import OpenAI
import tomllib
from dotenv import load_dotenv
import os
import sys


def main():
    load_dotenv()

    with open("config.toml", "rb") as f:
        config = tomllib.load(f)

    LLM = config["MODEL"]
    model_config = config['models'][LLM]

    client = OpenAI(
        base_url = model_config['url'],
        api_key = os.getenv(model_config['api'])
    )

    if len(sys.argv) < 2:
        print("I need a prompt.")
        sys.exit(1)
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2] ==  "--verbose":
        verbose = True
    prompt = sys.argv[1]

    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model_config['name'],
        messages = messages
    )

    if verbose:
        print(f"User Prompt: {prompt}")
        print(f"Prompt Tokens: {response.usage.prompt_tokens}")
        print(f"Total Tokens: {response.usage.total_tokens}")       

    print(response.choices[0].message.content)


print(get_dir_info("calculator", "pkg"))

# if __name__ == "__main__":
    # main()