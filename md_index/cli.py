from pathlib import Path
import click
from md_index.index import generate_index


@click.command()
@click.argument("directory", type=click.Path(exists=True), default=".")
@click.option(
    "-o",
    "--output",
    type=click.Path(file_okay=False, writable=True),
    default=".temp",
    help="Output directory.",
)
def generate(directory: str, output: str):
    output_dir = Path(output)
    output_dir.mkdir(parents=True, exist_ok=True)
    generate_index(Path(directory), output_dir)
    click.echo(f"Markdown index generated for {directory} in {output_dir}")


if __name__ == "__main__":
    generate()
