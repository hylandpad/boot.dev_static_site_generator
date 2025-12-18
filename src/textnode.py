from enum import Enum
from htmlnode import ParentNode
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = 'text'
    BOLD = 'bold'
    ITALIC = 'italic'
    CODE = 'code'
    LINK = 'link'
    IMAGE = 'image'
    
class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type.TEXT:
        return LeafNode(None,text_node.value)
    elif text_node.text_type.BOLD:
        return LeafNode('b',text_node.value)
    elif text_node.text_type.ITALIC:
        return LeafNode('i',text_node.value)
    elif text_node.text_type.CODE:
        return LeafNode('code',text_node.value)
    elif text_node.text_type.LINK:
        return LeafNode('a',text_node.value)
    elif text_node.text_type.IMAGE:
        return LeafNode('img',text_node.value)
    else:
        raise Exception("Text Node text not of valid type")