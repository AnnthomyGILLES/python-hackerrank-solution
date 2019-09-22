def wrapper(f):
    def fun(l):
        tmp = list()
        for idx, item in enumerate(l):
            if len(item) == 10:
                item = "+91" + item
            elif item.startswith("+91"):
                pass
            else:
                if item.startswith("0"):
                    item = item.replace("0", "+91", 1)
                elif item.startswith("91"):
                    item = item.replace("91", "+91", 1)
            s = item[:3] + " " + item[-10:-5] + " " + item[-5:]
            tmp.append(s)
        f(tmp)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    # l = [input() for _ in range(int(input()))]
    l = ["09191919191", "9100256236", "+919593621456"]
    sort_phone(l)
