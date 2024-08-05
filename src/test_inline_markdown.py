import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)

from textnode import (
    TextNode,
    TEXT_TYPE_TEXT,
    TEXT_TYPE_BOLD,
    TEXT_TYPE_ITALIC,
    TEXT_TYPE_CODE,
    TEXT_TYPE_LINK,
    TEXT_TYPE_IMAGE
)

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

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        text = "![alt text 1](image link 1)"
        matches = extract_markdown_images(text)
        self.assertListEqual([("alt text 1", "image link 1")], matches)
    
    def test_many_images(self):
        text = "![alt text 1](image link 1) and ![alt text 2](image link 2)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            [
                    ("alt text 1", "image link 1"),
                    ("alt text 2", "image link 2"),
                ], 
                matches
        )
    
    def test_no_matches(self):
        text = "no matches should be found"
        matches = extract_markdown_images(text)
        self.assertListEqual([], matches)

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        text = "[alt text 1](link text 1)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("alt text 1", "link text 1")
            ],
            matches
        )
    
    def test_single_link(self):
        text = "[alt text 1](link text 1) and [alt text 2](link text 2) "
        matches = extract_markdown_links(text)
        self.assertListEqual(
            [
                ("alt text 1", "link text 1"),
                ("alt text 2", "link text 2")
            ],
            matches
        )

    def test_no_matches(self):
        text = "no matches should be found"
        matches = extract_markdown_links(text)
        self.assertListEqual([], matches)