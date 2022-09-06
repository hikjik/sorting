input()
children = [int(i) for i in input().split()]
children.sort(reverse=True)

input()
cookies = [int(i) for i in input().split()]
cookies.sort(reverse=True)

count = 0
i = 0
for c in cookies:
    while i < len(children):
        if c < children[i]:
            i += 1
        else:
            count += 1
            i += 1
            break
print(count)
