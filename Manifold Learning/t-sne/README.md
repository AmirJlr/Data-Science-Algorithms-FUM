# t-SNE

## What is t-SNE?
(t-SNE) t-Distributed Stochastic Neighbor Embedding is a non-linear dimensionality reduction algorithm used for exploring high-dimensional data. It maps multi-dimensional data to two or more dimensions suitable for human observation. With help of the t-SNE algorithms, you may have to plot fewer exploratory data analysis plots next time you work with high dimensional data.

## Limitations of PCA
PCA is a linear algorithm. It will not be able to interpret complex polynomial relationship between features. On the other hand, t-SNE is based on probability distributions with random walk on neighborhood graphs to find the structure within the data.

## What does t-SNE actually do?
t-SNE a non-linear dimensionality reduction algorithm finds patterns in the data by identifying observed clusters based on similarity of data points with multiple features. But it is not a clustering algorithm it is a dimensionality reduction algorithm. This is because it maps the multi-dimensional data to a lower dimensional space, the input features are no longer identifiable. Thus you cannot make any inference based only on the output of t-SNE. So essentially it is mainly a data exploration and visualization technique.

## Use cases
t-SNE can be used on almost all high dimensional data sets. But it is extensively applied in Image processing, NLP, genomic data and speech processing.

## PCA vs t-SNE :
<table>
    <tr>
        <td><img src="imgs/pc vs tsne1.png" alt="tsne"/></td>
        <td><img src="imgs/pc vs tsne2.png" alt="tsne"/></td>
    </tr>
</table>

<table>
    <tr>
        <td><img src="imgs/pc vs tsne3.png" alt="tsne"/></td>
        <td><img src="imgs/pc vs tsne4.png" alt="tsne"/></td>
    </tr>
</table>
