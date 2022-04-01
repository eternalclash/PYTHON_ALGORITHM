# append() 배열 원소 삽입
# sort() 기본 오름차순, sort()
# reverse()  리스트의 원소 순서를 모두 뒤집어 놓는다
# insert(삽입할 위치 인덱스,삽입할 값) 특정한 인덱스 위치에 원소를 삽입할 떄 사용
# count(특정 값) 리스트에서 특정한 값을 가지는 데이터의 개수를 셀 때
# remove(특정값) 특정한 값을 갖는 원소 제거, 값을 가진 원소가 여러개면 하나만 제거
# ex)
a = [1,2,3,4,5,5,5]
remove_set={3,5}

result = [i for i in a if i not in remove_set]