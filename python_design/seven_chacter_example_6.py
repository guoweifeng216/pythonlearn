import lgStudent

def main():
    listOfStudent=[]
    carryOn='Y'
    while carryOn=='Y':
        sr=lgStudent.LGstudent()
        name=raw_input("Enter student's name:")
        midterm=float(raw_input("Enter student's grade on midterm exam:"))
        final = float(raw_input("Enter student's grade on final exam:"))
        st=lgStudent.LGstudent(name,midterm,final)
        print st
        listOfStudent.append(st)
        carryOn=raw_input("Do you want to continue(Y/N)?")
        carryOn=carryOn.upper()
    print listOfStudent
    print type(listOfStudent)
    print "\nNAME\tGRADE"
    listOfStudent.sort(key=lambda x:x.getName())
    for pupil in listOfStudent:
        print pupil
main()