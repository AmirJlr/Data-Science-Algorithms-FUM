<h1>Google Page Rank</h1>

<img src="imgs/pr1.jpg" alt="page rank">

<p>PageRank (PR) is an algorithm used by Google Search to rank websites in their search engine results.</p>

<b>PageRank works by counting the number and quality of links to a page to determine a rough estimate of how important the website is.
     The underlying assumption is that more important websites are likely to receive more links from other websites.</b>


<h2>Algorithm </h2>

<p>
    The PageRank algorithm outputs a <b>probability distribution</b> used to represent the likelihood that
    a person randomly clicking on links will arrive at any particular page.
    It is assumed in several research papers that the distribution is evenly divided among
    all documents in the collection at the beginning of the computational process. 
    The PageRank computations require several passes, called “iterations”, 
    through the collection to adjust approximate PageRank values to more closely reflect the theoretical true value.
</p>

<h2>Simplified algorithm</h2>

<p>
    Assume a small universe of four web pages: A, B, C, and D. 
    Links from a page to itself, 
    or multiple outbound links from one single page to another single page, are ignored. 
    PageRank is initialized to the same value for all pages. 
    In the original form of PageRank, the sum of PageRank over all pages was the total number of pages on the web at that time, 
    so each page in this example would have an initial value of 1. 
    However, later versions of PageRank, and the remainder of this section, assume a probability distribution between 0 and 1. 
    Hence the initial value for each page in this example is 0.25.
</p>

<p>
    The PageRank transferred from a given page to the targets of its outbound links upon the next iteration is
    divided equally among all outbound links.
    If the only links in the system were from pages B, C, and D to A, 
    each link would transfer 0.25 PageRank to A upon the next iteration, for a total of 0.75.
</p>

<img src="imgs/1.svg" alt="page rank">

<p>Suppose instead that page B had a link to pages C and A, page C had a link to page A, 
    and page D had links to all three pages. 
    Thus, upon the first iteration,
     page B would transfer half of its existing value, or 0.125, 
     to page A and the other half, or 0.125, to page C. 
     Page C would transfer all of its existing value, 0.25, to the only page it links to, A. 
     Since D had three outbound links, it would transfer one-third of its existing value, or approximately 0.083, to A. 
     At the completion of this iteration, page A will have a PageRank of approximately 0.458.
</p>

<img src="imgs/2.svg" alt="page rank">

<p>
    In other words, the PageRank conferred by an outbound link is equal to
        the document’s own PageRank score divided by the number of outbound links L( ).
</p>
    
<img src="imgs/3.svg" alt="page rank">

<p>
    In the general case, the PageRank value for any page u can be expressed as:
</p>

<img src="imgs/4.svg" alt="page rank">

<p>
    i.e. the PageRank value for a page u is dependent on the PageRank values for each page v contained in the set Bu 
    (the set containing all pages linking to page u), divided by the number L(v) of links from page v. 
    The algorithm involves a damping factor for the calculation of the PageRank. 
    It is like the income tax which the govt extracts from one despite paying him itself.
</p>

