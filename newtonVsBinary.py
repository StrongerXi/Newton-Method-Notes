#NOTE
# Newton method is supposed to converge quadratically once abs(guess - root) < 1 (not sure what happens when it's
# greater than 1, since it might oscillate or even never converge.
# However, as shown by running this script
# when f(x) = x^k, this does not work. This is because
# As shown in the proof for convergence of newton's method.
# If the term multiplied to e^2 keeps growing as x approaches root
# It may disrupt the convergence rate by over-dominating the (guess-root)^2 term.
# This might be rare since it requires the f to satifsfy a very specific mathematical property.
# for details please refer to the proof pdf.

tolerance = 0.000000001
slopePrecision = 0.001

def newton(f,a,count):    
    print(a)
    if abs(f(a)) <= tolerance:
        return (a,count)

    guess = a - f(a)/slopeAt(f,a)

    return newton(f,guess,count+1)



def slopeAt(f,x):
    
    left = x - slopePrecision
    right = x + slopePrecision

    return (f(right) - f(left)) / (2*slopePrecision)


# ASSUME: f(a) <= 0, f(b) >=0
def binary(f,a,b,count):
    print(a,b)
    if abs(f(a)) <= tolerance:
        return (a,count)
    
    mid = (b+a)/2

    if f(mid) < 0:
        return binary(f,mid,b,count+1)
    else:
        return binary(f,a,mid,count+1)



print(newton(lambda x: x**3+4*x**2+10, 2, 0))
print(binary(lambda x: x**3+4*x**2+10, -10, 2, 0))

print(newton(lambda x: x**3,50 ,0))
print(binary(lambda x: x**3, -50,50,0))

