import os
import shutil

from textnode import TextNode
from generate_page import generate_page


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

    if os.path.exists("public"):
        shutil.rmtree("public")
    files = copy_files_recursive("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

main()
