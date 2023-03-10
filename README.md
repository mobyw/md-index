# md-index

Generate markdown index of files in folder for mkdocs.

## Install

```bash
pip install md-index
```

## Usage

```bash
Usage: md-index [OPTIONS]

Options:
  -i, --input-dir PATH        Input directory.
  -o, --output-dir DIRECTORY  Output directory.
  -d, --depth INTEGER         Depth of the file tree to generate, 1 or 2.
  -u, --url-prefix TEXT       Prefix for the URLs in the generated index.
  --help                      Show this message and exit.
```

The command will generate a folder (default: `docs`) with a markdown file for each folder in the input directory (default: `.`). The markdown file will contain a list of files in the folder.

Default depth is 1, which means only the folders in the root of the input directory will be processed. Depth 2 will process the folders in the root and the subfolders. The depth is limited to 2.

## Examples

### Single level directory

```bash
├─folder1
│  ├─file1.txt
│  ├─file2.txt
│  └─file3.txt
├─folder2
│  ├─file1.txt
│  └─file2.txt
└─README.md
```

```bash
md-index
```

### Two-level directory

```bash
├─folder1
│  ├─subfolder1
│  │  ├─file1.txt
│  │  ├─file2.txt
│  │  └─file3.txt
│  └─subfolder2
│  │  └─file1.txt
├─folder2
│  ├─subfolder1
│  │  └─file1.txt
│  └─subfolder2
│  │  ├─file1.txt
│  │  └─file2.txt
└─README.md
```

```bash
md-index --depth=2
```

### Github repository download link

```bash
md-index --url-prefix=https://raw.githubusercontent.com/{user}/{repo}/{branch}/
```

### Example processing flow

```bash
pip install md-index
pip install mkdocs
cd /path/to/project
md-index
mkdocs build
```

The generated markdown index is in folder `docs` and the mkdocs site is in folder `site`. If you don't have a `mkdocs.yml` file in the root of the input directory, a simple yml file will be auto generated and set the website name `File Index` and theme `readthedocs`.

### Automatically publishing a GitHub file repository to Github Pages

```yml
name: Build and Deploy
on: [push]
jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3

      - name: Install Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Install md-index
        run: pip install md-index

      - name: Install mkdocs
        run: pip install mkdocs

      - name: Build index
        run: md-index
        working-directory: "./"

      - name: Build website
        run: mkdocs build
        working-directory: "./"

      - name: Upload build folder to gh-pages branch
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: "./site"
```
