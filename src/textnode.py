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


def main():
    test = TextNode("This is a text node", "bold", "https://www.boot.dev")
    print(test.__repr__())

if __name__ == "__main__":
    main()