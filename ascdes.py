n = int(input())
m = list(input().split())
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if m[i] > m[j]:
            m[i], m[j] = m[j], m[i]
print(*m)
print(" ".join(m[::-1]))

