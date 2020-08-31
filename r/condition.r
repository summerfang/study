# if, if else

a <- 50L

if (is.integer(a)) {
    print("a is an integer")
} else {
    print("a is not an integer")
}

l <- c("google", "microsoft", "facebook")

you.like = "facebook"

if ( you.like %in% l)
    print("found")

# switch

str = switch("google", baidu = "baidu", google="google", microsoft = "microsoft")
print(str)

str = switch(2, "baidu", "google", "microsoft")
print(str)

str = switch(4, "baidu", "google", "microsoft")
print(str)
