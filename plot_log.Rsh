#!/usr/bin/env Rscript

#arg

t=read.table(file="2014/11/NDIR_CO2_2014_11_07.txt",sep=';')
summary(t)
names(t)=c("module","time","temperature","CO2","lamp")
t$time=strptime(t$time,format="%Y/%m/%d %H:%M:%S")

pdf()
plot(t$time,t$CO2)
dev.off()
