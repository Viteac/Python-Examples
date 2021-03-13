names = []

scores = []


def average_marks():
    for i, v in enumerate(names):
        print(f'{v}  Marks:{scores[i]} Average: {float(sum(scores[i]) / len(scores[i]))}')


def name_score():
    t_m=[]
    n = input('Enter a Student name\n> ')
    names.append(n)

    while True:
        m = input('Enter student marks, if finished enter: "q"\n> ')
        if m == 'q':
            scores.append(t_m)
            break
        else:
            if not m.isdigit():
                print('You need Enter the number')
            else:
                t_m.append(int(m))

    question = input('Add more students? Y/N \n>').lower()
    if question == 'y':
        name_score()
    else:
        return

name_score()
average_marks()

