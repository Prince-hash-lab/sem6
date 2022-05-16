library(topsis)
mydata=read.csv('data.csv')
mydata
d <- as.matrix(mydata[,-1]) # -1, drop 1st column
d
w <- c(1, 1, 1, 1)
w

i <- c("+", "+", "-", "+")
i
topsis(d, w, i)

