import re
from textnode import (
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
    TEXT_TYPE_LINK,
    TEXT_TYPE_IMAGE
)

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TEXT_TYPE_TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TEXT_TYPE_TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
    new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches