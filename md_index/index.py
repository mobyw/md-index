from typing import List
from pathlib import Path


def generate_index(dir: Path, output_dir: Path):
    """Generate a markdown index for the given directory."""
    folders = get_folders(dir)
    for folder in folders:
        index_path = output_dir / f"{folder.name}.md"
        with open(index_path, "w", encoding="utf-8") as f:
            readme_path = folder / "README.md"
            if readme_path.is_file():
                f.write(readme_path.read_text(encoding="utf-8") + "\n\n")
            else:
                f.write(f"# {folder.name}\n\n")
            f.write("## File list\n\n")
            files_str = get_file_tree(folder)
            f.write(files_str)


def get_folders(dir: Path) -> List[Path]:
    """Return a list of folders in the given directory."""
    folders = dir.glob("*")
    folders = [
        folder
        for folder in folders
        if folder.is_dir() and not folder.name.startswith(".")
    ]
    folders.sort(key=lambda x: x.name)
    return folders


def get_file_tree(path: Path, depth: int = -1, tree_str: str = ""):
    if path.is_file():
        path_str = str(path).replace("\\", "/")
        tree_str += "  " * depth + f"- [{path.name}]({path_str})\n"
    elif path.is_dir():
        if depth != -1:
            tree_str += "  " * depth + "- " + str(path.relative_to(path.parent)) + "\n"
        for cp in path.iterdir():
            tree_str = get_file_tree(cp, depth + 1, tree_str)
    return tree_str
