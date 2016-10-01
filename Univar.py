def pythonUnivar(dataframe,feature, target, prediction=None,bins=10): 
    #dataframe should be a pandas dataframe
    #feature, target, prediction are strings
    #bins is an integer
    #add errorbars
    '''pythonUnivar is a function that will plot a histogram which has:
    
    1). n bins on the x-axis which partition the data set according to the provided feature
    2). A count on the y axis of the amount of people in each bin
    3). A line plot of how the target variable '1' value is distributed across each of the bins
    4). Optional: If there is a prediction column in the data set, a A line plot of how the predicted values are distributed across each of the bins
        
    args: 
    Dataframe is a pandas dataframe
    Feature is a column name of the dataframe by which the data will be partitioned
    Target is the dependent variable
    Prediction is a column of predictions of the dependent variable
    Bins is the number of bins to partition the data into, based on the distribution of the dependent variable.
        
    Example Call:
    '''
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    #==============================================================================
    #     implement error checking here    
    #==============================================================================
    #check that feature exists in dataframe, if not give suggestions 
    #check data can actually be divided up into given number of bins
    #check that prediction is also a binary variable

    #check validity of data, code is self documenting
    if(type(dataframe)!=pd.core.frame.DataFrame):
        print('You must provide a pandas dataframe, the dataframe you have provided is of type '+type(dataframe))
        return
    elif feature not in dataframe.columns:
        print(feature+' is not a valid column name')
        return 
    elif target not in dataframe.columns:
        print(target+' is not a valid column name')
        return
    elif ((prediction!=None) and (prediction not in dataframe.columns)):
        print(prediction+' is not a valid column name')
        return
    elif len(dataframe[target].unique())!=2:
        print('The target variable must be binary for this plot!')
        print(target+' has '+len(dataframe[target].unique())+' columns')
        return
    else:
        #encode the target variable to 1-0 binary values
        targetVar=dataframe[target]
        targetVals=dataframe[target].unique()
        dataframe[target]=np.where(dataframe[target]==targetVals[0], 1, 0) 
        
        #create a new matplotlib figure
        fig=plt.figure()
        ax1=fig.add_subplot(111)
        #add title
        plt.title('Histogram of '+feature+' and proportion of "successes" in each bin')
        #add second axis to give proporion of 1 values per bin
        ax2 = ax1.twinx()
        #label both axes
        ax2.set_ylabel('Proportion of Positive tests per bin')
        ax1.set_ylabel('Count of People in each bin')
        #create a regular histogram
        n=ax1.hist(dataframe[feature], bins=bins, normed=False, alpha=0.5)
        for i in n:
            print(i)
        #print(binedges)
        #ya,binedges=np.histogram(dataframe[feature], bins=bins, density=True)
        #ax1.plot(ya,binedges,color='green')
        #ax1.hist(dataframe[feature], density=True)
        #now add the line plot which shows how the response varies
        y,binEdges=np.histogram(dataframe[feature],weights=dataframe[target], bins=bins)
        print(binEdges)
        print(y)
        print(y/n[0])
        bincenters = (0.5*(binEdges[1:]+binEdges[:-1]))
        #mother of god this took ages
        ax1.plot(bincenters,(ax1.get_yticks()[-1])*(y/n[0]),'-', color='red', label='Target value density')
        
        
    #if there is a prediction, then also add it to the plot to see how closely it corresponds
    #to the target variable
    if prediction!=None:
        y2,binEdges2=np.histogram(dataframe[feature],weights=dataframe[prediction], bins=bins)
        bincenters2=0.5*(binEdges2[1:]+binEdges2[:-1])
        ax1.plot(bincenters2,(ax1.get_yticks()[-1])*(y2/n[0]),'-', color='green',label='Prediction density')
        print(y2)
        print(n[0])
        print((ax1.get_yticks()[-1])*(y2/n[0]))
    #replace the target variable with original non=numeric values
    ax1.legend(loc='upper left')
    dataframe[target]=targetVar
    return
