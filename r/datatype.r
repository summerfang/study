# Numbers
integrate_value = 1
print(integrate_value)

# String
str = "Hellow World"
print(str)

# Boolean
b = TRUE

# Vector
position1 = c(10,20)
position2 = c(20,30)

new_pos = position1 + position2
print(new_pos)

#vector
var.1 = c(10,20,30)
var.2 <- c(40,50,60)
c(20,40,50)->var.3

var.4 <- c("Hello", "World")
c(TRUE,1)-> var.5

print(ls())

print(cat(1,"+",1,"=",1+1, '\n'))

# 
cat(1,"+","1","=",1+1,"\n",file="r.txt",append=TRUE)


#
print('ruboob'=='runoob')

a=1
b <- TRUE
b = "abc"

a=c(3,4)
b=c(5,0)
a+b

a = c(10,20,30,40,50)
print(a)

print(a[1:4])

a[c(1,3,5)]

a[c(-1,-5)]

c(1.1,1.2,1.3) - 0.5

a = c(1,2)
a ^ 2


a = c(1,3,5,2,4,6)
print(sort(a))

print(rev(a))

print(order(a))

print(a[order(a)])

print(sum(1:5))
print(sd(1:5))
print(range(1:5))

print(c(1,2,3)>2)

vector = c(10, 40, 78, 64, 53, 62, 69, 70)

print(vector[which(vector >= 60 && vector < 70)])

print(all(TRUE, FALSE, FALSE))

print(any(FALSE, TRUE, FALSE))

print(toupper("RunOON"))

print(nchar("中问", type="byte"))
print(nchar("中问", type="char"))

print(substring("1234567890",1,5))
print(substring("1234567800",5))
print(as.numeric("12"))
print(as.character(12.34))
strsplit("2019;10;1",";")
gsub("/",'-',"2019/10/1")

gsub("[[:alpha:]]+","$","Two World")

v1 = c(10,20,30,40,50,60)
m1 = matrix(vector, 3, 2, byrow = TRUE)

colnames(m1) = c("x","y")
rownames(m1) = c("a","b","c")