from example.example_file import add_one
import typer

app = typer.Typer()


@app.command(help="adds one to the input")
def run_add_one(x: int = typer.Option(0, help="enter an integer")):
    print(add_one(x))


if __name__ == "__main__":
    app()
