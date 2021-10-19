a = [10,20,60,80,20,60]
dup_items = []
uniq_items = []
for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.append(x)
dup_items.sort()
print(dup_items)