T = int(input())
testes = []
while T > 0:
  T -= 1
  N, K = input().split()
  N = int(N)
  K = int(K)
  testes.append(T)
  for i in range(K):
      total = int(int(N % K) + int(N / K))
print(total)
