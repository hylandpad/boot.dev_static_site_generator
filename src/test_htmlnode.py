import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlNode(self):
        nodes =[]
        
        nodes.append(HTMLNode('div','Test Div',[],{'test':'True','test2':'False'}))
        nodes.append(HTMLNode('div','Test Div',[],{}))
        nodes.append(HTMLNode('div','Test Div Parent',['Test Div'],{}))
        nodes.append(HTMLNode('div','Test Div Grandchild',[],{}))
        
        for node in nodes:
            node.props_to_html()
    
    def test_leaf_to_html(self):
        nodes =[]
        nodes.append(LeafNode('p','This is a paragraph'))
        nodes.append(LeafNode('p','This is a paragraph',{'test':'True','test2':'False'}))
        
        for node in nodes:
            node.to_html()
    
    def test_leaf_to_html_p(self):
        node = LeafNode('p','This is a paragraph',{'test':'True','test2':'False'})
        self.assertEqual(node.to_html(),'<p  test="True" test2="False">This is a paragraph</p>')


if __name__ == "__main__":
    unittest.main()