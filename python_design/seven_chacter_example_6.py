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
    print "\nNAME\tGRADE"
    listOfStudent=listOfStudent.sort()
    for pupil in listOfStudent:
        print pupil
main()
cij_runner --hook-pr-trun dmesg sysinf pblk --env $CIJ_ENVS/hz-m2-fb3-131-48.sh --testsuite /root/git/cijoe/testsuites/block_smoke_01.suite -vv