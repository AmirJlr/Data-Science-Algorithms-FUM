# Gaussian Mixture Models

## First -- What is a Gaussian?

## A Distribution is a listing of outcomes of an experiment and the probability associated with each outcome


## What is a Gaussian Mixture Model?

It's a probability distribution that consists of multiple probability distributions.


Hard vs Soft Assignment. Hard might lead to mis grouping.

Guassian Mixture:

Instead of Hard assgning data points to a cluster, if we are uncertain about the data points where they belong or to which group, we use this method. It uses probability of a sample to determine the feasibility of it belonging to a cluster.


## How is it Optimized?

The Expecation Maximization Algorithm!


#### Comparing to Gradient Descent 
You can obtain maximum likelihood estimates using different methods and using an optimization algorithm is one of them. On another hand, gradient descent can be also used to maximize functions other than likelihood function.

## When Should I Use it?

Anytime you have unlabeled data and want to classify it. If data is normally distributed. 

Predicting Customer Churn
Anomaly Detection
Object Tracking

<img src ='imgs/Difference_between_KNN_and_GMM_300w.webp' />


If we have data where we assume that the clusters are not defined by simple circles but by more complex,
ellipsoid shapes, we prefer the GMM approach over the KNN approach. Additionally,
if we want to have soft cut-off borders and therewith probabilities, that is,
if we want to know the probability of a datapoint to belong to each of our clusters, 
we prefer the GMM over the KNN approach. Hence, 
if there arise the two buzz words <b>probabilities</b> and <b>non-circular</b> during our model selection discussion,
we should strongly check the use of the <b>GMM</b>.

<table>
    <tr>
    <td><img src="imgs/GMM_1.webp" alt="GMM"/></td>
    <td><img src="imgs/GMM_2.webp" alt="GMM"/></td>
    <td><img src="imgs/GMM_3.webp" alt="GMM"/></td>
    </tr>
</table>



we have seen that we can create an arbitrary dataset,
 fit a GMM to this data which is first finding gaussian distributed clusters (sources) in this dataset
  and second allows us to predict the membership probability of an unseen datapoint to these sources :
<table>
    <tr>
    <td><img src="imgs/em-gmm_1.webp" alt="GMM"/></td>
    <td><img src="imgs/em-gmm_2.webp" alt="GMM"/></td>
    
    </tr>
</table>