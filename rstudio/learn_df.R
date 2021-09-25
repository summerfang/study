No <- c(1,2,3,4,5)
Name <- c("John","",NA,NA,"Allen")
Age <- c(20,3,4,NA,5)
Gender <- c("Female", "Male", "Female", "Male","Female")

name_list <- data.frame(No, Name, Age, Gender)

# name_list[!(is.na(Name) | Name == "")] tiggers a syntax mistake since it must use "," to claim it will choose what column
name_list[!(is.na(Name) | Name == ""),]
