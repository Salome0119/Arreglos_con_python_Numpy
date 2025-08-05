#region serie fibonacci

#sin usar def, es decir, sin funciones
#Fn = F-1 + F-2
#f-1 va ser "a"
#f-2 va ser "b"
#Fn resultado final

a,b =0,1
#a=0  b=1

#Interante es una variable que tendra un comportamiento
#Incrementar el ciclo
for i in range(10):
    print(a)
    a,b=b,a+b
    #a=b y b=a+b
    
#0 a,b=b,a+b a=0 b=1+0=1
#1 a,b=b,a+b a=1 b=0+1=1
#2 a,b=b,a+b a=1 b=1+1=2
#3 a,b=b,a+b a=2 b=2+1=3 
#4 a,b=b,a+b a=3 b=3+2=5
#5 a,b=b,a+b a=5 b=3+5=8
#6 a,b=b,a+b a=8 b=5+8=13
#7 a,b=b,a+b a=13 b=8+13=21
#8 a,b=b,a+b a=21 b=13+21=34
#9 a,b=b,a+b a=34 b=21+34=55
#endregion