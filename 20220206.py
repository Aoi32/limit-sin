import sympy
x,y=symbols('x,y')
y=sin(x)/x
limit(y,x,oo)
plot(y,(x,-1,1),(y,-1,1))