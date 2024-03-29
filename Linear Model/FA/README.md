<h1>Factor Analysis (FA)</h1>

<img src="imgs/fa1.png" alt="FA">

Factor Analysis is a part of Exploratory Data Analysis process which is commonly used for dimensionality reduction method.
It is used to reduce a large number of variables into smaller number of variables.
It also has other uses like linear projection and matrix factorization.


Factor analysis is widely utilized in market research, advertising, psychology, finance, and operation research.
Market researchers use factor analysis to identify price-sensitive customers,
identify brand features that influence consumer choice, 
and helps in understanding channel selection criteria for the distribution channel.



Factor analysis is a method for investigating whether a number of variables of interest X1, X2,……., Xl, 
are linearly related to a smaller number of unobservable factors F1, F2,..……, Fk.



<h3>Assumptions:</h3>

<ul>
  <li>There are no outliers in data.</li>
  <li>Sample size should be greater than the factor.</li>
  <li>There should not be perfect multicollinearity.</li>
  <li>There should not be homoscedasticity between the variables.</li>
</ul>



<h2>Types of Factor Analysis :</h2>

<ul>
  <li>Exploratory factor analysis: Useful when you don’t know what structure your data is in or dimensions</li>
  <li>Confirmatory Factor Analysis: Useful when you know how many dimensions are in set of variables</li>
</ul>


<h2>How does Factor Analysis Work?</h2>
The primary objective of factor analysis is to reduce the number of observed variables and find unobservable variables.
These unobserved variables help the market researcher to conclude the survey. 
This conversion of the observed variables to unobserved variables can be achieved in two steps:

<ul>
  <li>Factor Extraction: In this step, the number of factors and approach for extraction selected using variance partitioning methods such as principal components analysis and common factor analysis.</li>
  <li>Factor Rotation: In this step, rotation tries to convert factors into uncorrelated factors — the main goal of this step to improve the overall interpretability. There are lots of rotation methods that are available such as: Varimax rotation method, Quartimax rotation method, and Promax rotation method.
  </li>
</ul>


<h2>DETERMINING THE NUMBER OF FACTORS</h2>
The number of factors in our dataset is equal to the number of variables in our dataset.
 All the factors are not gonna provide a significant amount of useful information about the common variance among the variables.
  So we have to decide the number of factors.
  The number of factors can be decided on the basis of the amount of common variance the factors explain. 
  In general, we will plot the factors and their eigenvalues.

Eigenvalues are nothing but the amount of variance the factor explains.
 We will select the number of factors whose eigenvalues are greater than 1.

 


<h2>Factor Analysis Vs. Principle Component Analysis</h2>
<ul>
<li>PCA component is a linear combination of the observed variable while in FA, the observed variables are linear combinations of the unobserved variable or factor.</li>
  <li>PCA components explain the maximum amount of variance while factor analysis explains the covariance in data.</li>
  <li>PCA components are fully orthogonal to each other whereas factor analysis does not require factors to be orthogonal.</li>
  <li>PCA components are uninterpretable. In FA, underlying factors are labelable and interpretable.</li>
  <li>PCA is a kind of dimensionality reduction method whereas factor analysis is the latent variable method.  </li>
  <li>PCA is a type of factor analysis. PCA is observational whereas FA is a modeling technique.</li>
</ul>






<h2>Conclusion: Why use Factor Analysis?</h2>
Factor Analysis allows us to look at a large dataset and allows us to reduce the observed variables into fewer unobserved variables.
This helps to understand the relationships among the variables and to be able to determine how market is doing.
 Factors make us to be able to interpret data better. However, results are somewhat hard to determine because of the interpretations. 
 The interpretations that come from factor analysis can be controversial and made up because there can be multiple interpretations in one factor.


<h2>Pros and Cons of Factor Analysis</h2>
 <b>Factor analysis explores large dataset and finds interlinked associations.</b>
 It reduces the observed variables into a few unobserved variables or identifies the groups of inter-related variables, 
 which help the market researchers to compress the market situations and find the hidden relationship among consumer taste, 
 preference, and cultural influence. 
 Also, It helps in improve questionnaire in for future surveys. Factors make for more natural data interpretation.
 
 <b>Results of factor analysis are controversial.</b>
 Its interpretations can be debatable because more than one interpretation can be made of the same data factors.
  After factor identification and naming of factors requires domain knowledge.

<h3>Adequacy Test</h3>
Before you perform factor analysis, you need to evaluate the “factorability” of our dataset.
 Factorability means "can we found the factors in the dataset?". There are two methods to check the factorability or sampling adequacy:

- Bartlett’s Test
- Kaiser-Meyer-Olkin Test

