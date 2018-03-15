import seven_2_1

def main():
    listOfStudent=obtainListOfStudent()
    displayResults(listOfStudent)



def obtainListOfStudent():
    carryOn='Y'
    listOfStudent=[]
    while carryOn=='Y':
        name=raw_input("Enter student's name:")
        midterm=raw_input("Enter student's grade on midterm exam:")
        final=raw_input("Enter student's grade on final exam")
        category=raw_input("Enter caregory (LG or PF):")
        if category=='LG':
            st=seven_2_1.LGstudent(name,midterm,final)
        else:
            st=seven_2_1.PFstudent(name,midterm,final)


        listOfStudent.append(st)
        carryOn=raw_input("Do you want to continue (Y/N)?")
        carryOn=carryOn.upper()

    return listOfStudent

def displayResults(listOfStudent):
    print "\nNAME\tGRADE"
    listOfStudent.sort(key=lambda x:x.getName())
    for pupil in listOfStudent:
        print pupil

main()