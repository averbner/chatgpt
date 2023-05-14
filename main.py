import openai
import typer
from rich import print
from rich.table import Table

def main():

    openai.api_key = "Your api key generated at https://platform.openai.com"

    print("💬 [bold green]ChatGPT API in Python[/bold green]")

    table = Table("Command", "Description")
    table.add_row("exit", "Exit application")
    table.add_row("new", "Create a new conversation")

    print(table)

    # Contexto del asistente
    context = {"role": "system",
               "content": "You are a very helpful assistant."}
    messages = [context]

    while True:

        content = __prompt()

        if content == "new":
            print("🆕 New conversation created")
            messages = [context]
            content = __prompt()

        messages.append({"role": "user", "content": content})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)

        response_content = response.choices[0].message.content

        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")


def __prompt() -> str:
    prompt = typer.prompt("\nWhat do you want to talk about? ")

    if prompt == "exit":
        exit = typer.confirm("✋ You're sure?")
        if exit:
            print("👋 See you later!")
            raise typer.Abort()

        return __prompt()

    return prompt


if __name__ == "__main__":
    typer.run(main)