library(hflights)
library(data.table)
library(tidyverse)

df <- as.data.frame(hflights)
dt <- as.data.table(hflights)
tib <- as_tibble(hflights)

dt[Month==10,mean(na.omit(AirTime)),by=UniqueCarrier]

# Create a dummy data.table and data.frame

dummy_frame_1 <- data.frame (
  id = 1:50,
  Capacity = sample(100:1000, size=50, replace = F),
  Code = sample(LETTERS[1:4], 50, replace = T),
  State = rep(c("Alabama","California","Taxes","Neveda"), len=50)
)

dummy_table_1 <- data.table(
  id = 1:50,
  Capacity = sample(100:1000, size=50, replace = F),
  Code = sample(LETTERS[1:4], 50, replace = T),
  State = rep(c("Alabama","California","Taxes","Neveda"),len=50)
)

dummy_tibble_1 <- data_frame(
  id = 1:50,
  Capacity = sample(100:1000, size=50, replace = F),
  Code = sample(LETTERS[1:4], 50, replace = T),
  State = rep(c("Alabama","California","Taxes","Neveda"),len=50)
)

# Describe data

nrow(dummy_frame_1)
nrow(dummy_table_1)
nrow(dummy_tibble_1)

ncol(dummy_frame_1)
ncol(dummy_table_1)
nrow(dummy_tibble_1)

str(dummy_frame_1)
str(dummy_table_1)
str(dummy_tibble_1)

names(dummy_frame_1)
names(dummy_table_1)
names(dummy_tibble_1)

head(dummy_frame_1)
head(dummy_table_1)
head(dummy_tibble_1)

summary(dummy_frame_1)
summary(dummy_table_1)
summary(dummy_tibble_1)

# Change column names
colnames(dummy_frame_1) = c("C1","C2","C3","C4")
colnames(dummy_table_1) = c("C1","C2","C3","C4")
colnames(dummy_tibble_1) = c("C1","C2","C3","C4")

colnames(dummy_frame_1)[which(names(dummy_frame_1) == "C1")] = "ID"
colnames(dummy_table_1)[which(names(dummy_table_1)=="C1")] = "ID"
colnames(dummy_tibble_1)[which(names(dummy_table_1)=="C1")] = "ID"

dummy_frame_1 <- setNames(dummy_frame_1, c("C1","C2","C3","C4"))
dummy_table_1 <- setNames(dummy_table_1, c("C1","C2","C3","C4"))
dummy_tibble_1 <- setNames(dummy_tibble_1, c("C1","C2","C3","C4"))

setnames(dummy_frame_1, c("C1"), c("ID"))
setnames(dummy_table_1, c("C1"), c("ID"))
setnames(dummy_tibble_1, c("C1"), c("ID"))

# Select columns

v_df_col_ID_1 <- dummy_frame_1[,c("ID")]
v_df_col_ID_2 <- dummy_frame_1$ID
v_df_col_ID_3 <- dummy_frame_1[["ID"]]
# v_df_col_ID_4 <- dummy_frame_1[,ID] # This is wrong format

df_col_ID <- dummy_frame_1["ID"]

dt_col_ID_1 <- dummy_table_1[,c("ID")]
dt_col_ID_2 <- dummy_table_1[,.(ID)]
dt_col_ID_3 <- dummy_table_1[,c(ID)]
# dt_col_ID_4 <- dummy_table_1["ID"] # This is wrong format

v_dt_col_ID_1 <- dummy_table_1[,ID]
v_dt_col_ID_2 <- dummy_table_1$ID
v_dt_col_ID_3 <- dummy_table_1[["ID"]]


df_cols <- dummy_frame_1["ID","C2"]

dt_col1 <- dummy_table_1[,c("ID", "C2")]
dt_cols <- dummy_table_1[,ID,C2]
dt_col_ID <- dummy_table_1[,ID]

tibble_col1 <- dummy_tibble_1[,c("ID")]
tibble_cols_1 <- dummy_tibble_1[c("ID","C2")]
tibble_cols_2 <- dummy_tibble_1[] 

tib %>% select(Year, Month)
