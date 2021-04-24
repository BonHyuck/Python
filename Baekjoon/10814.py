N = int(input())
members = [[] for _ in range(201)]
for k in range(N):
    age, name = input().split()
    members[int(age)].append(name)

for k in range(201):
    if len(members[k]) > 0:
        for name_index in range(len(members[k])):
            print(k, members[k][name_index])