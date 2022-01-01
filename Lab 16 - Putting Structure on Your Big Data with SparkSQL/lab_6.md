
Putting Structure on Your Big Data with SparkSQL
================================================

In particular, we will cover the following topics:

-   Manipulating DataFrames with Spark SQL schemas
-   Using Spark DSL to build queries


Manipulating DataFrames with Spark SQL schemas
==============================================

In this section, we will learn more about DataFrames and learn how to
use Spark SQL.

Let\'s take a look at the code that we will be using in our Jupyter
Notebook. To maintain consistency, we will be using the same KDD cup
data:

1.  We will first type [textFile] into a [raw\_data]
    variable as follows:

```
raw_data = sc.textFile("./kddcup.data.gz")
```


2.  What\'s new here is that we are importing two new packages from
    [pyspark.sql]:
    -   [Row]
    -   `SQLContext`
3.  The following code shows us how to import these packages:

```
from pyspark.sql import Row, SQLContext
sql_context = SQLContext(sc)
csv = raw_data.map(lambda l: l.split(","))
```


Using `SQLContext`, we create a new [sql\_context] variable
that holds the object of the `SQLContext` variable created by
PySpark. As we\'re using `SparkContext` to start this
`SQLContext` variable, we need to pipe in [sc] as the first
parameter of the `SQLContext` creator. After this, we need to take
our [raw\_data] variable and map it with the [l.split]
lambda function to create an object that holds our **comma-separated
values** (**CSV**).

4.  We\'ll leverage our new important [Row] objects to create a
    new object that has defined labels. This is to label our datasets by
    what feature we are looking at, as follows:

```
rows = csv.map(lambda p: Row(duration=int(p[0]), protocol=p[1], service=p[2]))
```


In the preceding code, we\'ve taken our comma-separated values
([csv]), and we\'ve created a [Row] object that takes the
first feature, called [duration]; the second feature, called
[protocol]; and the third feature, called [service]. This
directly corresponds to our labels in the actual datasets.

5.  Now, we can create a new DataFrame by calling the
    [createDataFrame] function in our [sql\_context]
    variable. To create this DataFrame, we need to feed in our row data
    objects, and the resulting object would be a DataFrame in
    [df]. After this, we need to register a temporary table. Here,
    we are just calling it [rdd]. By doing this, we can now use
    ordinary SQL syntax to query the content in this temporary table
    that is constructed by our rows:

```
df = sql_context.createDataFrame(rows)
df.registerTempTable("rdd")
```


6.  In our example, we need to select the duration from [rdd],
    which is a temporary table. The protocol we have selected here is
    equal to [\'tcp\'], and the duration, which is our first
    feature in a row, is larger than [2000], as demonstrated in
    the following code snippet:

```
sql_context.sql("""SELECT duration FROM rdd WHERE protocol = 'tcp' AND duration > 2000""")
```


7.  Now, when we call the [show] function, it gives us every
    single data point that matches these criteria:

```
sql_context.sql("""SELECT duration FROM rdd WHERE protocol = 'tcp' AND duration > 2000""").show()
```


8.  We will then get the following output:

```
+--------+
|duration|
+--------+
|   12454|
|   10774|
|   13368|
|   10350|
|   10409|
|   14918|
|   10039|
|   15127|
|   25602|
|   13120|
|    2399|
|    6155|
|   11155|
|   12169|
|   15239|
|   10901|
|   15182|
|    9494|
|    7895|
|   11084|
+--------+
only showing top 20 rows
```

Using the preceding example, we can infer that we can use the
`SQLContext` variable from the PySpark package to package our data
in a SQL friendly format.


Using Spark DSL to build queries
================================

In this section, we will use Spark DSL to build queries for structured
data operations:

1.  In the following command, we have used the same query as used
    earlier; this time expressed in the Spark DSL to illustrate and
    compare how using the Spark DSL is different, but achieves the same
    goal as our SQL is shown in the previous section:

```
df.select("duration").filter(df.duration>2000).filter(df.protocol=="tcp").show()
```


In this command, we first take the [df] object that we created in
the previous section. We then select the duration by calling the
[select] function and feeding in the [duration] parameter.

2.  Next, in the preceding code snippet, we call the [filter]
    function twice, first by using [df.duration], and the second
    time by using [df.protocol]. In the first instance, we are
    trying to see whether the duration is larger than [2000], and
    in the second instance, we are trying to see whether the protocol is
    equal to [\"tcp\"]. We also need to append the [show]
    function at the very end of the command to get the same results, as
    shown in the following code block:

```
+--------+
|duration|
+--------+
|   12454|
|   10774|
|   13368|
|   10350|
|   10409|
|   14918|
|   10039|
|   15127|
|   25602|
|   13120|
|    2399|
|    6155|
|   11155|
|   12169|
|   15239|
|   10901|
|   15182|
|    9494|
|    7895|
|   11084|
+--------+
only showing top 20 rows
```


Here, we have the top 20 rows of the data points again that fit the
description of the code used to get this result.

Summary
=======

In this lab, we covered Spark DSL and learned how to build queries.
We also learned how to manipulate DataFrames with Spark SQL schemas, and
then we used Spark DSL to build queries for structured data operations.