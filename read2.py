# words = [open('article.txt').read().split()]
words = ("hello goodbye hello ? - ” ")
# print(len(words))
# print(type(words))
# print(words[0])
new_words = words.split()#[0]
newer_words = []
newest_words = []
newest_words2 = []
newest_words3 = []
last_words =[]

for a in new_words:
    newer_words.append(a.lower())

for i in newer_words:
    newest_words.append(i.strip('”.!,()$-[]?%')) 
for a in newest_words:
    newest_words2.append(a.strip('“'))
for b in newest_words2:
    newest_words3.append(b.strip("’"))
# print(newest_words3)

# for x in newest_words3:
#     if x not in last_words:
#         last_words.append(x)
# # print(len(last_words))

print(newest_words3)

def word_count(x):
    counts = dict()
    words = x

    for word in newest_words3:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        
    return counts

    for x in counts:

        counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

# #     a = sorted(counts.items(), key=lambda x: x[1], reverse=True)
# # print(a)

        
print(word_count(newest_words3))














# newer_words = [[i.lower() for i in new_words.split()] for i in new_words]
# print(newer_words)
# for b in newer_words:

# print(newest_words)