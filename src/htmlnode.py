class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not implemented yet")
    
    def props_to_html(self):
        string = ""
        if not self.props:
            return string
        for key, value in self.props.items():
            #print(key + ", " + value)
            string += f" {key}=\"{value}\""
        return string
    
    def __repr__(self):
        return (f"HTMLNode:\n" +
                f"Tag: {self.tag}\n" +
                f"Value: {self.value}\n" + 
                f"Children: {self.children}\n" +
                f"Props: {self.props}")

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided.")
        if not self.children:
            raise ValueError("No children provided.")

        props_string = self.props_to_html()
        string = f"<{self.tag}{props_string}>"

        for child in self.children:
            try:
                string += child.to_html()
            except Exception as e:
                raise Exception(e, child)
        string += f"</{self.tag}>"
        return string
    