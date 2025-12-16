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
        if self.value is None:
           raise ValueError("LeafNode requires a value to create HTML.")
       
        if self.tag is None:
           return self.value
        
        if self.props:
            prop_string = self.props_to_html()
            return f'<{self.tag} {prop_string}>{self.value}</{self.tag}>'
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
        
    def to_html(self):
        if self.tag is None:
           raise ValueError("ParentNode requires a tag to create HTML.")
       
        if self.children is None:
           raise ValueError("ParentNode requires at least one child to create HTML.")
        
        if self.children == []:
            child_str = None
        else: 
            child_str = ''
            for child in self.children:
                child_str += child.to_html()
        
        if self.props:
            prop_string = self.props_to_html()
            html_str = f'<{self.tag}{prop_string if prop_string else ""}>{child_str if child_str else ""}</{self.tag}>'

        return html_str 
    