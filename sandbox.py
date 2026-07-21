from functions.get_file_info import schema_get_file_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_function import call_function
from prompts import sys_prompt
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

    print(sys.argv)
    if len(sys.argv) < 2:
        print("I need a prompt.")
        sys.exit(1)
    verbose_flag = False
    if len(sys.argv) == 3 and sys.argv[2] ==  "--verbose":
        verbose_flag = True
    prompt = sys.argv[1]

    messages = [{"role":"system", "content":sys_prompt},{"role": "user", "content": prompt}]

    max_iters = config["MAX_LOOP"]

    for i in range(0, max_iters):
        response = client.chat.completions.create(
            model=model_config['name'],
            messages = messages,
            tools=[schema_get_file_info, schema_get_file_content, schema_run_python_file, schema_write_file],
            tool_choice="auto"
        )

        print(response)
        print("\n")
        messages.append(response.choices[0].message)


        if verbose_flag:
            print(f"User Prompt: {prompt}")
            print(f"Prompt Tokens: {response.usage.prompt_tokens}")
            print(f"Total Tokens: {response.usage.total_tokens}")       

        if response.choices[0].message.tool_calls:
            for tool_call in response.choices[0].message.tool_calls:
                

                result = call_function(tool_call.function, verbose_flag)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)  # Ensure content is a string!
                })

        if response.choices[0].finish_reason == "stop":
            break


    print(f"\n{messages}")


if __name__ == "__main__":
    main()
