from textnode import TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    temp_string = ""
    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            temp_string = node.text
            while delimiter in temp_string:
                sections = temp_string.split(delimiter, 2)
                if len(sections) != 3:
                    raise Exception(f"Invalid markdown format: {node.text}")
                if sections[0] != "":
                    new_nodes.append(TextNode(sections[0], "text"))
                new_nodes.append(TextNode(sections[1], text_type))
                temp_string = sections[2]
            if temp_string != "":
                new_nodes.append(TextNode(temp_string, "text"))
    return new_nodes

#example: https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png
def extract_markdown_images(text):
    list = []
    categories = re.findall(r"!\[[\w ]+\]", text)
    matches = re.findall(r"\w+://[\w _./-]+", text)
    for i in range(0, len(categories)):
        list.append((categories[i].strip("![]"), matches[i]))
    return list

def extract_markdown_links(text):
    list = []
    categories = re.findall(r"\[[\w ]+\]", text)
    matches = re.findall(r"\(([^()]+)\)", text)
    #matches = re.findall(r"\w+://[A-Za-z_./-]+", text)
    for i in range(0, len(categories)):
        list.append((categories[i].strip("[]"), matches[i]))
    return list

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            node_string = node.text
            image_tuples = extract_markdown_images(node_string)
            for tuple in image_tuples:
                list = node_string.split(f"![{tuple[0]}]({tuple[1]})", 1)
                if list[0] != "":
                    new_nodes.append(TextNode(list[0], "text"))
                new_nodes.append(TextNode(tuple[0], "image", tuple[1]))
                node_string = list[1]
            if node_string != "":
                new_nodes.append(TextNode(node_string, "text"))  
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != "text":
            new_nodes.append(node)
        else:
            node_string = node.text
            link_tuples = extract_markdown_links(node_string)
            for tuple in link_tuples:
                list = node_string.split(f"[{tuple[0]}]({tuple[1]})", 1)
                if list[0] != "":
                    new_nodes.append(TextNode(list[0], "text"))
                new_nodes.append(TextNode(tuple[0], "link", tuple[1]))
                node_string = list[1]
            if node_string != "":
                new_nodes.append(TextNode(node_string, "text"))  
    return new_nodes

def text_to_textnodes(text):
    #print(text)
    return split_nodes_link(
        split_nodes_image(
        split_nodes_delimiter(
        split_nodes_delimiter(
        split_nodes_delimiter([TextNode(str(text), "text")], "**", "bold"), 
        "*", "italic"), 
        "`", "code")))