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
names(t)=c("module","time","iteration","index","temperature","PAR0","PAR0V","PAR1","PAR1V","PAR2","PAR2V","PAR3","PAR3V","PAR4","PAR4V","PAR5","PAR5V","PAR6","PAR6V","PAR7","PAR7V")
t$time=strptime(t$time,format="%Y/%m/%d %H:%M:%S")
summary(t)

pdf()
plot(t$time,t$PAR4,col="red")
plot(t$time,t$PAR5,col="green")
plot(t$time,t$PAR6,col="blue")
min=8123123;max=9123123
h=hist(t$PAR6,xlim=c(min,max), breaks=seq(min,max,1000))
#h
min=8410000;max=8420000
h=hist(t$PAR6,xlim=c(min,max), breaks=seq(min,max,100))
#h
dev.off()
