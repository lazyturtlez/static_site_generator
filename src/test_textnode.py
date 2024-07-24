import unittest

from textnode import TextNode
from textnode import text_node_to_html_node
from textnode import split_nodes_delimiter
from textnode import TEXT_TYPE_TEXT
from textnode import TEXT_TYPE_BOLD
from textnode import TEXT_TYPE_CODE
from textnode import TEXT_TYPE_ITALIC
from textnode import TEXT_TYPE_IMAGE
from textnode import TEXT_TYPE_LINK

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node 2", "bold")
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", "bold", "test url")
        node2 = TextNode("This is a text node", "bold", "test url")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", "bold", "test url")
        self.assertEqual("TextNode(This is a text node, bold, test url)", repr(node))

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        text_node = TextNode("test", "text")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "test")

    def test_text_to_bold(self):
        text_node = TextNode("test", "bold")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.to_html(), "<b>test</b>")

    def test_image(self):
        text_node = TextNode("test", "image", "www.test")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.props, {"src": "www.test", "alt": "test"})

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TEXT_TYPE_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded", TEXT_TYPE_BOLD),
                TextNode(" word", TEXT_TYPE_TEXT),
            ],
            new_nodes,
        )
    
    def test_single_node(self):
        node = TextNode("text **bold** text", TEXT_TYPE_TEXT)
        new_node = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        output = [
            TextNode("text ", TEXT_TYPE_TEXT),
            TextNode("bold", TEXT_TYPE_BOLD),
            TextNode(" text", TEXT_TYPE_TEXT),
        ]
        self.assertListEqual(output, new_node)

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded", TEXT_TYPE_BOLD),
                TextNode(" word and ", TEXT_TYPE_TEXT),
                TextNode("another", TEXT_TYPE_BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TEXT_TYPE_TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("bolded word", TEXT_TYPE_BOLD),
                TextNode(" and ", TEXT_TYPE_TEXT),
                TextNode("another", TEXT_TYPE_BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TEXT_TYPE_TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TEXT_TYPE_ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TEXT_TYPE_TEXT),
                TextNode("italic", TEXT_TYPE_ITALIC),
                TextNode(" word", TEXT_TYPE_TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TEXT_TYPE_TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TEXT_TYPE_BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TEXT_TYPE_ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TEXT_TYPE_BOLD),
                TextNode(" and ", TEXT_TYPE_TEXT),
                TextNode("italic", TEXT_TYPE_ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TEXT_TYPE_TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TEXT_TYPE_CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TEXT_TYPE_TEXT),
                TextNode("code block", TEXT_TYPE_CODE),
                TextNode(" word", TEXT_TYPE_TEXT),
            ],
            new_nodes,
        )




if __name__ == "__main__":
    unittest.main()