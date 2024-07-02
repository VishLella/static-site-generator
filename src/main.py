from textnode import TextNode
from htmlnode import HTMLNode, ParentNode
from leafnode import LeafNode

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

    # tempList = []
    # tempDict = {"href": "https://www.google.com", "target": "_blank"}

    # html = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    # print(html.props_to_html())
    

main()
