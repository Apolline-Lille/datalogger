#!/usr/bin/env Rscript

file_name="2014/11/PID_2014_11_14.txt"

#command line arguments
args=commandArgs(TRUE)
if(length(args)==0)
{
  cat("error: need file name to plot e.g.:\n"
    ,"./plot_log.Rsh 2014/11/NDIR_CO2_2014_11_08.txt\n")
  q()
}#no argument

file_name=args[1]

t=read.table(file=file_name,sep=';')
names(t)=c("module","time","index","PID")
t$time=strptime(t$time,format="%Y/%m/%d %H:%M:%S")
summary(t)

pdf()
plot(t$time,t$PID)
min=0;max=1023
h=hist(t$PID,xlim=c(min,max), breaks=seq(min,max,1))
h
min=0;max=15
h=hist(t$PID,xlim=c(min,max), breaks=seq(min,max,1))
h
dev.off()
