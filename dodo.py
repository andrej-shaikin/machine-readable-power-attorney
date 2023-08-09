from typing import Dict, List, Union

from doit.action import CmdAction

__all__ = [
    "task_compile_requirements",
    "task_flake8",
]


def task_flake8() -> Dict[str, List[CmdAction]]:
    """Линтер."""
    return {
        "actions": [
            CmdAction("flake8 ./"),
        ],
    }


def task_install_requirements() -> Dict[str, List[Union[CmdAction, str]]]:
    """Установка зависимостей."""
    return {
        "actions": [
            CmdAction("pip install -r requirements/main.txt"),
            CmdAction("pip install -r requirements/dev.txt")
        ],
        "file_dep": [
            "requirements/main.txt",
            "requirements/dev.txt",
        ],
    }


def task_compile_requirements() -> Dict[str, List[Union[CmdAction, str]]]:
    """Компилирование зависимостей."""
    return {
        "actions": [
            CmdAction("pip-compile --allow-unsafe --generate-hashes requirements/main.in > requirements/main.txt"),
            CmdAction("pip-compile --allow-unsafe --generate-hashes requirements/dev.in > requirements/dev.txt"),
        ],
        "file_dep": [
            "requirements/main.in",
            "requirements/dev.in",
        ],
    }
