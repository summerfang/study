info = c(1,2,4,8)

names = c("Google", "Runoob", "Taobao", "Weibo")

cols = c("#ED1C24","#22B14C","#FFC90E","#3f48CC")

pie(info, labels=names, col=cols)

png(file="runoob-pie.png", height=300, width=300)