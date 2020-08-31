table = data.frame(name = c("John","Mark","Rose"),
    age=c(20,30,60),
    sex=c("male","male","femail")
)

print(table)
print(summary(table))
print(str(table))

result = data.frame(table$name, table$age)
print(result)

result = table[2:3,1:2]
print(result)

table$dept = c("tech","support","sales")

print(table)

# cbind
sites = c("google", "microsoft", "facebook")
urls = c("www.goolge.com", "www.microosoft.com", "www.facebook.com" )
likes = c(111,222,333)

address = cbind(sites, likes, urls)

print(address)

alotaddress = rbind(address, address, address)
print(alotaddress)

address$country <- c("USA", "USA", "USA")

