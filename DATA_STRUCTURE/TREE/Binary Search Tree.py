class Node:
    def __init__(self,value):
        self.value=value
        self.left= None
        self.right=None

class NodeMgmt:
    def __init__ (self,head):
        self.head =head
    
    def insert(self,value): #이진트리 탐색 삽입
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left!=None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left= Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node= self.current_node.right
                else:
                    self.current_node.right=Node(value)
                    break
    def search(self,value):
        self.current_node= self.head
        while self.current_node:
            if self.current_node.value==value:
                return print(True)
            elif value < self.current_node.value:
                self.current_node=self.current_node.left
            else :
                self.current_node=self.current_node.right
        return print(False)
    
    def delete(self,value):
        #삭제할 노드 탐색, 삭제할 노그가 없는 경우
        searched = False # 이 트리에 FAlse면 존재X
        self.current_node=self.head
        self.parent= self.head # 삭제할 노드 위에 있는 parent node
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent= self.current_node
                self.current_node= self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right
        if searched == False:
            return print(False)
        
        # 이후부터 Case들ㅇ을 분리해서 코드 작성
        #1. 삭제할 노드가 leaf Node인 경우
        #self.current_node가 삭제할 Node, self.parent는 삭제할 Node의 Parent Node인 상태
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        
        #2. 삭제할 Node가 Child Node를 한 개 가지고 있을 경우
        if self.current_node.left != None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left=self.current_node.left
            else:
                self.parent.right=self.current_node.left
        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent.value:
                self.parent.left= self.current_node.right
            else :
                self.parent.right=self.current_node.right
        
        if self.current_node.left != None and self.current_node.right != None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent= self.change_node
                    self.change_node = self.change_node.left
                self.change_node_parent.left = None
                if self.change_node.right != None:
                    self.change_node_parent.left=self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left!=None:
                    self.change_node_parent = self.change_node
                    self.change_node= self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left=self.change_node.right
                else :
                    self.change_node_parent.left=None
                self.parent.right= self.change_node
                self.change_node.left= self.current_node.left
                self.change_node.right= self.current_node.right
                


                

            





head = Node(1)
BST = NodeMgmt(head)
BST.insert(2)
BST.insert(3)
BST.insert(4)
BST.insert(6)
BST.insert(9)
BST.search(6)