class Tree():
    def __init__(self, rootobj):
        self.__key = rootobj
        self.child = []
        self.childNum = 0

    def insertChild(self, newNode):
        t = Tree(newNode)
        self.child.append(t)
        self.childNum += 1

    def getFirstChild(self):
        if self.child:
            return self.child[0]
        else:
            return None

    def getLastChild(self):
        if self.child:
            return self.child[len(self)]
        else:
            return None

    def get_child(self, num):
        """
        """
        if self.child[num]:
            return self.child[num]
        else:
            return None

    def getRoot(self):
        return self.__key

    def deleteChild(self, num):
        if self.child[num]:
            self.child.pop(num)
            self.childNum -= 1
        else:
            return None
    
    def setRoot(self, obj):
        self.key = obj
    
    def getNodeNum(self):
        return self.childNum
    
    def output_tree(self, rootobj, num):
        buf = ''
        for i in range(num):
            buf = buf + '--'
        if hasattr(rootobj, 'getRoot'):
            print rootobj.getRoot()
            tree_list.append(buf+str(rootobj.getRoot()))
            for i in rootobj.child:
                self.output_tree(i, num+1)
        else:
            print rootobj
            tree_list.append(buf+str(rootobj))
        #keeptree.append((rootobj.getRoot(), rootobj.getNodeNum()))

tree_list = []
'''
atree = Tree('a')
atree.insertChild('b')
atree.insertChild('c')
atree.child[0].insertChild('d')
atree.child[1].insertChild('f')
'''
'''print atree.getRoot()
print atree.getFirstChild()
print atree.child[0].getRoot()
print atree.child[1].getRoot()
print atree.child[0].getFirstChild().getRoot()
print atree.child[1].getFirstChild().getRoot()
'''
'''
#keeptree = []
atree.set_output_tree(atree, 0)
a = atree.get_tree()
for i in a:
    print i
#print keeptree'''