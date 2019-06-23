if __name__ == '__main__':
    from collections import defaultdict
    student = defaultdict(list)
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student[score].append(name)
        scores.add(score)
    second_best_score = sorted(scores)[1]
    print("\n".join(sorted(student[second_best_score])))



