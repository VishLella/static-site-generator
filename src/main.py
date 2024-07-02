from textnode import TextNode
from htmlnode import HTMLNode, ParentNode
from leafnode import LeafNode
from markdown_functions import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)
def main():
    text = "This is a text node"
    type = "bold"
    url = "https://www.boot.dev"

    node = TextNode(text, type, url)

    node = ParentNode(
        "p",
        [
            ParentNode("test", [
                LeafNode(None, "Normal text"),
                LeafNode("b", "Bold text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],),
            LeafNode("b", "Bold text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())

    nodes = [TextNode("This is `text` with a `code block` word", "text")]
    new_nodes = split_nodes_delimiter(nodes, "`", "code")
    print(new_nodes)

    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    print(extract_markdown_images(text))

    text = "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
    print(extract_markdown_links(text))

    # tempList = []
    # tempDict = {"href": "https://www.google.com", "target": "_blank"}

    # html = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    # print(html.props_to_html())
    

main()
