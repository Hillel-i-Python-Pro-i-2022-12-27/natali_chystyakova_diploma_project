import pathlib
from typing import Final

from apps.config.path import FILES_OUTPUT_PATH

PAGES_PATH: Final[pathlib.Path] = FILES_OUTPUT_PATH.joinpath("pages")
