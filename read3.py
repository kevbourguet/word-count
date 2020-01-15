
file_object = [open("article.txt").read().split()]
file_object = file_object[0]

file_object = [item.lower() for item in file_object]

file_object = [l.strip('”“‘!()[]?') for l in file_object]

counts = dict()

for words in file_object:
    if words in counts:
        counts[words] += 1
    else:
        counts[words] = 1

counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        



print(counts[:10])