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
summary(t)

#plots
pdf()

#T
plot(t$time,t$T)
#A1-4
plot(t$time,t$A1v)
lines(t$time,t$A2v)
lines(t$time,t$A3v)
lines(t$time,t$A4v)
#A5-8
plot(t$time,t$A5v)
lines(t$time,t$A6v)
lines(t$time,t$A7v)
lines(t$time,t$A8v)

dev.off()
