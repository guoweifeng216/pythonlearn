import Fraction_cl

decimal_number=float(raw_input("Enter a positive decimal less than 1:"))
if (decimal_number*10000)>0:
    reduction_num = Fraction_cl.Fraction(decimal_number*10000, 10000)
    print "Converted to fraction:%d/%d" % reduction_num.reduction()