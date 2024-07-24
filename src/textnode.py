from htmlnode import LeafNode

TEXT_TYPE_TEXT = "text"
TEXT_TYPE_BOLD = "bold"
TEXT_TYPE_ITALIC = "italic"
TEXT_TYPE_CODE = "code"
TEXT_TYPE_LINK = "link"
TEXT_TYPE_IMAGE = "image"



class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node) -> bool:
        return (
            self.text == other_node.text
            and self.text_type == other_node.text_type
            and self.url == other_node.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TEXT_TYPE_TEXT:
        return LeafNode(None, text_node.text)

    if text_node.text_type == TEXT_TYPE_BOLD:
        return LeafNode("b", text_node.text)

    if text_node.text_type == TEXT_TYPE_ITALIC:
        return LeafNode("i", text_node.text)

    if text_node.text_type == TEXT_TYPE_CODE:
        return LeafNode("code", text_node.text)

    if text_node.text_type == TEXT_TYPE_LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})

    if text_node.text_type == TEXT_TYPE_IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    raise ValueError(f"Invalid text type: {text_node.text_type}")

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








def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test.__repr__())

if __name__ == "__main__":
    main()