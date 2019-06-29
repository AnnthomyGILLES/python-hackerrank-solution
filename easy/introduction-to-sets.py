def average(array):
    try:
        values = set(array)
        return sum(values)/len(values)
    except ZeroDivisionError:
        print("Pas de division par zero.")
        return None


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
