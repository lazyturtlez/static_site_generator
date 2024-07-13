import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag="test")
        node2 = HTMLNode(tag="test")
        self.assertEqual(node, node2)

    def test_false(self):
        node = HTMLNode(tag="tag")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_false2(self):
        node = HTMLNode(value="value")
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_false3(self):
        node = HTMLNode(children=[HTMLNode()])
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_false4(self):
        node = HTMLNode(props={"test":"case", "test2":"case2"})
        node2 = HTMLNode()
        self.assertNotEqual(node, node2)

    def test_props(self):
        node = HTMLNode(props={"test":"case", "test2":"case2"})
        self.assertEqual(' test="case" test2="case2"', node.props_to_html())

    def test_repr(self):
        node = HTMLNode()
        self.assertEqual("HTMLNode(None, None, None, None)", repr(node))

    def test_leafnode(self):
        node = LeafNode("p", "test")
        self.assertEqual(node.to_html(), "<p>test</p>")

    def test_leafnode_no_tag(self):
        node = LeafNode(None, "test")
        self.assertEqual(node.to_html(), "test")

    def test_to_html_with_children(self):
        child_node = LeafNode('c', "test")
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), "<p><c>test</c></p>")

    def test_to_html_with_many_children(self):
        child_node = LeafNode('c', "test")
        child_node2 = LeafNode('c2', "test2")
        child_node3 = LeafNode('c3', "test3")
        parent_node = ParentNode("p", [child_node, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<p><c>test</c><c2>test2</c2><c3>test3</c3></p>")

    def test_to_html_with_grand_children(self):
        grand_child = LeafNode('gc', "test_gc")
        child_node = ParentNode('c', [grand_child])
        parent_node = ParentNode("p", [child_node])
        self.assertEqual(parent_node.to_html(), "<p><c><gc>test_gc</gc></c></p>")

    def test_headings(self):
        node = ParentNode(
            "p",
            [
                LeafNode('c', "test"),
                LeafNode(None, "test2"),
                LeafNode("c3", "test3"),
                LeafNode(None, "test4")
            ]
        )
        self.assertEqual(node.to_html(), "<p><c>test</c>test2<c3>test3</c3>test4</p>")

if __name__ == "__main__":
    unittest.main()