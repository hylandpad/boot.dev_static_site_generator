class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        props_str = ""
        for prop in self.props:
            props_str += f' {prop}="{self.props[prop]}"'
        return props_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        
    def to_html(self):
        if self.props:
            prop_string = self.props_to_html()
            return f'<{self.tag} {prop_string}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'
    