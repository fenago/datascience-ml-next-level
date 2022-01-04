
Getting Started with PySpark
==============================

In this lab, we will work on PySpark. Start the spark shell by typing following command in the terminal: `pyspark`

The best way for us to understand Spark is to look at an example, as shown in the following screenshot:

```
lines = sc.textFile("/headless/Desktop/next-level-python-big-data/bigdata-with-pyspark/Lab01/data.txt")
lineLengths = lines.map(lambda s: len(s))
totalLength = lineLengths.reduce(lambda a, b: a + b)
totalLength
```

**Task:** Modify `data.txt` file, run above code again and verify that output (sum of total number of characters in text file) is correct.


![](./images/1.png)


In the preceding code, we have created a new variable called
[lines] by calling [SC.textFile (\"data.txt\")]. [sc]
is our Python objects that represent our Spark cluster. A Spark cluster
is a series of instances or cloud computers that store our Spark
processes. By calling a [textFile] constructor and feeding in
[data.text], we have potentially fed in a large text file and
created an RDD just using this one line. In other words, what we are
trying to do here is to feed a large text file into a distributed
cluster and Spark, and Spark handles this clustering for us.

In line two and line three, we have a MapReduce function. In line two,
we have mapped the length function using a [lambda] function to
each line of [data.text]. In line three, we have called a
reduction function to add all [lineLengths] together to produce
the total length of the documents. While Python\'s [lines] is a
variable that contains all the lines in [data.text], under the
hood, Spark is actually handling the distribution of fragments of
[data.text] in two different instances on the Spark cluster, and
is handling the MapReduce computation over all of these instances.



Spark SQL
=========

Let\'s look at how DataFrames can be used. The following code snippet is
a quick example of a DataFrame:

```
# spark is an existing SparkSession
df = spark.read.json("/headless/Desktop/next-level-python-big-data/bigdata-with-pyspark/Lab01/people.json")
# Displays the content of the DataFrame to stdout
df.show()

#+----+-------+
#| age| name|
#+----+-------+
#+null|Jackson|
#| 30| Martin|
#| 19| Melvin|
#+----|-------|
```


In the same way, as pandas or R would do, [read.json] allows us to
feed in some data from a JSON file, and [df.show] shows us the
contents of the DataFrame in a similar way to pandas.


Spark SQL can be used to execute SQL queries or
read data from any existing Hive insulation, where Hive is a database
implementation also from Apache. Spark SQL looks very similar to MySQL
or Postgres. The following code snippet is a good example:

```
#Register the DataFrame as a SQL temporary view
df.registerTempTable("people")

sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()

```

![](./images/2.png)


**Task:** Update the above query to select row where age is `30`.


Solution:

![](./images/3.png)


**Protip**

Open `http://localhost:4040/` in lab environment browser to view spark history:

![](./images/4.png)



SparkContext
============

Let\'s see how to set up a SparkContext:

1.  First, we need to import `SparkContext`.
2.  Create a new object in the [sc] variable standing for the
    SparkContext using the `SparkContext` constructor.
3.  In the `SparkContext` constructor, pass a [local]
    context. We are looking at `BigData PySpark` in this context,
    as follows:

```
from pyspark import SparkContext
sc = SparkContext('local', 'BigData PySpark')
```


4.  After we\'ve established this, all we need to do is then use
    [sc] as an entry point to our Spark operation, as demonstrated
    in the following code snippet:

```
visitors = [10, 3, 35, 25, 41, 9, 29]
df_visitors = sc.parallelize(visitors)
df_visitors_yearly = df_visitors.map(lambda x: x*365).collect()
print(df_visitors_yearly)
```


Let\'s take an example; if we were to analyze the synthetic datasets of
visitor counts to our clothing store, we might have a list of
[visitors] denoting the daily visitors to our store. We can then
create a parallelized version of the DataFrame, call
[sc.parallelize(visitors)], and feed in the [visitors]
datasets. [df\_visitors] then creates for us a DataFrame of
visitors. We can then map a function; for example, making the daily
numbers and extrapolating them into a yearly number by mapping a
[lambda] function that multiplies the daily number ([x]) by
[365], which is the number of days in a year. Then, we call a
[collect()] function to make sure that Spark executes on this
[lambda] call. Lastly, we print out [df\_ visitors\_yearly].


Spark shell
===========

Start our PySpark binary by typing `pyspark` in the terminal:

We can see that we\'ve started a shell session with Spark in the
following screenshot:


![](./images/ba96adf0-562b-47ec-9924-986c14b08156.png)



Spark is now available to us as a [spark] variable. Let\'s try a
simple thing in Spark. The first thing to do is to load a random file.
Let\'s load `README.md` file into our memory as follows:

```
text_file = spark.read.text("/headless/Desktop/next-level-python-big-data/bigdata-with-pyspark/Lab01/README.md")
```

If we use [spark.read.text] and then put in [README.md], we
get a few warnings, but we shouldn\'t be too concerned about that at the
moment, as we will see later how we are going to fix these things. The
main thing here is that we can use Python syntax to access Spark.

What we have done here is put [README.md] as text data read by
[spark] into Spark, and we can use [text\_file.count()] can
get Spark to count how many characters are in our text file as follows:

```
text_file.count()
```


From this, we get the following output:

```
109
```


We can also see what the first line is with the following:

```
text_file.first()
```


We will get the following output:

```
Row(value='# Apache Spark')
```


We can now count a number of lines that contain the word [Spark]
by doing the following:

```
lines_with_spark = text_file.filter(text_file.value.contains("Spark"))
```


Here, we have filtered for lines using the [filter()] function,
and within the [filter()] function, we have specified that
[text\_file\_value.contains] includes the word [\"Spark\"],
and we have put those results into the [lines\_with\_spark]
variable.

We can modify the preceding command and simply add [.count()], as
follows:

```
text_file.filter(text_file.value.contains("Spark")).count()
```


We will now get the following output:

```
20
```


We can see that [20] lines in the text file contain the word
[Spark]. This is just a simple example of how we can use the Spark
shell.
