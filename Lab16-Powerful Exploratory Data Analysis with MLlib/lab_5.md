
Powerful Exploratory Data Analysis with MLlib
=============================================

We will cover the following topics:

-   Computing summary statistics with MLlib
-   Using the Pearson and Spearman methods to discover correlations
-   Testing our hypotheses on large datasets


Computing summary statistics with MLlib
=======================================

Let\'s look at the code in the Jupyter Notebook
for this lab in [Lab_5.ipynb]. We will first collect the
data from the [kddcup.data.gz] text file and pipe this into the
[raw\_data] variable as follows:

```
raw_data = sc.textFile("./kddcup.data.gz")
```


The [kddcup.data] file is a **comma-separated value** (**CSV**)
file. We have to split this data by the [,] character and put it
in the [csv] variable as follows:

```
csv = raw_data.map(lambda x: x.split(","))
```


Let\'s take the first feature [x\[0\]] of the data file; this
feature represents the [duration], that is, aspects of the data.
We will transform it into an integer here, and also wrap it in a list as
follows:

```
duration = csv.map(lambda x: [int(x[0])])
```


This helps us do summary statistics over multiple variables, and not
just one of them. To activate the [colStats] function, we need to
import the [Statistics] package, as shown in the following
snippet:

```
from pyspark.mllib.stat import Statistics
```


This [Statistics] package is a sub package of
[pyspark.mllib.stat]. Now, we need to call the [colStats]
function in the [Statistics] package and feed it some data. Here,
we are talking about the [duration] data from the dataset and
we\'re feeding the summary statistics into the [summary] variable:

```
summary = Statistics.colStats(duration)
```


To access different summary statistics, such as the mean, standard
deviation, and so on, we can call the functions of the [summary]
objects, and access different summary statistics. For example, we can
access the [mean], and since we have only one feature in our
[duration] dataset, we can index it by the [00] index, and
we\'ll get the mean of the dataset as follows:

```
summary.mean()[0]
```


This will give us the following output:

```
47.97930249928637
```


Similarly, if we import the [sqrt] function from the Python
standard library, we can create the standard deviation of the durations
seen in the datasets, as demonstrated in the following code snippet:

```
from math import sqrt
sqrt(summary.variance()[0])
```


This will give us the following output:

```
707.746472305374
```


If we don\'t index the summary statistics with [\[0\]], we can see
that [summary.max()] and [summary.min()] gives us back an
array, of which the first element is the summary statistic that we
desire, as shown in the following code snippet:

```
summary.max()
array ([58329.]) #output
summary.min()
array([0.]) #output
```



Computing Pearson and Spearman correlations
===========================================

To understand this, let\'s assume that we are taking the first three
numeric variables from our dataset. For this, we want to access the
[csv] variable that we defined previously, where we simply split
[raw\_data] using a comma ([,]). We will consider only the
first three columns that are numeric. We will not take anything that
contains words; we\'re only interested in features that are purely based
on numbers. In our case, in [kddcup.data], the first feature is
indexed at [0]; feature 5 and feature 6 are indexed at [4]
and [5], respectively which are the numeric variables that we
have. We use a [lambda] function to take all three of these into a
list and put it into the [metrics] variable:

```
metrics = csv.map(lambda x: [x[0], x[4], x[5]])
Statistics.corr(metrics, method="spearman")
```


This will give us the following output:

```
array([[1. , 0.01419628, 0.29918926],
[0.01419628, 1. , -0.16793059],
[0.29918926, -0.16793059, 1. ]])
```


In the *Computing summary statistics with MLlib* section, we simply took
the first feature into a list and created a list with a length of one.
Here, we\'re taking three quantities of three variables into the same
list. Now, each list has a length of three.

To compute the correlations, we call the [corr] method on the
[metrics] variable and specify the [method] as
[\"spearman\"]. PySpark would give us a very simple matrix telling
us the correlation between the variables. In our example, the third
variable in our [metrics] variable is more correlated than the
second variable.


Testing our hypotheses on large datasets
========================================

Let\'s start by importing the
[Vectors] package from [pyspark.mllib.linalg]. Using this
vector, we\'re going to create a dense vector of the visitor frequencies
by day in our store.

Let\'s imagine that the frequencies go from [0.13] an hour to
[0.61], [0.8], and [0.5], finally ending on Friday at
[0.3]. So, we are putting these visitor frequencies into the
[visitors\_freq] variable. Since we\'re using PySpark, it is very
simple for us to run a chi-square test from the [Statistics]
package, which we have already imported as follows:

```
from pyspark.mllib.linalg import Vectors
visitors_freq = Vectors.dense(0.13, 0.61, 0.8, 0.5, 0.3)
print(Statistics.chiSqTest(visitors_freq))
```


By running the chi-square test, the [visitors\_freq] variable
gives us a bunch of useful information, as demonstrated in the following
screenshot:


![](./images/ec0a248d-d599-476c-bbd7-665a504a76bc.png)



The preceding output shows the chi-square test summary. We\'ve used the
[pearson] method, where there are [4] degrees of freedom in
our Pearson chi-square test, and the statistics are [0.585], which
means that the [pValue] is [0.964]. This results in no
presumption against the null hypothesis. In this way, the observed data
follows the same distribution as expected, which means our visitors are
not actually different. This gives us a good understanding of hypothesis
testing.

Summary
=======

In this lab, we learned summary statistics and computing the summary
statistics with MLlib. We also learned about Pearson and Spearman
correlations, and how we can discover these correlations in our datasets
using PySpark. Finally, we learned one particular way of performing
hypothesis testing, which is called the Pearson chi-square test. We then
used PySpark\'s hypothesis-testing functions to test our hypotheses on
large datasets.

In the next lab, we\'re going to look at putting the structure on
our big data with Spark SQL.
