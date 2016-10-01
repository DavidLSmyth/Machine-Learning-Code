gini <- function(p,y,title, plot=T){ 
	sorted <- cbind(p,y)
	y.val <- sum(y) 
	set.seed(3546) 
	rand <- runif(length(p)) 
	sorted <- cbind(sorted[order(-p,rand),-1],c(1:y.val,rep(y.val,nrow(sorted)-y.val))) 
	sorted <- cbind(sorted,cumsum(sorted[,1])) 
	sorted <- cbind(sorted,cumsum(rep(y.val/length(y),length(y)))) 
	csum <- colSums(sorted[,2:4]) 
	gini <- (csum[2]-csum[3])/(csum[1]-csum[3])
	
	if (plot){ 
		plot( x=1:nrow(sorted)/nrow(sorted), y=sorted[,3]/y.val, main=title, xlab="% Investigated", ylab="% Captured", col = "white")
		lines(x=1:nrow(sorted)/nrow(sorted),y=sorted[,3]/y.val)
		lines(x=1:nrow(sorted)/nrow(sorted),y=sorted[,2]/y.val, col = "blue")
		text(x=0.8,y=0.2,labels=paste("Gini: ",round(gini*100,1),"%",sep=""))
		lines(c(0,1),c(0,1), col = "red") 
	}
	gini 
	}