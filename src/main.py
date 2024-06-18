import os
import shutil

from textnode import TextNode


def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)


def main():
    text = TextNode("Test Node Baby", "bold", "https://www.google.com")

    if os.path.exists("public"):
        shutil.rmtree("public")
    files = copy_files_recursive("static", "public")

    print(files)


main()
