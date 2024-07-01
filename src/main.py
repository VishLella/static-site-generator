from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text = "This is a text node"
    type = "bold"
    url = "https://www.boot.dev"

    node = TextNode(text, type, url)

    tempList = []
    tempDict = {"href": "https://www.google.com", "target": "_blank"}

    html = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    print(html.props_to_html())
    

main()
