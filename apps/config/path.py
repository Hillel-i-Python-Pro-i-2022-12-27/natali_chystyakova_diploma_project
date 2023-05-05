from pathlib import Path
from typing import Final

# ROOT_PATH = Path(__file__).parent
# print(ROOT_PATH)

ROOT_PATH: Final[Path] = Path(__file__).parents[2]

# FILES_INPUT_PATH: Final[Path] = ROOT_PATH / "files_input"
FILES_INPUT_PATH: Final[Path] = ROOT_PATH.joinpath("files_input")
FILES_OUTPUT_PATH: Final[Path] = ROOT_PATH.joinpath("files_output")
