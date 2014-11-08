#!/usr/bin/env Rscript

file_name="2014/11/NDIR_CO2_2014_11_07.txt"

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
names(t)=c("module","time","index","CO2","temperature","lamp")
t$time=strptime(t$time,format="%Y/%m/%d %H:%M:%S")
summary(t)

pdf()
plot(t$time,t$CO2)
plot(t$time,t$temperature)
dev.off()
