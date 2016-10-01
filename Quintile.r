quintile <- function(var,p){ 
	cut(var, breaks= unique(quantile(var,probs=seq(0,1,by=p), na.rm=T)), include.lowest=T, ordered=T)
	}