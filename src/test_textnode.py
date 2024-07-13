import unittest

from textnode import TextNode
from textnode import text_node_to_html_node

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
        text_node = TextNode("test", "img", "www.test")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.props, {"src": "www.test", "alt": "test"})

if __name__ == "__main__":
    unittest.main()