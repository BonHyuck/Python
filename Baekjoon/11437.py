import sys
sys.setrecursionlimit(1000000)

# 트리를 만들어봅시다
# 1번이 무조건 루트니까 1번부터 시작
def make_tree(parent):
    for node in input_list[parent]:
        # 아직 부모가 없음
        if tree[node] == 0:
            tree[node] = parent
            input_list[node].remove(parent)
            make_tree(node)
        else:
            return
    return


# 트리의 특성상 바로 위의 부모는 1개뿐
N = int(input())
input_list = [[] for _ in range(N+1)]
checked = [0 for _ in range(N+1)]
# N-1개만큼의 input이 들어온다.
# 누가 부모고 자식인지 아직 모름
for k in range(N-1):
    n1, n2 = map(int, input().split())
    input_list[n1].append(n2)
    input_list[n2].append(n1)

# index = 자식, value = 부모
tree = [0 for _ in range(N+1)]
make_tree(1)
M = int(input())
# 결과값
result = 0


# for k in range(M):
#     n1, n2 = map(int, input().split())
#     # n1의 부모노드 전부
#     first_parent = [tree[n1], n1]
#     first_parent_node = tree[n1]
#     while first_parent_node != 0:
#         first_parent.append(tree[first_parent_node])
#         first_parent_node = tree[first_parent_node]
#
#     second_parent_node = n2
#     while second_parent_node != 0:
#         if second_parent_node in first_parent:
#             result = second_parent_node
#             break
#         second_parent_node = tree[second_parent_node]
#     if result == 0:
#         result = 1
#     print(result)
#     result = 0