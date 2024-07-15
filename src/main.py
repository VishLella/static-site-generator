import os
import shutil

from block_functions import (
    markdown_to_blocks,
    markdown_to_html
)


def main():

    i = 1
    source = "./static"
    destination = "./public"
    template_path = "./template.html"

    reset_tree(destination)
    transfer_files(source, destination)
    #generate_page("./content/index.md", template_path, "./public/index.html")
    #generate_page("./content/majesty/index.md", template_path, "./public/majesty/index.html")
    generate_pages_recursive("./content", template_path, "./public")
   




    #1. remove all files in the public directory
def reset_tree(destination):
    shutil.rmtree(destination)
    os.mkdir(destination)

    #2. copy all files, subdirectories, nested files, etc from static to public dir
def transfer_files(source, destination):

    dir = os.listdir(source)
    for item in dir:
        path = os.path.join(source, item)
        #print(path)
        if(os.path.isfile(path)):
            shutil.copy(path, destination)
        else:
            os.mkdir(os.path.join(destination, item))
            transfer_files(path, os.path.join(destination, item))


def generate_page(from_path, template_path, dest_path):
    print(f"Generating from {from_path} to {dest_path} using {template_path}")

    markdown = ""

    try:
        with open(from_path, "r") as f:
            markdown = f.read()
    except FileNotFoundError as e:
        print("File not found: ", e)
        return
    
    title = extract_title(markdown)
    html_node = markdown_to_html(markdown)
    content = html_node.to_html()

    template = ""

    try:
        with open(template_path, "r") as f:
            template = f.read()
    except FileNotFoundError as e:
        raise FileNotFoundError("File not found: ", e)

    template = template.replace(
        "<title> {{ Title }} </title>",
        f"<title> {title} </title>")

    template = template.replace("{{ Content }}", content)

    try:
        with open(dest_path, "w") as f:
            f.write(template) 
    except Exception as e:
        raise Exception("Unable to write to file: ", e)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    #/content
    dir = os.listdir(dir_path_content)
    #dest = dest_dir_path
    for item in dir:
        path = os.path.join(dir_path_content, item)
        print(path)
        #dest = os.path.join(dest_dir_path, item)
        if(os.path.isfile(path)):
            generate_page(path, template_path, dest_dir_path + "/index.html")
            #shutil.copy(path, dest_dir_path)
        else:
            os.mkdir(os.path.join(dest_dir_path, item))
            generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, item))
            #transfer_files(path, os.path.join(dest_dir_path, item))

def extract_title(markdown):
    lines = markdown_to_blocks(markdown)
    firstline = lines[0]
    if firstline[:2] != "# ":
        raise Exception("No Title Found")
    return firstline[2:].strip(" ")

main()
