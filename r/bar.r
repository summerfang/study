library(plotrix)
library(showtext);
font_add("SyHei", "SourceHanSansSC-Bold.otf");
cvd19 = matrix(
  c(83017, 83534, 1794546, 2640626, 190535, 585493),
  2, 3
)

# 设置文件名，输出为 png
png(file = "runoob-bar-2.png")
#加载字体
showtext_begin();
colnames(cvd19) = c("中国", "美国", "印度")
rownames(cvd19) = c("6月", "7月")

barplot(cvd19, main = "新冠疫情条形图", beside=TRUE, legend=TRUE,col=c("blue","green"),  family='SyHei')
# 去掉字体
showtext_end();
