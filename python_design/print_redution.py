import Fraction_cl
numerator=int(raw_input("Enter numrator of fraction:"))
denominator=int(raw_input("Enter numrator of denominator:"))
reduction_num=Fraction_cl.Fraction(numerator,denominator)
print "Reduction to lowest terms:%d/%d"%reduction_num.reduction()