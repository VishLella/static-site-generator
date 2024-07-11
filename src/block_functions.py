import re
from htmlnode import HTMLNode, ParentNode
from leafnode import LeafNode
from textnode import TextNode
from markdown_functions import text_to_textnodes


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    approved = []
    for block in blocks:
        block = block.strip(" ").strip("\n")
        if block != "":
            approved.append(block)
    return approved

def block_to_block_type(block):
    header = re.findall(r"^[#]{1,6} \w", block)
    code = block.split("```")
    if header:
        return "heading"
    if len(code) == 3 and code[0] == "" and code[2] == "":
        return "code"
    elif check_quote_block(block):
        return "quote"
    elif check_ulist_block(block):
        return "unordered_list"
    elif check_olist_block(block):
        return "ordered_list"
    return "paragraph"

def check_olist_block(block):
    lines = block.split("\n")
    for line in lines:
        temp = re.findall(r"^[1-9]{1}[0-9]*\. ", line)
        if not temp:
            return False
    return True

def check_ulist_block(block):
    lines = block.split("\n")
    for line in lines:
        if (line[0] != '*' and line[0] != '-') or line[1] != ' ':
            return False
    return True

def check_quote_block(block):
    lines = block.split("\n")
    for line in lines:
        if line[0] != '>':
            return False
    return True


def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    node_list = []
    for block in blocks:
        type = block_to_block_type(block)
        if type == "heading":
            node_list.append(heading_to_html(block))
            #return heading_to_html(block) #append to list
        elif type == "code":
            node_list.append(code_to_html(block))
            #return code_to_html(block)
        elif type == "quote":
            node_list.append(quote_to_html(block))
            #return quote_to_html(block)
        elif type == "unordered_list":
            node_list.append(ulist_to_html(block))
            #return 
        elif type == "ordered_list":
            node_list.append(olist_to_html(block))
            #return
        else:
            #paragraph
            node_list.append(p_to_html(block))
        
    #combine into parentnode div and return that
    return ParentNode("div", node_list)

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(TextNode.text_node_to_html_node(node))
    return html_nodes

def p_to_html(block):
    formatted_block = block.replace("\n", " ")
    children = text_to_children(formatted_block)
    return ParentNode("p", children)

def ulist_to_html(block):
    children = []
    lines = block.split("\n")    #parse block first line by line
    for line in lines:
        children.append(list_item_to_html(line[2:]))
    node = ParentNode("ul", children)
    return node

def olist_to_html(block):
    children = []
    lines = block.split("\n")    #parse block first line by line
    for line in lines:
        temp = line.split(". ", 1)
        children.append(list_item_to_html(temp[1])) #change this line
    node = ParentNode("ol", children)
    return node

def list_item_to_html(line):
    #<li>
    #text to children
    children = text_to_children(line)
    return ParentNode("li", children)

def quote_to_html(block):
    list = block.split("\n")
    quote= ""
    for line in list:
        quote += line[2:]
        quote += " "
    quote = quote.strip(" ")
    #quote = "".join(list)
    # get children (leafnodes) from quote
    children = text_to_children(quote)
    node = ParentNode("blockquote", children)
    return node

def code_to_html(block):
    text = block.split("```")
    inner = LeafNode("code", text[1])
    return ParentNode("pre", [inner])

def heading_to_html(block):
    hashtag = re.findall(r"^[#]{1,6}", block)
    text = block[len(hashtag[0]):].strip(" ")
    # get children (leafnodes) from text
    children = text_to_children(text)
    node = ParentNode(f"h{len(hashtag[0])}", children) #add children from text
    return node