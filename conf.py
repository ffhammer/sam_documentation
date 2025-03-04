import os
import sys

sys.path.insert(0, os.path.abspath("sam/src"))
from sam.ec_x_sys import generate_ecx_sys_prediction, ECxSySPrediction

project = "SAM"
copyright = "2024, Felix Hammer"
author = "Felix Hammer"
release = "30.10.2024"


extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",  # Automatically document from docstrings
    "sphinx.ext.napoleon",  # Support for Google-style and NumPy-style docstrings
    "sphinx_autodoc_typehints",  # Include type hints in the docs (optional)
]


templates_path = ["_templates"]
exclude_patterns = [
    "experiments",
    "imgs",  # Ignore the imgs folder
    "templates",  # Ignore the templates folder
    "index.md",  # Ignore index.md
    "*.md",  # Ignore all other .md files
    "_build",
    "Thumbs.db",
    ".DS_Store",  # Default exclusions
]


html_theme = "sphinx_material"
html_static_path = ["_static"]
autodoc_member_order = "bysource"

html_theme_options = {
    "repo_url": "https://github.com/mockaWolke/sam",
    "repo_name": "SAM Repository",
}
