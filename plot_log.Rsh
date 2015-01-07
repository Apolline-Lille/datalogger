#!/usr/bin/env Rscript

file_name="2014/11/PAR_2014_11_25.txt"

#command line arguments
args=commandArgs(TRUE)
if(length(args)==0)
{
  cat("error: need file name to plot e.g.:\n"
    ,"./plot_log.Rsh 2014/11/PAR_2014_11_25.txt\n")
  q()
}#no argument

file_name=args[1]

t=read.table(file=file_name,sep=';')
names(t)=c("module","time","iteration","CO2","temperature","LED")
t$time=strptime(t$time,format="%Y/%m/%d %H:%M:%S")

#t=t[1:1024,]
summary(t)

#plots
pdf()

#CO2
plot(t$time,t$CO2)
plot(t$time,t$temperature)

dev.off()
