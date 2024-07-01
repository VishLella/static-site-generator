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

    