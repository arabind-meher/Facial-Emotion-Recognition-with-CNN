from pathlib import Path


def read_dirs(_path: str, filter: list | None = None) -> list:
    path = Path(_path)
    return [
        (dir.name, str(dir))
        for dir in path.iterdir()
        if dir.is_dir() and (filter is None or dir.name in filter)
    ]


def read_files(_path: str, ext: list | None = None) -> list:
    path = Path(_path)
    return [
        str(file)
        for file in path.iterdir()
        if file.is_file() and (ext is None or file.suffix in ext)
    ]
