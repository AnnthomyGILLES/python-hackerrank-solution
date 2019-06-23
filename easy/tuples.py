if __name__ == '__main__':
    n = int(input())
    integer_list = input().split()
    ar=[]
    for i in range(0,len(integer_list)):
       ar.append(int(integer_list[i]))
    t=tuple(ar)
    print(hash(t))
