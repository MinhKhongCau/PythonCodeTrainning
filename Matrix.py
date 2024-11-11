A = [[1,2],[3,4]]
B = [[4,3],[1,2]]
rel = []

# for i in range(len(A)):
#     tmp = []
#     for j in range(len(A[0])):
#         tmp.append(A[i][j]+B[i][j])
#     rel.append(tmp)
# print(rel)

for i in range(len(A)):
    tmp = []
    for j in range(len(A[0])):
        sum = 0
        for k in range(len(B)):
            sum+=(A[j][k]*B[k][j])
        tmp.append(sum)
    rel.append(tmp)
print(rel)