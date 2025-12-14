import textnode

print('hello world')

def main():
    dummyNode = textnode.TextNode('here is some text',textnode.TextType.LINK_TEXT,'https://www.boot.dev')
    print(dummyNode)
    
main()