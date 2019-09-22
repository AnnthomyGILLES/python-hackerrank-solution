from collections import Counter


def minion_game(string):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    string_length = len(string)

    substring_list = []

    kevin_score = 0
    stuart_score = 0
    
    for i in range(string_length):
        if string[i] in vowels:
            kevin_score += string_length - i
        elif string[i] not in vowels:
            print(string[i:],  string_length - i)
            stuart_score += string_length - i

    if kevin_score > stuart_score:
        print('Kevin %s' % kevin_score)
    elif kevin_score < stuart_score:
        print('Stuart %s' % stuart_score)
    else:
        print('Draw')
    
if __name__ == "__main__":
    minion_game("BANANA")
