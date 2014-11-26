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

#t=t[1:1024,]
summary(t)

#plots
pdf()
#temperature
plot(t$time,t$temperature)
plot(t$time,t$PAR6V*1000,
  main="PAR voltage (mV)")

#PAR
##vs time
min=min(t$PAR4,t$PAR5,t$PAR6)
max=max(t$PAR4,t$PAR5,t$PAR6)
plot(t$time,t$PAR4,col="red"
  ,ylim=c(min,max)
  )
lines(t$time,t$PAR5,col="green")
lines(t$time,t$PAR6,col="blue")

##histogram
min=0;zero=2^23;max=2^24;span=10000
h=hist(t$PAR6
  ,main=paste("full range histogram by classes of ",span," levels",sep="")
  ,xlim=c(min,max+span),breaks=seq(min,max+span,10000))
lines(c(min,min),  c(-1234,12),col="red")
lines(c(zero,zero),c(-1234,12),col="green")
lines(c(max,max),   c(-1234,12),col="blue")
#h
min=min(t$PAR6);max=max(t$PAR6);span=100
#h=hist(t$PAR6)
h=hist(t$PAR6
  ,main=paste("histogram by classes of ",span," levels",sep="")
  ,breaks=seq(min,max+span,span))
#h$breaks
#h
dev.off()
