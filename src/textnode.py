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

def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test.__repr__())

if __name__ == "__main__":
    main()