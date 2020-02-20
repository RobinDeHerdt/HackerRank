if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    last_student_name = input()

    last_student_scores = student_marks[last_student_name]
    average = sum(last_student_scores) / len(last_student_scores)
    print('{:.2f}'.format(average))