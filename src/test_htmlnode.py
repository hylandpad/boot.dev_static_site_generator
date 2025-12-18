import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


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
        self.assertEqual(node.to_html(),'<p test="True" test2="False">This is a paragraph</p>')
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
        
    def test_to_html_with_children_with_props(self):
        child_node = LeafNode("span", "child",{'y':'false'})
        parent_node = ParentNode("div", [child_node],{'x':'true'})
        self.assertEqual(parent_node.to_html(), '<div x="true"><span y="false">child</span></div>')

    def test_to_html_with_multiple_children(self):
            child_node_1 = LeafNode("span", "child_1")
            child_node_2 = LeafNode("span", "child_2")
            parent_node = ParentNode("div", [child_node_1,child_node_2])
            self.assertEqual(parent_node.to_html(), "<div><span>child_1</span><span>child_2</span></div>")
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_multiple_grandchildren(self):
        grandchild_1_node = LeafNode("b", "grandchild_1")
        grandchild_2_node = LeafNode("i", "grandchild_2")
        child_node = ParentNode("span", [grandchild_1_node,grandchild_2_node,])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild_1</b><i>grandchild_2</i></span></div>",
        )

    def test_to_html_with_multiple_children_and_grandchildren(self):
        grandchild_1_node = LeafNode("b", "grandchild_1")
        grandchild_2_node = LeafNode("i", "grandchild_2")
        grandchild_3_node = LeafNode("b", "grandchild_3")
        grandchild_4_node = LeafNode("i", "grandchild_4")
        child_node_1 = ParentNode("span", [grandchild_1_node,grandchild_2_node,])
        child_node_2 = ParentNode("span", [grandchild_3_node,grandchild_4_node,])
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild_1</b><i>grandchild_2</i></span><span><b>grandchild_3</b><i>grandchild_4</i></span></div>",
        )
    
    def test_to_html_with_4_generations(self):
        grandchild_1_node = LeafNode("b", "grandchild_1")
        grandchild_2_node = LeafNode("i", "grandchild_2")
        great_grandchild_node = LeafNode("b","great_grandchild")
        grandchild_3_node = ParentNode("span", [great_grandchild_node])
        child_node_1 = ParentNode("span", [grandchild_1_node,grandchild_2_node,])
        child_node_2 = ParentNode("span", [grandchild_3_node])
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild_1</b><i>grandchild_2</i></span><span><span><b>great_grandchild</b></span></span></div>",
        )
    
    def test_to_html_with_4_generations_with_grandchildren_props(self):
        grandchild_1_node = LeafNode("b", "grandchild_1")
        grandchild_2_node = LeafNode("i", "grandchild_2")
        great_grandchild_node = LeafNode("b","great_grandchild")
        grandchild_3_node = ParentNode("span", [great_grandchild_node],{"style":""})
        child_node_1 = ParentNode("span", [grandchild_1_node,grandchild_2_node,])
        child_node_2 = ParentNode("span", [grandchild_3_node])
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b>grandchild_1</b><i>grandchild_2</i></span><span><span style=""><b>great_grandchild</b></span></span></div>',
        )
    
    
class TestErrors(unittest.TestCase):
    def test_to_html_missing_tag(self):
        def test_to_html_missing_tag(self):
            child_node = LeafNode("span", "child")
            parent_node = ParentNode(None, [child_node])
            with self.assertRaises(ValueError) as cm:
                parent_node.to_html()
            self.assertEqual(str(cm.exception),"ParentNode requires a tag to create HTML.")

    def test_to_html_missing_children(self):
        def test_to_html_missing_children(self):
            parent_node = ParentNode("div", None)
            parent_node.to_html()
            with self.assertRaises(ValueError) as cm:
                parent_node.to_html()
            self.assertEqual(str(cm.exception),"ParentNode requires at least one child to create HTML.")

if __name__ == "__main__":
    unittest.main()