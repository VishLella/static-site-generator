import unittest

from htmlnode import HTMLNode

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
        print(node)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())

if __name__ == "__main__":
    unittest.main()

