import unittest

from htmlnode import HTMLNode, ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    # def test_eq(self):
    #     tempList = [HTMLNode("a"), HTMLNode("a")]
    #     tempDict = {"href": "https://www.google.com", "target": "_blank"}

    #     node = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    #     node2 = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    #     self.assertEqual(node, node2)
    
    # def test_limit_eq(self):
    #     node = HTMLNode("p")
    #     node2 = HTMLNode("p")
    #     self.assertEqual(node, node2)

    # def test_noteq(self):
    #     tempList = [HTMLNode("a"), HTMLNode("a")]
    #     tempDict = {"href": "https://www.google.com", "target": "_blank"}

    #     node = HTMLNode("a", "In today's episode of..", tempList, tempDict)
    #     node2 = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    #     self.assertNotEqual(node, node2)

    # def test_dict_noteq(self):
    #     tempList = [HTMLNode("a"), HTMLNode("a")]
    #     tempDict = {"href": "https://www.google.com", "target": "_blank"}
    #     tempDict2 = {"href": "https://www.google.com", "target": "wrong"}

    #     node = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    #     node2 = HTMLNode("p", "In today's episode of..", tempList, tempDict2)
    #     self.assertNotEqual(node, node2)

    # def test_list_noteq(self):
    #     tempList = [HTMLNode("a"), HTMLNode("a")]
    #     tempList2 = [HTMLNode("a")]
    #     tempDict = {"href": "https://www.google.com", "target": "_blank"}
    #     tempDict2 = {"href": "https://www.google.com", "target": "_blank"}

    #     node = HTMLNode("p", "In today's episode of..", tempList, tempDict)
    #     node2 = HTMLNode("p", "In today's episode of..", tempList, tempDict2)
    #     self.assertNotEqual(node, node2)

    def test_props_to_html(self):
        tempList = []
        tempDict = {"href": "https://www.google.com", "target": "_blank"}

        node = HTMLNode("p", "In today's episode of..", tempList, tempDict)
        #print(node)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()

