from htmlnode import HTMLNode

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        
        if not self.value:
            raise ValueError("leaf nodes require a value.:\n", self)
        
        if not self.tag:
            return self.value
        
        prop_string = self.props_to_html()
        if prop_string != "":
            return f"<{self.tag}{prop_string}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"