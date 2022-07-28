def fib(n):
    f_1 = 0
    f_2 = 1
    for i in range(2, n+1):
        f_1, f_2 = f_2, (f_1 + f_2)
    return f_2
    # put your code here

def main():
    n = int(input())
    print(fib(n))
    print(fib(n)%10)
if __name__ == "__main__":
    main()
