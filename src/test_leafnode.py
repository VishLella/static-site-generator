import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_tag_and_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    def test_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_tag(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_raw(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")



if __name__ == "__main__":
    unittest.main()