from pathlib import Path
import sys
import shutil

from normalaze import normalazie

CATEGORIES = {'Images': ['.JPEG', '.PNG', '.JPG', '.SVG'],
              'video': ['.AVI', '.MP4', '.MOV', '.MKV'], 'Document': ['.DOC', '.DOCX', '.TXT', '.PDF', '.XLSX', '.PPTX'],
              'Music': ['.MP3', '.OGG', '.WAV', '.AMR'], 'archives': ['.ZIP', '.GZ', '.TAR'], 'others': ['']}


def remove_dir(path: Path):
    folders_to_delete = [f for f in path.glob("**")]
    for folder in folders_to_delete[::-1]:
        try:
            folder.rmdir()
        except OSError:
            continue


def move_file(path: Path, root_dir: Path, categorie: str) -> None:
    target_dir = root_dir.joinpath(categorie)
    if not target_dir.exists():
        target_dir.mkdir()
    path.replace(target_dir.joinpath(f'{normalazie(path.stem)}{path.suffix}'))


def get_category(path: Path) -> str:
    ext = path.suffix.upper()
    for cat, val in CATEGORIES.items():
        if ext in val:
            return cat
    if ext not in val:
        ext = CATEGORIES['others']
    return cat


def sort_folder(path: Path):
    for item in path.glob('**/*'):
        if item.is_file():
            cat = get_category(item)
            move_file(item, path, cat)
            print(item)


def unpack_archice(path: Path):
    for item in path.glob('**/*'):
        try:
            shutil.unpack_archive(
                item, f'{item}{item.stem}')
            print('good')
        except shutil.ReadError:
            continue


def main():
    try:
        # path = Path(r'C:\Users\Ulfanzer\Desktop\Testfolder')
        path = Path(sys.argv[1])
    except IndexError:
        return "No path folder"

    if not path.exists():
        return f"Folder with path {path} doesn't exists"

    sort_folder(path)
    remove_dir(path)
    unpack_archice(path)
    return 'All ok'


if __name__ == '__main__':
    print(main())
