# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n = int(input())

ordered_dictionary = collections.OrderedDict()

for i in range(n):
    item = input().split()
    item_name = " ".join(item[:-1:])
    net_price = int(item[-1])
    if item_name in ordered_dictionary:
        ordered_dictionary[item_name] = ordered_dictionary[item_name] + net_price
    else:
        ordered_dictionary[item_name] = net_price

for key, value in ordered_dictionary.items():
    print(key, value)