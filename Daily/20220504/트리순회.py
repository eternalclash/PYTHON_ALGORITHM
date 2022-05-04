# 매우중요한 포인트
# 중위 순횐는 x축 기준으로 볼떄 왼쪽부터 다맞는다
class Node:
    def __init__(self,data,left_node,right_node):
        self.data=data
        self.left_node=left_node
        self.right_node=right_node

def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node !='.':
        pre_order(tree[node.left_node])

def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')

n = int(input())
tree = {}
for i in range(n):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])