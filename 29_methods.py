# functions are used to rerun a given set of codes
# It is used to achieve DRY : Do not Repeat Yourself
def studentmarks(rollno, stumarks):
    for id in stumarks.keys():
        if rollno == id:
            print(f'Student with roll number: {rollno} has secured {stumarks[rollno]} marks.')
        else:
            print(f'Invalid roll number:{rollno}')
            break


marks = {'1234': 180, '7890': 250, '5678': 500}
roll = input('Enter the roll number:')
studentmarks(roll, marks)


def highest_even(*args):
    even = []
    for num in args:
        if (int(num) % 2) == 0:
            even.append(num)
    return max(even)


even_list = [12, 4, 7, 3, 24, 9, 8, 10]
max_even = highest_even(12, 4, 7, 3, 24, 9, 8, 10)
print(f'Highest even number from list', even_list, f' is {max_even}')
