# 数据
input <- mtcars[,c('wt','mpg')]

# 生成 png 图片
png(file = "scatterplot.png")

# 设置坐标 x 轴范围 2.5 到 5, y 轴范围 15 到 30.
plot(x = input$wt,y = input$mpg,
   xlab = "Weight",
   ylab = "Milage",
   xlim = c(2.5,5),
   ylim = c(15,30),              
   main = "Weight vs Milage"
)