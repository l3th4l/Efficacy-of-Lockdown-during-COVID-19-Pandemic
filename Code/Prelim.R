#install libraries 
#install.packages("readr")
#install.packages("ggplot2")
#install.packages("tidyverse")
#install.packages("ggpubr")

rm(list = ls()) #clear env 

#import libraries
library(readr)
library(ggplot2)
library(ggpubr)
library(tidyverse)

theme_set(theme_pubr())

data_dir = "../Datasets"
data_file = "COVID-19 Cases(14-03-2022).csv"


dat = read.csv(paste(data_dir, data_file, sep = "/"))
head(dat)

#convert types
dat$Date = as.Date.character(dat$Date, format = "%d/%m/%Y")

#plot time series 
dat_in = dat %>% filter(Region == "West Bengal" & Date > as.Date.character("1/1/2020", format = "%d/%m/%Y"))

dat_in[c("D.R.A")] = (dat_in$Death / (dat_in$Cured.Discharged + dat_in$Death)) * dat_in$Active.Cases

p1 = ggplot(data = dat_in, aes(x=Date, y=D.R.A,)) + geom_line(color = "#E46726", size = 1)
p2 = ggplot(data = dat_in, aes(x=Date, y=Active.Cases)) + geom_line(color = "#2E9FDF", size = 1)

figure <- ggpubr::ggarrange(p1, p2,
                    labels = c("DRA", "A"),
                    ncol = 1, nrow = 2)
figure
