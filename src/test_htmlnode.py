import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHtmlNode(unittest.TestCase):
    def test_eq_false(self):
        node = HTMLNode("p", "Learning to Code")
        node2 = HTMLNode("a", "link to Google", None, {"href": "google.com"})
        self.assertNotEqual(node, node2)

    def test_to_html(self):
        node = HTMLNode("p", "Learning to code")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html_empty(self):
        node = HTMLNode("p", "Learning to code")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html(self):
        node = HTMLNode("a", "Learning to code", None, {"href": "boot.dev"})
        self.assertEqual(node.props_to_html(), ' href="boot.dev"')

    def test_repr(self):
        node = HTMLNode("p", "Learning to code")
        self.assertEqual(
            "HTMLNode(p, Learning to code, None, None)", repr(node)
        )

    def test_leaf(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leaf_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_no_props(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), 'Click me!')

    def test_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(
        ), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_parent_node_with_parent_prop(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            {"style": "text-align:right"}
        )
        self.assertEqual(node.to_html(
        ), '<p style="text-align:right"><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')


if __name__ == "__main__":
    unittest.main()
