from leafnode import LeafNode
from htmlnode import ParentNode

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, node):
        if (self.text == node.text and
            self.text_type == node.text_type and
            self.url == node.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(text_node):
        type = text_node.text_type

        match type:
            case "text":
                return LeafNode(None, text_node.text)
            case "bold":
                return LeafNode("b", text_node.text)
            case "italic":
                return LeafNode("i", text_node.text)
            case "code":
                return LeafNode("code", text_node.text)
            case "link":
                return LeafNode("a", text_node.text, {"href" : text_node.url})
            case "image":
                return LeafNode("img", " ", {"src" : text_node.url , 
                                            "alt" : text_node.text})
            case _:
                raise Exception("Not a valid type.")
    
    #node(text, text_type, url=None)
    # def split_nodes_delimiter(old_nodes, delimiter, text_type):
    #     new_nodes = []

    #     temp_string = ""
    #     for node in old_nodes:
    #         if node.text_type != "text":
    #             new_nodes.append(node)
    #         else:
    #             temp_string = node.text
    #             while delimiter in temp_string:
    #                 sections = temp_string.split(delimiter, 2)
    #                 if len(sections) != 3:
    #                     raise Exception(f"Invalid markdown format: {node.text}")
    #                 if sections[0] != "":
    #                     new_nodes.append(TextNode(sections[0], "text"))
    #                 new_nodes.append(TextNode(sections[1], text_type))
    #                 temp_string = sections[2]
    #             if temp_string != "":
    #                 new_nodes.append(TextNode(temp_string, "text"))
    #             # start = 0
    #             # for i in range(0, len(node.text)):
    #             #     if node.text[i] == '*':
    #             #         if i > 0:
    #             #             new_nodes.append(TextNode(node.text[start:i]), )
    #             #             start = i
    #             #         if i + 1 < len(node.text) and node.text[i+1] == '*': #italics
    #             #             i += 2
    #             #             complete = False
    #             #             while i < len(node.text):
    #             #                 if (i + 1 < len(node.text) and 
    #             #                     node.text[i] == '*' and node.text[i+1] == "*"):
    #             #                     complete = True
    #             #                     i += 1
    #             #                     break
    #             #                 i += 1
    #             #             if not complete:
    #             #                 raise Exception(f"Invalid Markdown Format: {node.text}")
    #             #             complete = False
    #             #             new_nodes.append(TextNode())

    #                 #loop through till first character
    #                 #split, if prev list isn't empty then send as text
    #                 #check if remaining string contains delimiter, if not exception
    #                 #split("*", 1) --> splits until the next occurence

    #     return new_nodes
    