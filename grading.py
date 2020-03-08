def gradingStudents(grades):
    # Write your code here
    final=[]
    for grade in grades:
        if(grade>36):
            x=grade%5
            y=5-x
            if(y<5):
                if((grade+y)-grade<3):
                    grade=grade+y
                    final.append(grade)
                else:
                    final.append(grade)
        else:
            final.append(grade)
    return final

if __name__ == '__main__':
        grades=[12,43,23,76,67]
        print(gradingStudents(grades))
