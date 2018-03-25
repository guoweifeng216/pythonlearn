
class Fraction:
    def __init__(self,numerator="1",denominator="1"):
        self.numerator=numerator
        self.denominator=denominator

    def setNumerator1(self,numerator):
        self._numerator1=numerator

    def setDenominator1(self,denominator):
        self.denominator1=denominator

    def setNumerator2(self, numerator):
        self.numerator2 = numerator

    def setDenominator2(self, denominator):
        self.denominator2 = denominator

    def greatCommonDivisor(self,M,N):
        M=int(M)
        N=int(N)
        while True:
            if N == 0:
                # print "Greatest common divisor:%d" % M
                break
            else:
                T = N
                N = M % N
                M = T
        return M

    def reduction(self):
        numerator=self.numerator/self.greatCommonDivisor(self.numerator,self.denominator)
        denominator=self.denominator/self.greatCommonDivisor(self.numerator,self.denominator)
        # print "Reduction to lowest terms:%d/%d" % (numerator,denominator)
        return int(numerator),int(denominator)