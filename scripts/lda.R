library(dplyr)
library(ggplot2)
library(GGally)
library(caTools)
library(ROCR)
library(MASS)

  data <- read.csv("data1.csv")
  set.seed(2784)
  split = sample.split(data$y, SplitRatio = 0.7)
  data.train <- filter(data, split == TRUE) 
  data.test <- filter(data, split == FALSE)
  lda_mod <- lda(y ~., data=data.train)
  summary(lda_mod)
  predTest = predict(lda_mod, newdata=data.test)
  table(data.test$y, predTest > 0.5)
  rm(list=ls())


