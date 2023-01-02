<h1>Factor Analysis (FA)</h1>

Factor Analysis is a part of Exploratory Data Analysis process which is commonly used for dimensionality reduction method.
It is used to reduce a large number of variables into smaller number of variables.
It also has other uses like linear projection and matrix factorization.


Factor analysis is widely utilized in market research, advertising, psychology, finance, and operation research.
Market researchers use factor analysis to identify price-sensitive customers,
identify brand features that influence consumer choice, 
and helps in understanding channel selection criteria for the distribution channel.



Factor analysis is a method for investigating whether a number of variables of interest X1, X2,……., Xl, 
are linearly related to a smaller number of unobservable factors F1, F2,..……, Fk.



Assumptions:
- There are no outliers in data.
- Sample size should be greater than the factor.
- There should not be perfect multicollinearity.
- There should not be homoscedasticity between the variables.



Types of Factor Analysis :
- Exploratory factor analysis: Useful when you don’t know what structure your data is in or dimensions
- Confirmatory Factor Analysis: Useful when you know how many dimensions are in set of variables


How does Factor Analysis Work?
The primary objective of factor analysis is to reduce the number of observed variables and find unobservable variables.
These unobserved variables help the market researcher to conclude the survey. 
This conversion of the observed variables to unobserved variables can be achieved in two steps:

- Factor Extraction: In this step, the number of factors and approach for extraction selected using variance partitioning methods such as principal components analysis and common factor analysis.
- Factor Rotation: In this step, rotation tries to convert factors into uncorrelated factors — the main goal of this step to improve the overall interpretability. There are lots of rotation methods that are available such as: Varimax rotation method, Quartimax rotation method, and Promax rotation method.


DETERMINING THE NUMBER OF FACTORS
The number of factors in our dataset is equal to the number of variables in our dataset.
 All the factors are not gonna provide a significant amount of useful information about the common variance among the variables.
  So we have to decide the number of factors.
  The number of factors can be decided on the basis of the amount of common variance the factors explain. 
  In general, we will plot the factors and their eigenvalues.

Eigenvalues are nothing but the amount of variance the factor explains.
 We will select the number of factors whose eigenvalues are greater than 1.


 “Beauty gets the attention but personality gets the heart”. These lines portray the importance of things which lies beyond our vision. What about a Machine Learning algorithm that finds information about the inner beauty like my heart which finds the creamy layer of the Oreo despite the unappetizing outer crunchy biscuits.

 INTRODUCTION
 Factor analysis is one of the unsupervised machine learning algorithms which is used for dimensionality reduction. This algorithm creates factors from the observed variables to represent the common variance i.e. variance due to correlation among the observed variables. Yes, it sounds a bit technical so let’s break it down into pizza and slices.
 
 Factor Analysis
 Representing features in terms of factors (Image by Author)
 
 x is the variable and F is the factor and l is the factor loading which can also be considered as the weight of the factor for the corresponding variable. The number of factors is equal to the number of variables.
 
 STORY-TIME
 Let’s get everything more clear with an example. Let’s imagine that every one of us is now a recruiter and we want to hire employees for our business firm. The interview process has been over and for each personality of the interviewee, we have rated them out of 10. The various personalities of the interviewee are distant, relaxed, careless, talkative, lazy, etc.
 
 There are about 32 variables. We can see that relaxed, careless, and lazy features are correlated because these persons won’t be successful. Since these variables are correlated we can try to form a factor called ‘unsuccessful behaviors’ which will explain the common variance i.e. variance due to correlation among these features.
 
 Factor Analysis
 Similar or correlated features can be grouped and represented as factors (Image by Author)
 
 The dataset and code can be downloaded from my GithubRepo
 
 STEPS INVOLVED IN FACTOR ANALYSIS
 The various steps involved in factor analysis are
 
 Loading Image
 DataHour: Predicting Road Quality using AI
 Date: THUR, 5 Jan 2022 Time: 7 PM - 8 PM IST
 Bartlett’s Test of Sphericity and KMO Test
 Determining the number of factors
 Interpreting the factors
 Make sure that you have removed the outliers, standard scaled the data and also the features have to be numeric.
 
 I am going to implement this in python with the help of the following packages
 
 factor_analyzer
 numpy
 pandas
 matplotlib
  
 
 BARTLETT’S TEST OF SPHERICITY
 Bartlett’s test checks whether the correlation is present in the given data. It tests the null hypothesis (H0) that the correlation matrix is an Identical matrix. The identical matrix consists of all the diagonal elements as 1. So, the null hypothesis assumes that no correlation is present among the variables.
 
 We want to reject this null hypothesis because factor analysis aims at explaining the common variance i.e. the variation due to correlation among the variables. If the p test statistic value is less than 0.05, we can decide that the correlation is not an Identical matrix i.e. correlation is present among the variables with a 95% confidence level.
 
 from factor_analyzer.factor_analyzer import calculate_bartlett_sphericitychi2,p = calculate_bartlett_sphericity(dataframe)
 print("Chi squared value : ",chi2)
 print("p value : ",p)#OUTPUT:Bartlett Sphericity TestChi squared value : 4054.19037041082
 p value : 0.0
 Read the dataset using pandas and store the dataset in a dataframe. We have stored the dataset in a dataframe named ‘dataset’. Just simply pass the ‘dataset’ through the calculate_bartltett_sphericty function, it will test the null hypothesis and will return the chi-squared value and the p test statistic. Since the p test statistic is less than 0.05, we can conclude that correlation is present among the variables which is a green signal to apply factor analysis.
 
 KAISER-MEYER-OLKIN (KMO) TEST
 KMO Test measures the proportion of variance that might be a common variance among the variables. Larger proportions are expected as it represents more correlation is present among the variables thereby giving way for the application of dimensionality reduction techniques such as Factor Analysis. KMO score is always between 0 to 1 and values more than 0.6 are much appreciated. We can also say it as a measure of how suited our data is for factor analysis.
 
 from factor_analyzer.factor_analyzer import calculate_kmokmo_vars,kmo_model = calculate_kmo(dataset)
 print(kmo_model)#OUTPUT:
 KMO Test Statistic 0.8412492848324344
 Just pass the dataframe which contains information about the dataset to the calculate_kmo function. The function will return the proportion of variance for each variable which is stored in the variable ‘kmo_vars’ and the proportion of variance for the whole of our data is stored in ‘kmo_model’. we can see that our data has an overall proportion of variance of 0.84. It shows that our data has more correlation and dimensionality reduction techniques such as the factor analysis can be applied.
 
 ###DETERMINING THE NUMBER OF FACTORS
 The number of factors in our dataset is equal to the number of variables in our dataset. All the factors are not gonna provide a significant amount of useful information about the common variance among the variables. So we have to decide the number of factors. The number of factors can be decided on the basis of the amount of common variance the factors explain. In general, we will plot the factors and their eigenvalues.
 
 Eigenvalues are nothing but the amount of variance the factor explains. We will select the number of factors whose eigenvalues are greater than 1.
 
 ####But why should we choose the factors whose eigenvalues are greater than 1?
 
 The answer is very simple. In a standard normal distribution with mean 0 and Standard deviation 1, 
 the variance will be 1. Since we have standard scaled the data the variance of a feature is 1. 
 This is the reason for selecting factors whose eigenvalues(variance) are greater than 1 i.e. 
 the factors which explain more variance than a single observed variable.

 


Factor Analysis Vs. Principle Component Analysis
- PCA components explain the maximum amount of variance while factor analysis explains the covariance in data.
- PCA components are fully orthogonal to each other whereas factor analysis does not require factors to be orthogonal.
- PCA component is a linear combination of the observed variable while in FA, the observed variables are linear combinations of the unobserved variable or factor.
- PCA components are uninterpretable. In FA, underlying factors are labelable and interpretable.
- PCA is a kind of dimensionality reduction method whereas factor analysis is the latent variable method.
- PCA is a type of factor analysis. PCA is observational whereas FA is a modeling technique.


Conclusion: Why use Factor Analysis?
Factor Analysis allows us to look at a large dataset and allows us to reduce the observed variables into fewer unobserved variables.
This helps to understand the relationships among the variables and to be able to determine how market is doing.
 Factors make us to be able to interpret data better. However, results are somewhat hard to determine because of the interpretations. 
 The interpretations that come from factor analysis can be controversial and made up because there can be multiple interpretations in one factor.


 Pros and Cons of Factor Analysis
 - Factor analysis explores large dataset and finds interlinked associations.
 It reduces the observed variables into a few unobserved variables or identifies the groups of inter-related variables, 
 which help the market researchers to compress the market situations and find the hidden relationship among consumer taste, 
 preference, and cultural influence. 
 Also, It helps in improve questionnaire in for future surveys. Factors make for more natural data interpretation.
 
- Results of factor analysis are controversial. Its interpretations can be debatable because more than one interpretation can be made of the same data factors.
  After factor identification and naming of factors requires domain knowledge.

Adequacy Test
Before you perform factor analysis, you need to evaluate the “factorability” of our dataset. Factorability means "can we found the factors in the dataset?". There are two methods to check the factorability or sampling adequacy:

- Bartlett’s Test
- Kaiser-Meyer-Olkin Test

