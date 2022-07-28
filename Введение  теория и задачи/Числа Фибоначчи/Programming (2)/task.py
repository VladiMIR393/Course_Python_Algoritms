def fib_mod(n, m):
    f_1 = 0
    f_2 = 1
    a = []
    a.append(f_1 % m)
    a.append(f_2 % m)
    for i in range(2, 6*m+2):
        f_1, f_2 = f_2%m, (f_1 + f_2)%m
        a.append(f_2 % m)
        if i > 2 and a[i] == 1 and a[i-1] == 0:
            k = i-1
            return(a[n%k])
def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))
if __name__ == "__main__":
    main()