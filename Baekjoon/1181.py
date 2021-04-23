N = int(input())
arr = list(set([input() for _ in range(N)]))
# arr = list(set(['wtf'+str(i) for i in range(N)]))
indexing = [[] for _ in range(51)]
for text in arr:
    indexing[len(text)].append(text)
result = []

for k in range(51):
    if len(indexing[k]) > 0:
        indexing[k] = sorted(indexing[k])
        result.extend(indexing[k])

for r in result:
    print(r)