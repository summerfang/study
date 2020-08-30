# (),^,%%,%/%,*,/,+-
print(8/4%%3)
print(8/0.5^2)
print(8/8%%4%/%2)

# >,>=,<,<=,!=

v1=c(2,3,4,6)
v2=c(2,3,5,6)

print(v1 >= v2)
print(v1 > v2)
print(v1 < v2)
print(v1 <= v2)
print(v1 == v2)
print(v1!=v2)

# &,|,!,&&,||

v3 = c(3,1,TRUE,2+3i)
v4 = c(5,1,FALSE,2+3i)

print(v3|v4)
print(v3&v4)
print(!v3)

print(v3&&v4)
print(v3||v4)

v1<-c(3,1,TRUE,"runoob")
v2<<-c(3,1,TRUE,"runoob")
v3=c(3,1,TRUE,"runoob")

print(v1)
print(v2)
print(v3)

c(3,1,TRUE,"runoob")->v4
c(3,1,TRUE,"runoob")->>v5
print(v4)
print(v5)

# :, %in%, %*%
v <- 1:15
print(v)

v1<-3
v2<-5

print(v1%in%v)
print(v2%in%v)

M = matrix(c(10,20,30,40,50,60), nrow=2,ncol=3,byrow=TRUE)
print(M)
print(t(M))

t = M %*% t(M)

# math
print(sqrt(4))
print(exp(4))
print(log(4,2)) 
print(log10(100))

print(round(4.6))
print(round(4.67,1))
print(ceiling(4.1))
print(floor(3.9))

print(sin(pi/2))
print(sin(pi/6))
print(cos(pi/4))
print(tan(pi/3))

print(asin(0.5))
print(acos(0.7071068))
print(atan(1.732051))

# Probabity density function

print(dnorm(0))
print(pnorm(0))
print(qnorm(0.5))

print(rnorm(3, 5, 2))
