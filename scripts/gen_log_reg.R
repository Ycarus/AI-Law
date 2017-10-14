library(dplyr)
library(ggplot2)
library(GGally)
library(caTools)
library(car) # for VIF

  data <- read.csv("data64.csv")
  set.seed(2784)
  split = sample.split(data$y, SplitRatio = 0.7)
  data.train <- filter(data, split == TRUE) 
  data.test <- filter(data, split == FALSE)
  mod <- glm(y ~., data=data.train, family = binomial(link='logit'), control = list(maxit = 50))
  summary(mod)
  predTest = predict(mod, newdata=data.test, type="response")
  table(data.test$y, predTest > 0.5)
  rm(list=ls())


