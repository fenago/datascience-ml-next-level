
Getting Your Big Data into the Spark Environment Using RDDs
===========================================================

In this lab, we will cover the following topics:

-   Loading data onto Spark RDDs
-   Parallelization with Spark RDDs
-   Basics of RDD operation

#### Pre-reqs:
- Google Chrome (Recommended)

#### Lab Environment
Notebooks are ready to run. All packages have been installed. There is no requirement for any setup.

All examples are present in `~/Desktop/next-level-python-big-data/bigdata-with-pyspark/Lab02` folder. 


Loading data on to Spark RDDs
=============================

In this section, we are going to look at loading data on to Spark RDDs,
and will cover the following topics:

-   The UCI machine learning data repository
-   Getting data from the repository to Python
-   Getting data into Spark

Let\'s start with an overview of the UCI machine learning data
repository.

### Start SparkShell
Start the spark shell by typing following command in the terminal: 

```
cd ~/Desktop/next-level-python-big-data/bigdata-with-pyspark/Lab02

pyspark
```

**Note:** Jupyter Notebook can be used as well instead of spark shell. `Lab_2.ipynb` is already present in Lab02 directory. 


The UCI machine learning repository
===================================

We can access the UCI machine learning repository.
Let\'s take a look at the KDD Cup 1999 dataset, which we will download,
and then we will load the whole dataset into PySpark.

https://archive.ics.uci.edu/ml/machine-learning-databases/kddcup99-mld


![](./images/e7fb27a2-161d-4d0a-bddf-1955206aab1d.png)

**Note:** Dataset is already downloaded. Let's load it in PySpark:

Load this using `SparkContext`. So, `SparkContext`
is materialized or objectified in Python as the [sc] variable as follows:

```
sc
```


This output is as demonstrated in the following code snippet:

```
< SparkContext master=local[*] appName=PySparkShell?
```




Getting data into Spark
=======================

1.  Next, load the KDD cup data into PySpark using [sc], as shown
    in the following command:

```
raw_data = sc.textFile("./kddcup.data.gz")
```


2.  In the following command, we can see that the raw data is now in the
    [raw\_data] variable:

```
raw_data
```


This output is as demonstrated in the following code snippet:

```
./kddcup.data,gz MapPartitionsRDD[3] at textFile at NativeMethodAccessorImpl.java:0
```


If we enter the [raw\_data] variable, it gives us details
regarding [kddcup.data.gz], where raw data underlying the data
file is located, and tells us about [MapPartitionsRDD.]

Now that we know how to load the data into Spark, let\'s learn about
parallelization with Spark RDDs.


Parallelization with Spark RDDs
===============================

Let\'s look at how we can do this. Let\'s first assume that our data is
already in Python, and so, for demonstration purposes, we are going to
create a Python list of a hundred numbers as follows:

```
a = range(100)
a
```


This gives us the following output:

```
range(0, 100)
```


For example, if we look at [a], it is simply a list of 100
numbers. If we convert this into a [list], it will show us the
list of 100 numbers:

```
list (a)
```


This gives us the following output:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
...
```


The following command shows us how to turn this into an RDD:

```
list_rdd = sc.parallelize(a)
```


If we look at what [list\_rdd] contains, we can see that it is
[PythonRDD.scala:52], so, this tells us that the Scala-backed
PySpark instance has recognized this as a Python-created RDD, as
follows:

```
list_rdd
```


This gives us the following output:

```
PythonRDD[3] at RDD at PythonRDD.scala:52
```


Now, let\'s look at what we can do with this list. The first thing we
can do is count how many elements are present in [list\_rdd] by
using the following command:

```
list_rdd.count()
```


This gives us the following output:

```
100
```


We can see that [list\_rdd] is counted at 100. If we run it again
without cutting through into the results, we can actually see that,
since Scala is running in a real time when going through the RDD, it is
slower than just running the length of [a], which is instant.

However, RDD takes some time, because it needs time to go through the
parallelized version of the list. So, at small scales, where there are
only a hundred numbers, it might not be very helpful to have this
trade-off, but with larger amounts of data and larger individual sizes
of the elements of the data, it will make a lot more sense.

We can also take an arbitrary amount of elements from the list, as
follows:

```
list_rdd.take(10)
```


This gives us the following output:

```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


When we run the preceding command, we can see that PySpark has performed
some calculations before returning the first ten elements of the list.
Notice that all of this is now backed by PySpark, and we are using
Spark\'s power to manipulate this list of 100 items.

Let\'s now use the reduce function in [list\_rdd], or in RDDs in
general, to demonstrate what we can do with PySpark\'s RDDs. We will
apply two parameter functions as an anonymous [lambda] function to
the `reduce` call as follows:

```
list_rdd.reduce(lambda a, b: a+b)
```


Here, [lambda] takes two parameters, [a] and [b]. It
simply adds these two numbers together, hence [a+b], and returns
the output. With the RDD `reduce` call, we can sequentially add
the first two numbers of RDD lists together, return the results, and
then add the third number to the results, and so on. So, eventually, you
add all 100 numbers to the same results by using `reduce`.

Now, after some work through the distributed database, we can now see
that adding numbers from [0] to [99] gives us [4950],
and it is all done using PySpark\'s RDD methodology.

Basics of RDD operation
=======================

Go back to the PySpark Terminal; we
have already loaded our raw data as a text file, as we have seen in
previous labs.

We will write a [filter] function to find all the lines to
indicate RDD data, where each line [contains] the word
[normal], as seen in the following screenshot:

```
contains_normal = raw_data.filter(lambda line: "normal." in line)

contains_normal.count()
```


Let\'s analyze what this means. Firstly, we are calling the
[filter] function for the RDD raw data, and we\'re feeding it an
anonymous [lambda] function that takes one [line] parameter
and returns the predicates, as we have read in the documentation, on
whether or not the word [normal] exists in the line. At this
moment, as we have discussed in the previous labs, we haven\'t
actually computed this [filter] operation. What we need to do is
call a function that actually consolidates the data and forces Spark to
calculate something. In this case, we can count on
[contains\_normal], as demonstrated in the following screenshot:


![](./images/67a5b615-fcae-4356-99da-0bf6b0e22232.png)


For the second example, we will use the map. Since we downloaded the KDD
cup data, we know that it is a comma-separated value file, and so, one
of the very easy things for us to do is to split each line by two
commas, as follows:

```
split_file = raw_data.map(lambda line: line.split(","))

split_file.take(5)
```


Let\'s analyze what is happening. We call the `map` function on
[raw\_data]. We feed it an anonymous [lambda] function
called [line], where we are splitting the [line] function by
using [,]. The result is a split file. Now, here the power of
Spark really comes into play. Recall that, in the
[contains\_normal.] filter, when we called a function that forced
Spark to calculate [count], it took us a few minutes to come up
with the correct results. If we perform the `map` function, it is
going to have the same effect, because there are going to be millions of
lines of data that we need to map through. And so, one of the ways to
quickly preview whether our mapping function runs correctly is if we can
materialize a few lines instead of the whole file.

To do this, we can use the [take] function that we have used
before, as demonstrated in the following screenshot:


![](./images/e99a6e8a-4409-4b4e-b1e1-858e278abc2d.png)


Summary
=======

In this lab, we learned how to load data on Spark RDDs and also
covered parallelization with Spark RDDs. We had an
overview of the basic RDD operations, and also checked the functions
from the official documentation.

In the next lab, we will cover big data cleaning and data wrangling.
