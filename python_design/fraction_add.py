import Fraction_cl
def main():
    first_numrator=int(raw_input("Enter numerator of first fraction:"))
    first_denominator=int(raw_input("Enter denominator of first fraction:"))
    second_numrator=int(raw_input("Enter numerator of second fraction:"))
    second_denominator=int(raw_input("Enter denominator of second fraction:"))
    fractionAdd(first_numrator,first_denominator,second_numrator,second_denominator)

def fractionAdd(first_numrator,first_denominator,second_numrator,second_denominator):
    numrator=first_numrator*second_denominator+first_denominator*second_numrator
    denominator=first_denominator*second_denominator
    reduction_num = Fraction_cl.Fraction(numrator, denominator)
    print "Sum:%d/%d"%reduction_num.reduction()
main()