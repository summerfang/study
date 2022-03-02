rm(list=ls())
library(xgboost)
library(caret)

boston = MASS::Boston
str(boston)

set.seed(12)

indexes = createDataPartition(boston$medv, p = .85, list = F)
train = boston[indexes, ]
test = boston[-indexes, ]

train_x = data.matrix(train[, -13])
train_y = train[,13]

test_x = data.matrix(test[, -13])
test_y = test[, 13]

xgb_train = xgb.DMatrix(data = train_x, label = train_y)
xgb_test = xgb.DMatrix(data = test_x, label = test_y)

xgbc = xgboost(data = xgb_train, max.depth = 2, nrounds = 50)
print(xgbc)

pred_y = predict(xgbc, xgb_test)

mse = mean((test_y - pred_y)^2)
mae = caret::MAE(test_y, pred_y)
rmse = caret::RMSE(test_y, pred_y)

cat("MSE: ", mse, "MAE: ", mae, " RMSE: ", rmse)

x = 1:length(test_y)
plot(x, test_y, col = "red", type = "l")
lines(x, pred_y, col = "blue", type = "l")
legend(x = 1, y = 38,  legend = c("original test_y", "predicted test_y"), 
       col = c("red", "blue"), box.lty = 1, cex = 0.8, lty = c(1, 1))

