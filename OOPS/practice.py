class ComplexNumber:
    def __init__(self,real=0,imaginary=0):
        self.real=real
        self.imaginary=imaginary

    def conjugate(self):
        print(f"({self.real} , ({-1*self.imaginary}))")
    
    def __str__(self):
        if(self.imaginary<0):
            return (f"({self.real}{self.imaginary}i)")
        elif(self.imaginary>0):
            return (f"({self.real}+{self.imaginary}i)")
        else:
            return (f"{self.real}")
        
    def __add__(self,other):
        a=self.real+other.real
        b=other.imaginary+ self.imaginary
        return ComplexNumber(a,b)
    
    def __mul__(self,other):
        a=self.real
        b=self.imaginary
        c=other.real
        d=other.imaginary
        return ComplexNumber(a*c-b*d,a*d+b*c)

A=ComplexNumber(0,5)
A.conjugate()
print(A)

B=ComplexNumber(1,1)

C=A+B
print(A+B)
print(C)

D=A*C
print(D)