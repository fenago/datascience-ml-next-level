
Lab 5: The DataFrame object
===========================

### This lab covers:

- Instantiating a `DataFrame` object from a dictionary and a numpy `ndarray`
- Importing a multidimensional dataset with the `read_csv` method
- Sorting one or more columns in a `DataFrame`
- Accessing rows and columns from a `DataFrame`
- Setting and resetting the index of a `DataFrame`
- Renaming column and index values


#### Creating A DataFrame from a Dictionary

Let\'s begin by importing `Pandas`. We\'ll also be using the
NumPy library for some random data generation. It is commonly assigned
the alias `np`.



```
In  [1] import pandas as pd
        import numpy as np
```


The following example below uses three equal-sized lists to store cities,
countries, and populations. You\'re welcome to substitute other iterable
objects like tuples or `Series` in place of the lists. The `DataFrame`
class is available as a top-level attribute on the `pandas` library. Its
first parameter, `data`, represents the data source.



```
In  [2] city_data = {
            "City": ["New York City", "Paris", "Barcelona", "Rome"],
            "Country": ["United States", "France", "Spain", "Italy"],
            "Population": [8600000, 2141000, 5515000, 2873000]
        }
 
        cities = pd.DataFrame(city_data)
        cities
 
Out [2]
 
            City         Country   Population
0  New York City   United States      8600000
1          Paris          France      2141000
2      Barcelona           Spain      5515000
3           Rome           Italy      2873000
```


What if we wanted the data flipped around, with our column headers
serving as the index labels? There are a few options available here. On
our existing `DataFrame`, we can either invoke the `transpose` method or
access its `T` attribute.



```
In  [3] cities.transpose() # is the same as
        cities.T
 
Out [3]
 
                        0        1          2        3
City        New York City    Paris  Barcelona     Rome
Country     United States   France      Spain    Italy
Population        8600000  2141000    5515000  2873000
```




The `DataFrame` class also includes a convenient `from_dict` class
method. This utility method only accepts a dictionary for its `data`
parameter, which saves `Pandas` some extra calculations. The method\'s
`orient` parameter can be passed an argument of `"index"` to orient the
headers as index labels.



```
In  [4] pd.DataFrame.from_dict(data = city_data, orient = "index")
 
Out [4]
 
                        0        1          2        3
City        New York City    Paris  Barcelona     Rome
Country     United States   France      Spain    Italy
Population        8600000  2141000    5515000  2873000
```




#### Creating A DataFrame from a Numpy ndarray



The `DataFrame` constructor also accepts a NumPy `ndarray` object.
Let\'s say we want to create a 3x5 `DataFrame` of integers between 1 and
100 (inclusive). We can begin by using the `randint` function on its
`random` module to create our data.



```
In  [5] data = np.random.randint(1, 101, [3, 5])
        data
 
Out [5] array([[25, 22, 80, 43, 42],
              [40, 89,  7, 21, 25],
              [89, 71, 32, 28, 39]])
```




Next, we pass our `ndarray` into the `DataFrame` constructor. Just like
with the rows, `Pandas` will assign each column a numeric index if a set
of custom column headers is not provided.



```
In  [6] pd.DataFrame(data = data)
 
Out [6]
 
    0   1   2   3   4
0  25  22  80  43  42
1  40  89   7  21  25
2  89  71  32  28  39
```




We can pass the `index` parameter an iterable sequence like a list,
tuple, or `ndarray` to serve as the row labels. Note that the length of
the iterable must be equal to the number of rows in the dataset. This is
a 3x5 table, so we must provide 3 labels for the indices.



```
In  [7] index = ["Morning", "Afternoon", "Evening"]
        temperatures = pd.DataFrame(data = data, index = index)
        temperatures
 
Out [7]
 
            0   1   2   3   4
Morning    25  22  80  43  42
Afternoon  40  89   7  21  25
Evening    89  71  32  28  39
```




The `columns` parameter allows us to set the names of the columns (aka
the vertical labels) in the `DataFrame`. Because we have 5 total
columns, the length of our iterable must be 5. The example below varies
things up by storing the headers in a tuple.



```
In  [8] index = ["Morning", "Afternoon", "Evening"]
        columns = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
        temperatures = pd.DataFrame(data = data,
                                    index = index,
                                    columns = columns)
        temperatures
 
Out [8]
 
           Monday  Tuesday  Wednesday  Thursday  Friday
Morning        25       22         80        43      42
Afternoon      40       89          7        21      25
Evening        89       71         32        28      39
 
Both the row and column indices are allowed to contain duplicates.
 
In  [9] index = ["Morning", "Afternoon", "Morning"]
        columns = ["Monday", "Tuesday", "Wednesday", "Tuesday", "Friday"]
        pd.DataFrame(data = data, index = index, columns = columns)
 
Out [9]
 
           Monday  Tuesday  Wednesday  Tuesday  Friday
Morning        25       22         80       43      42
Afternoon      40       89          7       21      25
Morning        89       71         32       28      39
```




Similarities between Series and DataFrames
------------------------------------------------

Many of the `Series` attributes and methods introduced in the previous
labs are also available on a `DataFrame`. Of course, the
implementations of them are often different; we\'re dealing with
multiple columns now! Let\'s import our first dataset to try them out!


#### Importing a CSV File with the read\_csv Method


The `nba.csv` file is a list of professional basketball players in the
National Basketball Association for the 2019-2020 season. The dataset
includes each player\'s name, team, position, birthday, and salary.



```
In  [10] pd.read_csv("nba.csv")
 
Out [10]
 
               Name                 Team    Position  Birthday     Salary
0      Shake Milton   Philadelphia 76ers          SG   9/26/96    1445697
1    Christian Wood      Detroit Pistons          PF   9/27/95    1645357
2     PJ Washington    Charlotte Hornets          PF   8/23/98    3831840
3      Derrick Rose      Detroit Pistons          PG   10/4/88    7317074
4     Marial Shayok   Philadelphia 76ers           G   7/26/95      79568
  …               …                    …           …         …          …
445   Austin Rivers      Houston Rockets          PG    8/1/92    2174310
446     Harry Giles     Sacramento Kings          PF   4/22/98    2578800
447     Robin Lopez      Milwaukee Bucks           C    4/1/88    4767000
448   Collin Sexton  Cleveland Cavaliers          PG    1/4/99    4764960
449     Ricky Rubio         Phoenix Suns          PG  10/21/90   16200000
 
450 rows x 5 columns
```




There\'s one important optimization we can make here. The values in the
**Birthday** column are imported as strings rather than as datetime
objects, which limits the number of operations we can perform on them.
Let\'s use the `parse_dates` parameter to coerce the values into the
more appropriate type. Datetimes will be displayed in a consistent
YYYY-MM-DD format.



```
In  [11] pd.read_csv("nba.csv", parse_dates = ["Birthday"])
 
Out [11]
 
               Name                 Team Position   Birthday    Salary
0      Shake Milton   Philadelphia 76ers       SG 1996-09-26   1445697
1    Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
2     PJ Washington    Charlotte Hornets       PF 1998-08-23   3831840
3      Derrick Rose      Detroit Pistons       PG 1988-10-04   7317074
4     Marial Shayok   Philadelphia 76ers        G 1995-07-26     79568
…                 …                    …        …          …         …
445   Austin Rivers      Houston Rockets       PG 1992-08-01   2174310
446     Harry Giles     Sacramento Kings       PF 1998-04-22   2578800
447     Robin Lopez      Milwaukee Bucks        C 1988-04-01   4767000
448   Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
449     Ricky Rubio         Phoenix Suns       PG 1990-10-21  16200000
 
450 rows x 5 columns
```




Much better! We can assign the `DataFrame` to a `nba` variable and get
to work.



```
In  [12] nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
```




#### Shared and Exclusive Attributes between Series and DataFrames



The values in a `Series` must be of a single homogenous data type. In
comparison, the columns in a `DataFrame` are more likely to hold
heterogenous (i.e. varied) data. Let\'s try accessing our trusty
`dtypes` attribute on `nba`. It will return a `Series` object with the
`DataFrame` \'s columns and their respective data types. As a reminder,
`object` is internal `pandas` lingo for strings.



```
In  [13] nba.dtypes
 
Out [13] Name                object
         Team                object
         Position            object
         Birthday    datetime64[ns]
         Salary               int64
         dtype: object
```




We can count the number of columns with each data type by invoking the
`value_counts` method on the resulting `Series`.



```
In  [14] nba.dtypes.value_counts()
 
Out [14] object            3
         datetime64[ns]    1
         int64             1
         dtype: int64
```




A `DataFrame` is fundamentally composed of two objects: an index
consisting of row labels and a data container that holds each row\'s
values. `Pandas` ships with several index objects, each of which is
optimized to store values of a specific type (numeric, string, datetime,
etc.). The `index` attribute returns the underlying Index object for a
`DataFrame`. Let\'s take a look at what kind of index `Pandas` is using
for our `nba` dataset.



```
In  [15] nba.index
 
Out [15] RangeIndex(start=0, stop=450, step=1)
```


What about the data itself? We can access the NumPy `ndarray` holding
the values through the `DataFrame`\'s values attribute.



```
In  [16] nba.values
 
Out [16] array([['Shake Milton', 'Philadelphia 76ers', 'SG',
                 Timestamp('1996-09-26 00:00:00'), 1445697],
                ['Christian Wood', 'Detroit Pistons', 'PF',
                 Timestamp('1995-09-27 00:00:00'), 1645357],
                ['PJ Washington', 'Charlotte Hornets', 'PF',
                 Timestamp('1998-08-23 00:00:00'), 3831840],
                ...,
                ['Robin Lopez', 'Milwaukee Bucks', 'C',
                 Timestamp('1988-04-01 00:00:00'), 4767000],
                ['Collin Sexton', 'Cleveland Cavaliers', 'PG',
                 Timestamp('1999-01-04 00:00:00'), 4764960],
                ['Ricky Rubio', 'Phoenix Suns', 'PG',
                 Timestamp('1990-10-21 00:00:00'), 16200000]],  
                 dtype=object)
```




The `DataFrame` also has an exclusive `columns` attribute which returns
an `Index` object containing the headers.



```
In  [17] nba.columns
 
Out [17] Index(['Name', 'Team', 'Position', 'Birthday', 'Salary'],   
         dtype='object'
```




Both the horizontal and vertical indices are collected in a list
referenced by the `axes` attribute.



```
In  [18] nba.axes
 
Out [18] [RangeIndex(start=0, stop=450, step=1),
          Index(['Name', 'Team', 'Position', 'Birthday', 'Salary'],          
          dtype='object')]
```




The `shape` attribute returns a tuple with the dimensions of the
`DataFrame`. This one has 450 rows by 5 columns.



```
In  [19] nba.shape
 
Out [19] (450, 5)
 
The ndim attribute returns the number of dimensions.
 
In  [20] nba.ndim
 
Out [20] 2
```




The `size` attribute calculates the total number of values in the
dataset, including missing ones. It will be equal to the product of the
number of rows and the number of columns.



```
In  [21] nba.size
 
Out [21] 2250
 
In  [22] len(nba.index) * len(nba.columns)
 
Out [22] 2250
```




If we want to *exclude* missing values, the `count` method returns a
`Series` with the number of non-null values per `DataFrame` column. The
values can be added together with the sum method to arrive at the total
number of non-null values in the `DataFrame`. This dataset holds no
missing values, so the results from the `size` attribute and the `count`
method will be the same.



```
In  [23] nba.count()
 
Out [23] Name        450
         Team        450
         Position    450
         Birthday    450
         Salary      450
         dtype: int64
 
In  [24] nba.count().sum()
 
Out [24] 2250
```




#### Shared Methods between Series and DataFrames



We can extract any number of rows from the top or bottom of the dataset
with the `head` and `tail` methods.



```
In  [25] nba.head(2)
 
Out [25]
 
             Name                Team Position   Birthday   Salary
0    Shake Milton  Philadelphia 76ers       SG 1996-09-26  1445697
1  Christian Wood     Detroit Pistons       PF 1995-09-27  1645357
 
In  [26] nba.tail(n = 3)
 
Out [26]
 
              Name                 Team Position   Birthday    Salary
447    Robin Lopez      Milwaukee Bucks        C 1988-04-01   4767000
448  Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
449    Ricky Rubio         Phoenix Suns       PG 1990-10-21  16200000
```




The `sample` method extracts a number of random rows from the
`DataFrame`.



```
In  [27] nba.sample(3)
 
Out [27]
 
                                    Team Position   Birthday    Salary
Name                                                                 
Al Horford            Philadelphia 76ers        C 1986-06-03  28000000
Tristan Thompson     Cleveland Cavaliers        C 1991-03-13  18539130
Jusuf Nurkic      Portland Trail Blazers        C 1994-08-23  12000000
```




Let\'s say we wanted to find out how many different teams, salaries and
positions existed in this dataset. The `nunique` method returns a
`Series` object with a count of unique values found in *each* column.



```
In  [28] nba.nunique()
 
Out [28] Name        450
         Team         30
         Position      9
         Birthday    430
         Salary      269
         dtype: int64
```




You may also recall the `max` and `min` methods. On a `DataFrame`, they
will return a `Series` holding the maximum and minimum values of *each*
column. The maximum value for a datetime column will be the latest date
in chronological order.



```
In  [29] nba.max()
 
Out [29] Team         Washington Wizards
         Position                     SG
         Birthday    2000-12-23 00:00:00
         Salary                 40231758
         dtype: object
 
In  [30] nba.min()
 
Out [30] Team              Atlanta Hawks
         Position                      C
         Birthday    1977-01-26 00:00:00
         Salary                    79568
         dtype: object
```




What if we wanted to expand our results to find the four highest-paid
players in the NBA? The `nlargest` method retrieves a subset of rows
where a given column has the largest values in the dataset. Because a
`DataFrame` can contain multiple sortable columns, we have to use the
`columns` parameter to specify which column(s) to use as the basis for
sorting. The argument can be either a string or a list of strings
representing column names.



```
In  [31] nba.nlargest(n = 4, columns = "Birthday")
 
Out [31]
 
                  Name                   Team Position   Birthday    Salary
205      Stephen Curry  Golden State Warriors       PG 1988-03-14  40231758
38          Chris Paul  Oklahoma City Thunder       PG 1985-05-06  38506482
219  Russell Westbrook        Houston Rockets       PG 1988-11-12  38506482
251          John Wall     Washington Wizards       PG 1990-09-06  38199000
```




Our next challenge: let\'s find the 3 oldest players in the league. The
`nsmallest` method can help us here; it returns a subset of rows in
which a given column has the smallest values in the dataset. The
smallest datetime values are those occur the earliest in chronological
order.



```
In  [32] nba.nsmallest(3, columns = ["Birthday"])
 
Out [32]
 
              Name             Team Position   Birthday   Salary
98    Vince Carter    Atlanta Hawks       PF 1977-01-26  2564753
196  Udonis Haslem       Miami Heat        C 1980-06-09  2564753
262    Kyle Korver  Milwaukee Bucks       PF 1981-03-17  6004753
```




What if we wanted to calculate the sum of all NBA salaries? One strategy
is to isolate the **Salary** `Series` and invoke the `sum` method on
that. We can also invoke `sum` directly on the `DataFrame` itself. The
`numeric_only` parameter can be used to target only columns with numeric
values. Otherwise, `pandas` will return the sum (i.e. the concatenation)
of string columns as well.



```
In  [33] nba.sum(numeric_only = True)
 
Out [33] Salary    3444112694
         dtype: int64
```




Yup, the total combined salaries of these 450 NBA players is a cool 3.44
billion. We can find the average salary with the `mean` method.



```
In  [34] nba.mean()
 
Out [34] Salary    7.653584e+06
         dtype: float64
```




Other statistical calculations like median and statistical deviation are
also available. They will automatically filter for only numeric columns.



```
In  [35] nba.median()
 
Out [35] Salary    3303074.5
         dtype: float64
 
In  [36] nba.std()
 
Out [36] Salary    9.288810e+06
         dtype: float64
```



Sorting a DataFrame
-------------------------



Our dataset arrived in a jumbled, random order but that\'s no problem!
We can sort our `DataFrame` by one or more columns with the
`sort_values` method. By default, the method returns a *new*
`DataFrame`.



#### Sort by Single Column



Let\'s first sort our players by name. We can pass a single string
argument to the `by` parameter of the `sort_values` method representing
the column whose values we\'d like to sort.



```
In  [37] nba.sort_values("Name")      # is the same as
         nba.sort_values(by = "Name")
 
Out [37]
 
                  Name                   Team Position   Birthday    Salary
52        Aaron Gordon          Orlando Magic       PF 1995-09-16  19863636
101      Aaron Holiday         Indiana Pacers       PG 1996-09-30   2239200
437        Abdel Nader  Oklahoma City Thunder       SF 1993-09-25   1618520
81         Adam Mokoka          Chicago Bulls        G 1998-07-18     79568
399  Admiral Schofield     Washington Wizards       SF 1997-03-30   1000000
…                    …                      …        …          …         …
159        Zach LaVine          Chicago Bulls       PG 1995-03-10  19500000
302       Zach Norvell     Los Angeles Lakers       SG 1997-12-09     79568
312       Zhaire Smith     Philadelphia 76ers       SG 1999-06-04   3058800
137    Zion Williamson   New Orleans Pelicans        F 2000-07-06   9757440
248     Zylan Cheatham   New Orleans Pelicans       SF 1995-11-17     79568
```


What if we wanted to find the five youngest players in the NBA? We could
sort the **Birthday** column in reverse chronological order by passing
`ascending` an argument of False, then take five rows off the top with
the `head` method. This is an example of method chaining, where multiple
methods are invoked in sequence on returned objects.



```
In  [38] nba.sort_values("Birthday", ascending = False).head()
 
Out [38]
 
                    Name                  Team Position   Birthday   Salary
136      Sekou Doumbouya       Detroit Pistons       SF 2000-12-23  3285120
432  Talen Horton-Tucker    Los Angeles Lakers       GF 2000-11-25   898310
137      Zion Williamson  New Orleans Pelicans        F 2000-07-06  9757440
313           RJ Barrett       New York Knicks       SG 2000-06-14  7839960
392         Jalen Lecque          Phoenix Suns        G 2000-06-13   898310
```




#### Sort by Multiple Columns

The `by` parameter of the `sort_values` method also accepts a list of
columns. The `DataFrame`\'s columns will be sorted in the order they are
stored in the list. By default, all sorts will be in ascending order.
The next example sorts the teams alphabetically, then sorts the players
within each team.



```
In  [39] nba.sort_values(by = ["Team", "Name"])
 
Out [39]
 
                Name                Team Position   Birthday    Salary
359         Alex Len       Atlanta Hawks        C 1993-06-16   4160000
167     Allen Crabbe       Atlanta Hawks       SG 1992-04-09  18500000
276  Brandon Goodwin       Atlanta Hawks       PG 1995-10-02     79568
438   Bruno Fernando       Atlanta Hawks        C 1998-08-15   1400000
194      Cam Reddish       Atlanta Hawks       SF 1999-09-01   4245720
  …                …                   …        …          …         …
418     Jordan McRae  Washington Wizards       PG 1991-03-28   1645357
273  Justin Robinson  Washington Wizards       PG 1997-10-12    898310
428    Moritz Wagner  Washington Wizards        C 1997-04-26   2063520
21     Rui Hachimura  Washington Wizards       PF 1998-02-08   4469160
36     Thomas Bryant  Washington Wizards        C 1997-07-31   8000000
```

We can pass a single Boolean value to the `ascending` parameter to apply
the same sort order to each column. Here, we sort the **Team** column in
descending (i.e. reverse alphabetical) order, then the **Name** column
in descending order as well.



```
In  [40] nba.sort_values(["Team", "Name"], ascending = False)
 
Out [40]
 
                Name                Team Position   Birthday    Salary
36     Thomas Bryant  Washington Wizards        C 1997-07-31   8000000
21     Rui Hachimura  Washington Wizards       PF 1998-02-08   4469160
428    Moritz Wagner  Washington Wizards        C 1997-04-26   2063520
273  Justin Robinson  Washington Wizards       PG 1997-10-12    898310
418     Jordan McRae  Washington Wizards       PG 1991-03-28   1645357
  …                …                   …        …          …         …
194      Cam Reddish       Atlanta Hawks       SF 1999-09-01   4245720
438   Bruno Fernando       Atlanta Hawks        C 1998-08-15   1400000
276  Brandon Goodwin       Atlanta Hawks       PG 1995-10-02     79568
167     Allen Crabbe       Atlanta Hawks       SG 1992-04-09  18500000
359         Alex Len       Atlanta Hawks        C 1993-06-16   4160000
```


What if we wanted a different sorting order for each column? For
example, we might want to sort the teams in ascending order, then sort
the salaries within those teams in descending order. To accomplish this,
we can pass the `ascending` parameter a list of Boolean values. The
lists passed to the `by` and `ascending` parameters must be equal in
length. `Pandas` will match each column with its sort order by on shared
index positions between the lists.



```
In  [41] nba.sort_values(by = ["Team", "Salary"],
                         ascending = [True, False])
 
Out [41]
 
                  Name                Team Position   Birthday    Salary
111   Chandler Parsons       Atlanta Hawks       SF 1988-10-25  25102512
28         Evan Turner       Atlanta Hawks       PG 1988-10-27  18606556
167       Allen Crabbe       Atlanta Hawks       SG 1992-04-09  18500000
213    De'Andre Hunter       Atlanta Hawks       SF 1997-12-02   7068360
339      Jabari Parker       Atlanta Hawks       PF 1995-03-15   6500000
  …                  …                   …        …          …         …
80         Isaac Bonga  Washington Wizards       PG 1999-11-08   1416852
399  Admiral Schofield  Washington Wizards       SF 1997-03-30   1000000
273    Justin Robinson  Washington Wizards       PG 1997-10-12    898310
283   Garrison Mathews  Washington Wizards       SG 1996-10-24     79568
353      Chris Chiozza  Washington Wizards       PG 1995-11-21     79568
```




As always, the `inplace` parameter mutates the original `DataFrame`
instead of returning a copy. There will be no output produced in Jupyter
Notebook



```
In  [42] nba.sort_values(by = ["Team", "Salary"],
                         ascending = [True, False],
                         inplace = True)
```




Sort by Index
-------------------


#### Sort by Row Index

The `sort_index` method sorts a `DataFrame` by its index values.



```
In  [43] nba.sort_index().head() # is the same as
         nba.sort_index(ascending = True).head()
 
Out [43]
 
             Name                Team Position   Birthday   Salary
0    Shake Milton  Philadelphia 76ers       SG 1996-09-26  1445697
1  Christian Wood     Detroit Pistons       PF 1995-09-27  1645357
2   PJ Washington   Charlotte Hornets       PF 1998-08-23  3831840
3    Derrick Rose     Detroit Pistons       PG 1988-10-04  7317074
4   Marial Shayok  Philadelphia 76ers        G 1995-07-26    79568
```




We can also reverse the sort order by passing False to the `ascending`
parameter.



```
In  [44] nba.sort_index(ascending = False).head()
 
Out [44]
 
              Name                 Team Position   Birthday    Salary
449    Ricky Rubio         Phoenix Suns       PG 1990-10-21  16200000
448  Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
447    Robin Lopez      Milwaukee Bucks        C 1988-04-01   4767000
446    Harry Giles     Sacramento Kings       PF 1998-04-22   2578800
445  Austin Rivers      Houston Rockets       PG 1992-08-01   2174310
```




Finally, we can make any of these changes permanent with the `inplace`
parameter.



```
In  [45] nba.sort_index(inplace = True)
```




#### Sort by Column Index

To sort the *columns* in order, pass an argument of either 1 or
\"columns\" to the `axis` parameter of the `sort_index` method.



```
In  [46] nba.sort_index(axis = 1).head() # is the same as
         nba.sort_index(axis = "columns").head()
 
Out [46]
 
    Birthday            Name Position   Salary                Team
0 1996-09-26    Shake Milton       SG  1445697  Philadelphia 76ers
1 1995-09-27  Christian Wood       PF  1645357     Detroit Pistons
2 1998-08-23   PJ Washington       PF  3831840   Charlotte Hornets
3 1988-10-04    Derrick Rose       PG  7317074     Detroit Pistons
4 1995-07-26   Marial Shayok        G    79568  Philadelphia 76ers
```




How about sorting the columns in reverse alphabetical order? As always,
it\'s just a matter of combining the right method with the right
arguments.



```
In  [47] nba.sort_index(axis = "columns", ascending = False).head()
 
Out [47]
 
                 Team   Salary Position            Name   Birthday
0  Philadelphia 76ers  1445697       SG    Shake Milton 1996-09-26
1     Detroit Pistons  1645357       PF  Christian Wood 1995-09-27
2   Charlotte Hornets  3831840       PF   PJ Washington 1998-08-23
3     Detroit Pistons  7317074       PG    Derrick Rose 1988-10-04
4  Philadelphia 76ers    79568        G   Marial Shayok 1995-07-26
```




The `inplace` parameter is available on the `sort_index` method call as
well.



Setting a New Index
-------------------------



Our dataset is fundamentally a list of players. It seems fitting to use
the **Name** column as the index labels. The `set_index` method returns
a new `DataFrame` with a given column serving as the index.



```
In  [48] nba.set_index(keys = "Name") # is the same as
         nba.set_index("Name")
 
Out [48]
 
                               Team Position   Birthday    Salary
Name                                                            
Shake Milton     Philadelphia 76ers       SG 1996-09-26   1445697
Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
PJ Washington     Charlotte Hornets       PF 1998-08-23   3831840
Derrick Rose        Detroit Pistons       PG 1988-10-04   7317074
Marial Shayok    Philadelphia 76ers        G 1995-07-26     79568
             …                    …        …          …         …
Austin Rivers       Houston Rockets       PG 1992-08-01   2174310
Harry Giles        Sacramento Kings       PF 1998-04-22   2578800
Robin Lopez         Milwaukee Bucks        C 1988-04-01   4767000
Collin Sexton   Cleveland Cavaliers       PG 1999-01-04   4764960
Ricky Rubio            Phoenix Suns       PG 1990-10-21  16200000
```




Looks good! Let\'s make the operation permanent.



```
In  [49] nba.set_index(keys = "Name", inplace = True)
```




If we know the column we\'d like to use as the index when importing a
dataset, we can also pass its name as a string to the `read_csv`
method\'s `index_col` parameter.



```
In  [50] nba = pd.read_csv("nba.csv",
                           parse_dates = ["Birthday"],
                           index_col = "Name")
```




Selecting Columns or Rows from a DataFrame
------------------------------------------------



A `DataFrame` is a collection of `Series` objects sharing a common
index. We can easily extract one or more these columns from the
`DataFrame`.



#### Select a Single Column from a DataFrame



Each `Series` column is available as an attribute on the `DataFrame`.
Object attributes are accessed with dot syntax. For example, we can
extract the **Salary** column with `nba.Salary`. Notice how the index
carries over from the `DataFrame` to the `Series`.



```
In  [51] nba.Salary
 
Out [51] Name
         Shake Milton       1445697
         Christian Wood     1645357
         PJ Washington      3831840
         Derrick Rose       7317074
         Marial Shayok        79568
                             ...  
         Austin Rivers      2174310
         Harry Giles        2578800
         Robin Lopez        4767000
         Collin Sexton      4764960
         Ricky Rubio       16200000
         Name: Salary, Length: 450, dtype: int64
```




If you\'d like to consistently work with 2-dimensional data structures,
a `Series` can be converted to a `DataFrame` with the `to_frame` method.



```
In  [52] nba.Salary.to_frame()
 
Out [52]
 
                  Salary
Name                   
Shake Milton     1445697
Christian Wood   1645357
PJ Washington    3831840
Derrick Rose     7317074
Marial Shayok      79568
             …         …
Austin Rivers    2174310
Harry Giles      2578800
Robin Lopez      4767000
Collin Sexton    4764960
Ricky Rubio     16200000
```




A column can also be extracted by passing its name between a pair of
square brackets. The advantage of this approach is that it supports
columns with spaces in their names.



```
In  [53] nba["Position"]
 
Out [53] Name
         Shake Milton      SG
         Christian Wood    PF
         PJ Washington     PF
         Derrick Rose      PG
         Marial Shayok      G
                           ..
         Austin Rivers     PG
         Harry Giles       PF
         Robin Lopez        C
         Collin Sexton     PG
         Ricky Rubio       PG
         Name: Position, Length: 450, dtype: object
```




#### Select Multiple Columns from a DataFrame



We might be curious to see what salary each player will be celebrating
on their birthdays. To extract multiple columns, declare a pair of
opening and closing square brackets, then pass the column names in a
list. The result will be a new `DataFrame` whose columns will have the
order of the list elements.



```
In  [54] nba[["Salary", "Birthday"]]
 
Out [54]
 
                  Salary   Birthday
Name                              
Shake Milton     1445697 1996-09-26
Christian Wood   1645357 1995-09-27
PJ Washington    3831840 1998-08-23
Derrick Rose     7317074 1988-10-04
Marial Shayok      79568 1995-07-26
             …         …          …
Austin Rivers    2174310 1992-08-01
Harry Giles      2578800 1998-04-22
Robin Lopez      4767000 1988-04-01
Collin Sexton    4764960 1999-01-04
Ricky Rubio     16200000 1990-10-21
```




This can be an effective way to rearrange the `DataFrame`\'s columns in
any desired order. Pass the columns in a list, then reassign the
resulting `DataFrame` back to its original variable.



What if we wanted to select columns based on their data types? The
`select_dtypes` method accepts `include` and `exclude` parameters, the
argument to either of which can be a single string or a list of data
types. As a reminder, you can use the `dtypes` attribute to see the
available types of data in the dataset.



```
12345678910In  [55] # Select only string columns
         nba.select_dtypes(include = "object")
 
Out [55]
 
               Name                 Team Position
0      Shake Milton   Philadelphia 76ers       SG
1    Christian Wood      Detroit Pistons       PF
2     PJ Washington    Charlotte Hornets       PF
3      Derrick Rose      Detroit Pistons       PG
4     Marial Shayok   Philadelphia 76ers        G
  …               …                    …        …
445   Austin Rivers      Houston Rockets       PG
446     Harry Giles     Sacramento Kings       PF
447     Robin Lopez      Milwaukee Bucks        C
448   Collin Sexton  Cleveland Cavaliers       PG
449     Ricky Rubio         Phoenix Suns       PG
 
In  [56] # Exclude string and integer columns
         nba.select_dtypes(exclude = ["object", "int"])
 
Out [56]
 
      Birthday
0   1996-09-26
1   1995-09-27
2   1998-08-23
3   1988-10-04
4   1995-07-26
  …          …
445 1992-08-01
446 1998-04-22
447 1988-04-01
448 1999-01-04
449 1990-10-21
```




Select Rows from a DataFrame
----------------------------------



Rows can be extracted from a `DataFrame` by index label or index
position.



#### Extract Rows by Index Label



The `loc` attribute accepts the label of a row to extract. It is
declared with a pair of square brackets containing the index label and
returns a `Series` object holding the values of the row with that label.
As with everything else in Python, the search is case-sensitive.



```
In  [57] nba.loc["LeBron James"]
 
Out [57] Team         Los Angeles Lakers
         Position                     PF
         Birthday    1984-12-30 00:00:00
         Salary                 37436858
         Name: LeBron James, dtype: object
```




We can also pass a list in between the square brackets to extract
multiple rows. The result will be a `DataFrame`.



```
In  [58] nba.loc[["Kawhi Leonard", "Paul George"]]
 
Out [58]
 
                               Team Position   Birthday    Salary
Name                                                            
Kawhi Leonard  Los Angeles Clippers       SF 1991-06-29  32742000
Paul George    Los Angeles Clippers       SF 1990-05-02  33005556
```




The rows will be returned in the order the index labels appear in the
list, not the order the labels appear in the `DataFrame`.



```
In  [59] nba.loc[["Paul George", "Kawhi Leonard"]]
 
Out [59]
 
                               Team Position   Birthday    Salary
Name                                                            
Paul George    Los Angeles Clippers       SF 1990-05-02  33005556
Kawhi Leonard  Los Angeles Clippers       SF 1991-06-29  32742000
```




`Pandas` also supports Python\'s list slicing syntax for extracting a
selection of index labels. For example, we can sort the index to get the
players\' names in alphabetical order, then select all players between
Otto Porter and Patrick Beverley. With string labels, both endpoints
will be inclusive.



```
In  [60] nba.sort_index().loc["Otto Porter":"Patrick Beverley"]
 
Out [60]
 
                                  Team Position   Birthday    Salary
Name                                                               
Otto Porter              Chicago Bulls       SF 1993-06-03  27250576
PJ Dozier               Denver Nuggets       PG 1996-10-25     79568
PJ Washington        Charlotte Hornets       PF 1998-08-23   3831840
Pascal Siakam          Toronto Raptors       PF 1994-04-02   2351838
Pat Connaughton        Milwaukee Bucks       SG 1993-01-06   1723050
Patrick Beverley  Los Angeles Clippers       PG 1988-07-12  12345680
```




We can also pull out a collection of values from the middle of the
`DataFrame` to the end. It\'s the same syntax as extracting elements
from the middle of a Python list: a colon following the initial index
label.



```
In  [61] nba.sort_index().loc["Zach Collins":]
 
Out [61]
 
                                   Team Position   Birthday    Salary
Name                                                                 
Zach Collins     Portland Trail Blazers        C 1997-11-19   4240200
Zach LaVine               Chicago Bulls       PG 1995-03-10  19500000
Zach Norvell         Los Angeles Lakers       SG 1997-12-09     79568
Zhaire Smith         Philadelphia 76ers       SG 1999-06-04   3058800
Zion Williamson    New Orleans Pelicans        F 2000-07-06   9757440
Zylan Cheatham     New Orleans Pelicans       SF 1995-11-17     79568
```




Alternatively, we can use list slicing syntax to pull from the beginning
of the `DataFrame` *to* a specific index label. Provide a colon followed
by the index label to extract to. The syntax below returns all players
from the beginning to the dataset to \"Al Horford\".



```
In  [62] nba.sort_index().loc[:"Al Horford"]
 
Out [62]
 
                                    Team Position   Birthday    Salary
Name                                                                 
Aaron Gordon               Orlando Magic       PF 1995-09-16  19863636
Aaron Holiday             Indiana Pacers       PG 1996-09-30   2239200
Abdel Nader        Oklahoma City Thunder       SF 1993-09-25   1618520
Adam Mokoka                Chicago Bulls        G 1998-07-18     79568
Admiral Schofield     Washington Wizards       SF 1997-03-30   1000000
Al Horford            Philadelphia 76ers        C 1986-06-03  28000000
```




A `KeyError` exception will be raised if an index label does not exist
in the `DataFrame`.



```
In  [63] nba.loc["Bugs Bunny"]
 
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
 
KeyError: 'Bugs Bunny'
```




#### Extract Rows by Index Position



The `iloc` (index location) attribute extracts one or more rows by index
position. It accepts either a single integer for one record or a list of
integers for multiple records.



```
In  [64] nba.iloc[300]
 
Out [64] Team             Denver Nuggets
         Position                     PF
         Birthday    1999-04-03 00:00:00
         Salary                  1416852
         Name: Jarred Vanderbilt, dtype: object
 
In  [65] nba.iloc[[100, 200, 300, 400]]
 
Out [65]
 
                                Team Position   Birthday   Salary
Name                                                            
Brian Bowen           Indiana Pacers       SG 1998-10-02    79568
Marco Belinelli    San Antonio Spurs       SF 1986-03-25  5846154
Jarred Vanderbilt     Denver Nuggets       PF 1999-04-03  1416852
Louis King           Detroit Pistons        F 1999-04-06    79568
```




List slicing syntax is valid here as well. However, in this scenario,
the numeric value after the colon is *exclusive*. The four players below
represent index positions 400, 401, 402, and 403.



```
In  [66] nba.iloc[400:404]
 
Out [66]
 
                                    Team Position   Birthday    Salary
Name                                                                  
Louis King               Detroit Pistons        F 1999-04-06     79568
Kostas Antetokounmpo  Los Angeles Lakers       PF 1997-11-20     79568
Rodions Kurucs             Brooklyn Nets       PF 1998-02-05   1699236
Spencer Dinwiddie          Brooklyn Nets       PG 1993-04-06  10605600
 
In  [67] nba.iloc[:2]
 
Out [67]
 
                              Team Position   Birthday   Salary
Name                                                          
Shake Milton    Philadelphia 76ers       SG 1996-09-26  1445697
Christian Wood     Detroit Pistons       PF 1995-09-27  1645357
 
In  [68] nba.iloc[447:]
 
Out [68]
 
                              Team Position   Birthday    Salary
Name                                                           
Robin Lopez        Milwaukee Bucks        C 1988-04-01   4767000
Collin Sexton  Cleveland Cavaliers       PG 1999-01-04   4764960
Ricky Rubio           Phoenix Suns       PG 1990-10-21  16200000
```




Negative numbers can also be passed for one or both of the values. The
next example extracts from the 10^th^-to-last row up to but not
including the 6^th^-to-last row.



```
In  [69] nba.iloc[-10:-6]
 
Out [69]
 
                                    Team Position   Birthday   Salary
Name                                                                
Jared Dudley          Los Angeles Lakers       PF 1985-07-10  2564753
Max Strus                  Chicago Bulls       SG 1996-03-28    79568
Kevon Looney       Golden State Warriors        C 1996-02-06  4464286
Willy Hernangomez      Charlotte Hornets        C 1994-05-27  1557250
```




A third number after a second colon specifies the step sequence or, in
other words, the stride interval between every two index locations. In
the example below, we select each alternate row from the first ten rows.
The results thus have index position 0, 2, 4, 6, and 8.



```
In  [70] nba.iloc[0:10:2]
 
Out [70]
 
                             Team Position   Birthday    Salary
Name                                                          
Shake Milton   Philadelphia 76ers       SG 1996-09-26   1445697
PJ Washington   Charlotte Hornets       PF 1998-08-23   3831840
Marial Shayok  Philadelphia 76ers        G 1995-07-26     79568
Kendrick Nunn          Miami Heat       SG 1995-08-03   1416852
Brook Lopez       Milwaukee Bucks        C 1988-04-01  12093024
```




#### Extract Values from Specific Columns



Both the `loc` and `iloc` attributes accept a second argument
representing the column(s) to extract. In the example below, we use
`loc` to identify the value at the intersection of the \"Giannis
Antetokounmpo\" index label and the **Team** column.



```
In  [71] nba.loc["Giannis Antetokounmpo", "Team"]
 
Out [71] 'Milwaukee Bucks'
```




A list can be passed for either one of the two arguments, or both of
them.



```
In  [72] # Extract the row with a "James Harden" index label and the
         # values from the "Position" and "Birthday" columns
 
         nba.loc["James Harden", ["Position", "Birthday"]]
 
Out [72] Position                     PG
         Birthday    1989-08-26 00:00:00
         Name: James Harden, dtype: object
 
In  [73] # Extract the rows with "Russell Westbrook" and "Anthony Davis"
         # index labels and values from the "Team" and "Salary" columns
 
         nba.loc[
                 ["Russell Westbrook", "Anthony Davis"],
                 ["Team", "Salary"]
                ]
 
Out [73]
 
                                 Team    Salary
Name                                          
Russell Westbrook     Houston Rockets  38506482
Anthony Davis      Los Angeles Lakers  27093019
```




List slicing syntax can also be used to extract multiple columns without
explicitly writing out all of their names. We have four columns in our
dataset; let\'s extract all columns from **Position** to **Salary**.
Both endpoints will be inclusive.



```
In  [74] nba.loc["Joel Embiid", "Position":"Salary"]
 
Out [74] Position                      C
         Birthday    1994-03-16 00:00:00
         Salary                 27504630
         Name: Joel Embiid, dtype: object
```




The column names must be passed in the order they appear in the
`DataFrame`. The code below yields an empty result because the
**Salary** column comes after the **Position** column.



```
In  [75] nba.loc["Joel Embiid", "Salary":"Position"]
 
Out [75] Series([], Name: Joel Embiid, dtype: object)
```




Each `DataFrame` column is assigned an index position. In our current
`DataFrame`, **Team** has an index of 0, **Position** has an index of 1,
and so on.



```
In  [76] nba.columns
 
Out [76] Index(['Team', 'Position', 'Birthday', 'Salary'], dtype='object')
```




The index position of a column can also be passed as the second argument
to `iloc`.



```
In  [77] nba.iloc[57, 3]
 
Out [77] 796806
```




List slicing syntax can be mixed and matched here as well. The next
example pulls all rows from index position 100 up to (but not including)
index position 104, as well as the columns from the beginning up to (but
not including) the column at index position 3 (**Salary**).



```
In  [78] nba.iloc[100:104, :3]
 
Out [78]
 
                             Team Position   Birthday
Name                                                 
Brian Bowen        Indiana Pacers       SG 1998-10-02
Aaron Holiday      Indiana Pacers       PG 1996-09-30
Troy Daniels   Los Angeles Lakers       SG 1991-07-15
Buddy Hield      Sacramento Kings       SG 1992-12-17
```




The `iloc` and `loc` attributes are remarkably versatile. They can
accept a single value, a list of values, a list slice, and more. The
disadvantage of this flexibility is that it demands extra overhead;
`pandas` has to perform several conditional checks to figure out what
kind of input we\'ve given to `iloc` or `loc`.



Two alternatives attributes, `at` and `iat`, are available when we want
to extract a *single* value from a `DataFrame`. The `at` attribute
accepts the row and columns labels, while the `iat` attributes accepts
the row and column indices.



```
In  [79] nba.at["Austin Rivers", "Birthday"]
 
Out [79] Timestamp('1992-08-01 00:00:00')
 
In  [80] nba.iat[263, 1]
 
Out [80] 'PF'
```




The `%%time it` magic method in Jupyter Notebook calculates the average
processing time of the code in a cell. Sometimes, it can even run the
cell 100,000 times! The results below are subject to some degree of
variance between different machines but show the clear speed advantage
of the `at` and `iat` attributes over `loc` and `iloc`.



```
In  [81] %%timeit
         nba.at["Austin Rivers", "Birthday"]
 
6.38 µs ± 53.6 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
 
In  [82] %%timeit
         nba.loc["Austin Rivers", "Birthday"]
 
9.12 µs ± 53.8 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
 
In  [83] %%timeit
         nba.iat[263, 1]
 
4.7 µs ± 27.4 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
 
In  [84] %%timeit
         nba.iloc[263, 1]
 
7.41 µs ± 39.1 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```




Extract Value from Series
-------------------------------



The `loc`, `iloc`, `at`, and `iat` attributes are available on `Series`
objects as well. We can practice by extracting a sample `Series` from
our `DataFrame`.



```
In  [85] nba["Salary"].loc["Damian Lillard"]
 
Out [85] 29802321
 
In  [86] nba["Salary"].at["Damian Lillard"]
 
Out [86] 29802321
 
In  [87] nba["Salary"].iloc[234]
 
Out [87] 2033160
 
In  [88] nba["Salary"].iat[234]
 
Out [88] 2033160
```




Rename Column or Row
--------------------------



We can rename some or all of the columns in the `DataFrame` by
overwriting the `columns` attribute with a list of new names.



```
In  [89] nba.columns
 
Out [89] Index(['Team', 'Position', 'Birthday', 'Pay'], dtype='object')
 
In  [90] nba.columns = ["Team", "Position", "Date of Birth", "Pay"]
            nba.head(1)
 
Out [90]
 
                            Team Position Date of Birth      Pay
Name                                                           
Shake Milton  Philadelphia 76ers       SG    1996-09-26  1445697
```




The `rename` method is an alternate option. We can pass its `columns`
parameter a dictionary with keys representing the existing column names
and values representing their new names.



```
In  [91] nba.rename(columns = { "Date of Birth": "Birthday" })
 
Out [91]
 
                               Team Position   Birthday       Pay
Name                                                            
Shake Milton     Philadelphia 76ers       SG 1996-09-26   1445697
Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
PJ Washington     Charlotte Hornets       PF 1998-08-23   3831840
Derrick Rose        Detroit Pistons       PG 1988-10-04   7317074
Marial Shayok    Philadelphia 76ers        G 1995-07-26     79568
            …               …              …          …         …
Austin Rivers       Houston Rockets       PG 1992-08-01   2174310
Harry Giles        Sacramento Kings       PF 1998-04-22   2578800
Robin Lopez         Milwaukee Bucks        C 1988-04-01   4767000
Collin Sexton   Cleveland Cavaliers       PG 1999-01-04   4764960
Ricky Rubio            Phoenix Suns       PG 1990-10-21  16200000
 
As always, use the inplace parameter to make the operation permanent.
 
In  [92] nba.rename(
           columns = { "Date of Birth": "Birthday" },
           inplace = True
         )
```




The `rename` method can rename an index label. The example below swaps
\"Giannis Antetokounmpo\" with his popular nickname \"Greek Freak\".



```
In  [93] nba.loc["Giannis Antetokounmpo"]
 
Out [93] Team                 Milwaukee Bucks
         Position                          PF
         Birthday         1994-12-06 00:00:00
         Pay                         25842697
         Name: Giannis Antetokounmpo, dtype: object
 
In  [94] nba.rename(
           index = { "Giannis Antetokounmpo": "Greek Freak" }, 
           inplace = True
         )
 
In  [95] nba.loc["Greek Freak"]
 
Out [95] Team                 Milwaukee Bucks
         Position                          PF
         Birthday         1994-12-06 00:00:00
         Pay                         25842697
         Name: Greek Freak, dtype: object
```




Resetting an Index
-------------------------



What if we wanted another column to serve as the index of our
`DataFrame`? We *could* invoke the `set_index` method again with a
different column but, unfortunately, that would lose the current index
of player names.



```
In  [96] nba.set_index("Team").head()
 
Out [96]
 
                   Position   Birthday   Salary
Team___________________________________________                                          
Philadelphia 76ers       SG 1996-09-26  1445697
Detroit Pistons          PF 1995-09-27  1645357
Charlotte Hornets        PF 1998-08-23  3831840
Detroit Pistons          PG 1988-10-04  7317074
Philadelphia 76ers        G 1995-07-26    79568
```




In order to preserve the player\'s names, we need to first re-integrate
the existing index as a regular column in our `DataFrame`. The
`reset_index` method moves an existing index\'s values into a column and
generates a fresh sequential index.



```
In  [97] nba.reset_index().head()
 
Out [97]
 
               Name                 Team Position   Birthday    Salary
0      Shake Milton   Philadelphia 76ers       SG 1996-09-26   1445697
1    Christian Wood      Detroit Pistons       PF 1995-09-27   1645357
2     PJ Washington    Charlotte Hornets       PF 1998-08-23   3831840
3      Derrick Rose      Detroit Pistons       PG 1988-10-04   7317074
4     Marial Shayok   Philadelphia 76ers        G 1995-07-26     79568
 
Now we're in the clear to use the set_index method.
 
In  [98] nba.reset_index().set_index("Team").head()
 
Out [98]
 
                              Name Position   Birthday   Salary
Team___________________________________________________________                                                          
Philadelphia 76ers    Shake Milton       SG 1996-09-26  1445697
Detroit Pistons     Christian Wood       PF 1995-09-27  1645357
Charlotte Hornets    PJ Washington       PF 1998-08-23  3831840
Detroit Pistons       Derrick Rose       PG 1988-10-04  7317074
Philadelphia 76ers   Marial Shayok        G 1995-07-26    79568
```




The `reset_index` method also accepts an `inplace` parameter. Be
careful, however. If the parameter is set to True, the method will not
return a new `DataFrame` and thus the `set_index` method cannot be
chained on in sequence. We\'ll have to rely on two separate method calls
in sequence.



```
In  [99] nba.reset_index(inplace = True)
         nba.set_index("Name", inplace = True)
```




Coding Challenge
-----------------------



Now that we\'ve explored the financials of the NBA, let\'s practice the
concepts in the lab with a similar dataset. The `nfl.csv` file
contains a list of players in the National Football League with similar
**Team**, **Position**, **Birthday** and **Salary** columns. See if you
can answer the questions below.


1.   How can we import the **nfl.csv** file? What\'s an
    effective way to convert its **Birthday** column to store datetime
    objects?


The `read_csv` method can import the CSV text file. The `parse_dates`
parameter accepts a list of columns whose values should be coerced into
datetime objects.



```
In  [100] nfl = pd.read_csv("nfl.csv", parse_dates = ["Birthday"])
          nfl
 
Out [100]
 
                    Name                  Team Position   Birthday   Salary
0           Tremon Smith   Philadelphia Eagles       RB 1996-07-20   570000
1         Shawn Williams    Cincinnati Bengals       SS 1991-05-13  3500000
2            Adam Butler  New England Patriots       DT 1994-04-12   645000
3            Derek Wolfe        Denver Broncos       DE 1990-02-24  8000000
4              Jake Ryan  Jacksonville Jaguars      OLB 1992-02-27  1000000
   …                   …                     …        …          …        …
1650    Bashaud Breeland    Kansas City Chiefs       CB 1992-01-30   805000
1651         Craig James   Philadelphia Eagles       CB 1996-04-29   570000
1652  Jonotthan Harrison         New York Jets        C 1991-08-25  1500000
1653         Chuma Edoga         New York Jets       OT 1997-05-25   495000
1654        Tajae Sharpe      Tennessee Titans       WR 1994-12-23  2025000
 
1655 rows × 5 columns
```



2.   What are the two ways we can overwrite the index of
    the `DataFrame` to store the player names?


Our first option is to invoke the `set_index` method on our existing
`DataFrame` with an `inplace` argument of True.



```
In  [101] nfl.set_index("Name", inplace = True)
```




Our second option is to use the `index_col` parameter with the
`read_csv` method when importing the dataset.



```
In  [102] nfl = pd.read_csv("nfl.csv", index_col = "Name",
                            parse_dates = ["Birthday"])
```




The results will be the same either way.



```
In  [103] nfl.head()
 
Out [103]
 
                                Team Position   Birthday   Salary
Name                                                            
Tremon Smith     Philadelphia Eagles       RB 1996-07-20   570000
Shawn Williams    Cincinnati Bengals       SS 1991-05-13  3500000
Adam Butler     New England Patriots       DT 1994-04-12   645000
Derek Wolfe           Denver Broncos       DE 1990-02-24  8000000
Jake Ryan       Jacksonville Jaguars      OLB 1992-02-27  1000000
```



3.   How can we can get a count of the number of players
    per team in this dataset?


We can invoke the `value_counts` method on the **Team** column. Extract
the `Series` with either dot syntax or square brackets. The results
below are truncated for brevity.



```
In  [104] nfl.Team.value_counts()    # is the same as
          nfl["Team"].value_counts()
 
Out [104] New York Jets           58
          Washington Redskins     56
          Kansas City Chiefs      56
          San Francisco 49Ers     55
          New Orleans Saints      55
```



4.   Who are the five highest paid players in this
    dataset?


The `sort_values` method can sort the **Salary** column for us. To
modify its default ascending sort order, we pass a False argument to the
`ascending` parameter.



```
In  [105] nfl.sort_values("Salary", ascending = False).head()
 
Out [105]
 
                                 Team Position   Birthday    Salary
Name                                                              
Kirk Cousins        Minnesota Vikings       QB 1988-08-19  27500000
Jameis Winston   Tampa Bay Buccaneers       QB 1994-01-06  20922000
Marcus Mariota       Tennessee Titans       QB 1993-10-30  20922000
Derek Carr            Oakland Raiders       QB 1991-03-28  19900000
Jimmy Garoppolo   San Francisco 49Ers       QB 1991-11-02  17200000
```



5.   I\'d like to sort the dataset by teams in
    alphabetical order, then by salary in descending order. What will
    the code look like?


We\'ll have to pass a list argument to both the `by` and `ascending`
parameters of the `sort_values` method.



```
In  [106] nfl.sort_values(by = ["Team", "Salary"],
                          ascending = [True, False])
 
Out [106]
 
                                   Team Position   Birthday    Salary
Name                                                                 
Chandler Jones        Arizona Cardinals      OLB 1990-02-27  16500000
Patrick Peterson      Arizona Cardinals       CB 1990-07-11  11000000
Larry Fitzgerald      Arizona Cardinals       WR 1983-08-31  11000000
David Johnson         Arizona Cardinals       RB 1991-12-16   5700000
Justin Pugh           Arizona Cardinals        G 1990-08-15   5000000
                 …                   …         …          …         …
Ross Pierschbacher  Washington Redskins        C 1995-05-05    495000
Kelvin Harmon       Washington Redskins       WR 1996-12-15    495000
Wes Martin          Washington Redskins        G 1996-05-09    495000
Jimmy Moreland      Washington Redskins       CB 1995-08-26    495000
Jeremy Reaves       Washington Redskins       SS 1996-08-29    495000
```



6.   Who is the oldest player on the New York Jets
    roster? What is his birthday?


This is a tricky one. Given the current tools at our disposal, here\'s
what we can do. We want to set the **Team** column as the index of the
`DataFrame` to allow for easy extraction of all Jets players. To
preserve the player names currently in our index, we\'ll have to use the
`reset_index` method first.



```
In  [107] nfl.reset_index(inplace = True)
          nfl.set_index(keys = "Team", inplace = True)
          nfl.head(3)
 
Out [107]
 
                                Name Position   Birthday   Salary
Team_____________________________________________________________                                                             
Philadelphia Eagles     Tremon Smith       RB 1996-07-20   570000
Cincinnati Bengals    Shawn Williams       SS 1991-05-13  3500000
New England Patriots     Adam Butler       DT 1994-04-12   645000
```




Next, we can use the `loc` attribute to isolate all players on the New
York Jets.



```
In  [108] nfl.loc["New York Jets"].head()
Out [108]
                             Name Position   Birthday   Salary Team________________________________________________________                                                         New York Jets   Bronson Kaufusi       DE 1991-07-06   645000 New York Jets    Darryl Roberts       CB 1990-11-26  1000000 New York Jets     Jordan Willis       DE 1995-05-02   754750 New York Jets  Quinnen Williams       DE 1997-12-21   495000New York Jets        Sam Ficken        K 1992-12-14   495000
```




The last step is to sort the **Birthday** column and extract the top
record. This sort is only possible because we converted the values to
store datetime objects.



```
In  [109] nfl.loc["New York Jets"].sort_values("Birthday").head(1)
 
Out [109]
 
                     Name Position   Birthday   Salary
Team__________________________________________________
New York Jets  Ryan Kalil        C 1985-03-29  2400000
```

The oldest player on the New York Jets in this dataset is Ryan Kalil.
His birthday is March 29th, 1985.
