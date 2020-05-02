# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

from Testing import assertions

def find_student_average(student_marks, last_student_name):
    last_student_scores = student_marks[last_student_name]
    average = sum(last_student_scores) / len(last_student_scores)
    return '{:.2f}'.format(average)

example1 = dict([['Harsh', [25, 26.5, 28]], ['Anurag', [26, 28, 30]]])
assertions.assert_equals("26.50", find_student_average(example1, "Harsh"))

example2 = dict([['Krishna', [67, 68, 69]], ['Arjun', [70, 98, 63]], ['Malika', [52, 56, 60]]])
assertions.assert_equals("56.00", find_student_average(example2, "Malika"))