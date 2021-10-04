# Developing this repository

## Setup

The following is a possible way to set up this project, using Anaconda or Miniconda environment manager.

You can use any other environment manager as well, we use a standard requirements.txt file.

```bash
cd <project dir>
conda create -n eenlp python=3.8
conda activate eenlp
python -m pip install -r requirements.txt
# this makes the current project importable (as eenlp)
python -m pip install -e .
```

## Markdown generation

Locally:

```bash
python eenlp/docs/generate_docs.py
```

Using GitHub Actions:

- https://github.com/altsoph/EENLP/actions/workflows/generate-markdown.yml

Click "Run workflow" (you can choose branch, too).

You can change files in `eenlp/docs/`, e.g. languages, tasks, etc., and re-generate markdown to see the changes.