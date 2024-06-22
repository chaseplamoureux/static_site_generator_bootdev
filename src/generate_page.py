import os

from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.lstrip("# ")
    return Exception("No h1 header was found in markdown source file!")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = get_content(from_path)
    template_content = get_content(template_path)
    html_nodes = markdown_to_html_node(markdown_content)
    html_content = html_nodes.to_html()
    title = extract_title(markdown_content)
    template_content = template_content.replace("{{ Content }}", html_content)
    template_content = template_content.replace("{{ Title }}", title)
    # if not (os.path.exists(dest_path)):
    #     os.makedirs(dest_path)
    write_content(dest_path, template_content)


def get_content(path):
    with open(path, mode="r") as content:
        return content.read()


def write_content(path, file_content):
    with open(path, mode="w") as output:
        output.write(file_content)
