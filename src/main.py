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

    

    text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)"
    print(extract_markdown_images(text))

    text = "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
    print(extract_markdown_links(text))

    print("\n\n\n")

    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))

    print("\n\n\n")

    str = """
###### This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is a list item
- This is another list item
    """
    blocks = markdown_to_blocks(str)
    print(blocks)

    for block in blocks:
        print(block_to_block_type(block))
        #print(block, "\n")


    # tempList = []
    # tempDict = {"href": "https://www.google.com", "target": "_blank"}

    # html = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    # print(html.props_to_html())
    

main()
