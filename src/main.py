from textnode import TextNode
from htmlnode import HTMLNode, ParentNode
from leafnode import LeafNode
from markdown_functions import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes
)
from block_functions import (
    markdown_to_blocks,
    block_to_block_type
)

import os
import shutil

def main():

    i = 1
    source = "./static"
    destination = "./public"
    reset_tree(destination)
    transfer_files(source, destination)

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


main()
