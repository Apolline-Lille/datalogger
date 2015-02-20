#!/usr/bin/env Rscript

file_name="2014/11/PAR_2014_11_25.txt"

#command line arguments
args=commandArgs(TRUE)
if(length(args)==0)
{
  cat("error: need file name to plot e.g.:\n"
    ,"./plot_log.Rsh 2015/02/ADC_2015_02_04.txt\n")
  q()
}#no argument

file_name=args[1]

t=read.table(file=file_name,sep=';')
names(t)=c("module","time","iterationOfProgram","iterationOfModule",
 "T",
 "A1","A1v",
 "A2","A2v",
 "A3","A3v",
 "A4","A4v",
 "A5","A5v",
 "A6","A6v",
 "A7","A7v",
 "A8","A8v")
t$time=strptime(t$time,format="%Y/%m/%d %H:%M:%S")

#t=t[1:1024,]
t=t[1:12,]
summary(t)

#plots
pdf()

#T
plot(t$time,t$T)
#A1-4 (Volt)
min=min(t$A1v,t$A2v,t$A3v,t$A4v)
max=max(t$A1v,t$A2v,t$A3v,t$A4v)
plot(t$time,t$A1v
 ,ylim=c(min,max)
 )
lines(t$time,t$A2v)
lines(t$time,t$A3v)
lines(t$time,t$A4v)
#A5-8 (Volt)
min=min(t$A5v,t$A6v,t$A7v,t$A8v)
max=max(t$A5v,t$A6v,t$A7v,t$A8v)
plot(t$time,t$A5v
 ,ylim=c(min,max)
 )
lines(t$time,t$A6v)
lines(t$time,t$A7v)
lines(t$time,t$A8v)

#A1-4 (value)
min=min(t$A1,t$A2,t$A3,t$A4)
max=max(t$A1,t$A2,t$A3,t$A4)
plot(t$time,t$A1
 ,ylim=c(min,max)
 )
lines(t$time,t$A2)
lines(t$time,t$A3)
lines(t$time,t$A4)
#A5-8 (value)
min=min(t$A5,t$A6,t$A7,t$A8)
max=max(t$A5,t$A6,t$A7,t$A8)
plot(t$time,t$A5
 ,ylim=c(min,max)
 )
lines(t$time,t$A6)
lines(t$time,t$A7)
lines(t$time,t$A8)

dev.off()
