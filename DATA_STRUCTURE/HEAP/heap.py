# 일반적으로 힙 구현시 배열 자료구조 활용
# 배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 수월함
# parent node index= child node index//2
# left child node index = parent node index*2
# right child node index = parent node index*2 + 1



from turtle import left, right


class Heap:
    def __init__ (self,data):
        self.heap_array=list()
        self.heap_array.append(None) #인덱스는 1부터 시작
        self.heap_array.append(data)
    def move_up(self,inserted_idx): #노드의 위치를 판별
        if inserted_idx <=1:
            return False
        
        parent_idx = inserted_idx//2
        if self.heap_array[inserted_idx]>self.heap_array[parent_idx]:
            return True

    def insert(self,data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        
        inserted_idx=len(self.heap_array) - 1
        while self.move_up(inserted_idx): #바꿔줘야 할 노드이면 계속해서 바꿀 수 있게
            parent_idx = inserted_idx//2
            self.heap_array[inserted_idx],self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx=parent_idx
        return True
    def move_down(self,popped_idx):
        left_child_popped_idx=popped_idx*2
        right_child_popped_idx=popped_idx*2+1
        if left_child_popped_idx>=len(self.heap_array): #자식노드가 없을 때
            return False
        elif right_child_popped_idx>=len(self.heap_array):
            if self.heap_array[popped_idx]<self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_popped_idx]>self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else :
                    return False

    def pop(self):
        if len(self.heap_array) <=1:
            return None
        returned_data = self.heap_array[1]
        self.heap_array[1]=self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx=1

        while self.move_down(popped_idx):
            left_child_popped_idx=popped_idx*2
            right_child_popped_idx=popped_idx*2+1

            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx]<self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]=self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            else:
                if self.heap_array[left_child_popped_idx]>self.heap_array[right_child_popped_idx]:
                      self.heap_array[popped_idx],self.heap_array[left_child_popped_idx]=self.heap_array[left_child_popped_idx],self.heap_array[popped_idx]
                      popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx],self.heap_array[right_child_popped_idx]=self.heap_array[right_child_popped_idx],self.heap_array[popped_idx]
                        popped_idx=right_child_popped_idx
        return returned_data

heap=Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

