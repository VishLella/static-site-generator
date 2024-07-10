import re

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
