
The GroupBy object
====================

### This lab covers:

- Using a [GroupBy] object to store multiple
    [DataFrames]
- Extracting first and last rows from each `DataFrame` in a
    [GroupBy] object
- Performing aggregate operations on groups
- Iterating over each `DataFrame` in a group


Creating a GroupBy Object from Scratch
------------------------------------------------



Let\'s create a new Jupyter Notebook and import the `Pandas` library.



```
In  [1] import pandas as pd
```




We\'ll kick things off with a small example and explain more of the
technical details in the next section. Let\'s create a simple
`DataFrame`. It will consist of 5 rows of fruit and vegetable
prices for a supermarket. Each item will be classified as either a fruit
or a vegetable.



```
In  [2] food_data = {
          "Item": ["Banana", "Cucumber", "Orange", "Tomato", "Watermelon"],
          "Type": ["Fruit", "Vegetable", "Fruit", "Vegetable", "Fruit"],
          "Price": [0.99, 1.25, 0.25, 0.33, 3.00]
        }
 
        supermarket = pd.DataFrame(data = food_data)
 
        supermarket
 
Out [2]
 
         Item       Type  Price
0      Banana      Fruit   0.99
1    Cucumber  Vegetable   1.25
2      Orange      Fruit   0.25
3      Tomato  Vegetable   0.33
4  Watermelon      Fruit   3.00
```




A [GroupBy] operation is ideal when we want to group
`DataFrame` rows into clusters based on shared values in a column.
For example, the supermarket owner may be curious about the performance
of the two *types* of items he sells: fruits and vegetables. If he can
isolate the [\"Fruit\"] rows and [\"Vegetable\"] rows into
separate groups, it becomes easier to perform an aggregate analysis on
either, such as calculating the average price of items within the group.



Let\'s begin by invoking the [groupby] method on the
[supermarket] `DataFrame`. Pass in the name of the column
whose values should be used to create the groups. The return value will
be a *new object,* a [DataFrameGroupBy] object. This is a
*separate* and *distinct* entity compared to a `DataFrame` like
[supermarket].



```
In  [3] group = supermarket.groupby("Type")
        group
 
Out [3] <pandas.core.groupby.generic.DataFrameGroupBy object at 
        0x114f2db90>
```




There are 2 unique values within the **Type** column, so there will be 2
groups within the [GroupBy] object. The [get\_group] method
accepts a grous name and returns the corresponding rows.



```
In  [4] group.get_group("Fruit")
 
Out [4]
 
         Item  Price
0      Banana   0.99
2      Orange   0.25
4  Watermelon   3.00
```




The [GroupBy] also supports aggregate operations. The next example
invokes the [mean] method to calculate the average price of items
within each group.



```
In  [5] group.mean()
 
Out [5]
 
              Price
Type              
Fruit      1.413333
Vegetable  0.790000
```




With the foundational knowledge under our belts, we are clear to move on
to a more complex dataset.



Creating a GroupBy Object from Dataset
------------------------------------------------



In This lab, we\'ll be working with the [fortune1000.csv]
file. The Fortune 1000 is a listing of the 1,000 largest companies
within the United States, sorted by revenue. The list is updated
annually by the business magazine Fortune. Each row includes the
company\'s name, revenue and profit numbers, employee count, sector, and
industry. Multiple companies are categorized under the same sector. For
example, Apple and Amazon.com both belong to the Technology sector.
Industries can be considered a subcategory within each sector. For
example, the Pipelines and Petroleum Refining industries both fall under
the Energy sector.



```
In  [6] pd.read_csv("fortune1000.csv")
 
Out [6]
 
          Company  Revenues  Profits  Employees        Sector      Industry
0         Walmart  500343.0   9862.0    2300000     Retailing  General M...
1     Exxon Mobil  244363.0  19710.0      71200        Energy  Petroleum...
2    Berkshire...  242137.0  44940.0     377000    Financials  Insurance...
3           Apple  229234.0  48351.0     123000    Technology  Computers...
4    UnitedHea...  201159.0  10558.0     260000   Health Care  Health Ca...
…               …         …        …          …             …             …
995  SiteOne L...    1862.0     54.6       3664   Wholesalers  Wholesale...
996  Charles R...    1858.0    123.4      11800   Health Care  Health Ca...
997     CoreLogic    1851.0    152.2       5900  Business ...  Financial...
998  Ensign Group    1849.0     40.5      21301   Health Care  Health Ca...
999           HCP    1848.0    414.2        190    Financials   Real estate
 
In  [7] fortune = pd.read_csv("fortune1000.csv")
```




The **Sector** column holds 21 unique sectors. Imagine we wanted to find
the average revenues across the companies within *each* of those
sectors. Before we use the [GroupBy] object, let\'s solve the
problem with a more traditional approach. As first introduced in the
**Filtering a DataFrame** lab, we can create a Boolean
`Series` to extract rows based on a specific value within any
`DataFrame` column. In the next example, we target all companies
within the [\"Retailing\"] sector.



```
In  [8] in_retailing = fortune["Sector"] == "Retailing"
        retailing_companies = fortune[in_retailing]
        retailing_companies.head()
 
Out [8]
 
       Company  Revenues  Profits  Employees     Sector           Industry
0      Walmart  500343.0   9862.0    2300000  Retailing  General Mercha...
7   Amazon.com  177866.0   3033.0     566000  Retailing  Internet Servi...
14      Costco  129025.0   2679.0     182000  Retailing  General Mercha...
22  Home Depot  100904.0   8630.0     413000  Retailing  Specialty Reta...
38      Target   71879.0   2934.0     345000  Retailing  General Mercha...
```




We can then calculate the Retailing sector\'s average revenue by calling
the [mean] method on the **Revenues** column.



```
In  [9] retailing_companies["Revenues"].head()
 
Out [9] 0     500343.0
        7     177866.0
        14    129025.0
        22    100904.0
        38     71879.0
        Name: Revenues, dtype: float64
 
In  [10] retailing_companies["Revenues"].mean()
 
Out [10] 21874.714285714286
```




The code above is a suitable solution to calculate the average revenue
of *one* sector. However, we\'ll need to write some additional code if
we want to apply the same logic to the other 20 sectors within the
[fortune] `DataFrame`. Python can help automate some of the
repetition, but the [GroupBy] object offers the same solution out
of the box. There\'s no need to reinvent the wheel.



Let\'s invoke the [groupby] method on [fortune]. It accepts
a string for the column whose values should be used to group the rows. A
column is a good candidate for a grouping if it contains duplicate
values or, in other words, if multiple rows share a value within it.
We\'ll target the **Sector** column in the next example and assign the
return value to a [sectors] variable.



```
In  [11] sectors = fortune.groupby("Sector")
 
What kind of object are we dealing with here? Let's output the sectors variable to see.
 
In  [12] sectors
 
Out [12] <pandas.core.groupby.generic.DataFrameGroupBy object at 
         0x1235b1d10>
```




It\'s a [DataFrameGroupBy] object! A [GroupBy] object is
just a bundle of multiple [DataFrames]. Behind the scenes,
`Pandas` has repeated the extraction process we used for the
[\"Retailing\"] sector a few examples ago \-- but it\'s done so
for all 21 sectors in the **Sector** column.



Let\'s count the number of [DataFrames] stored within the
[sectors] [GroupBy] object by passing it into Python\'s
built-in [len] function.



```
In  [13] len(sectors)
 
Out [13] 21
```




There are 21 [DataFrames] within the [sectors]
[GroupBy] object because there are 21 unique values within the
**Sector** column in [fortune]. We can confirm this by invoking
the [nunique] method on the original **Sector** column.



```
In  [14] fortune["Sector"]
 
Out [14] 0              Retailing
         1                 Energy
         2             Financials
         3             Technology
         4            Health Care
                      ...       
         995          Wholesalers
         996          Health Care
         997    Business Services
         998          Health Care
         999           Financials
         Name: Sector, Length: 1000, dtype: object
 
In  [15] fortune["Sector"].nunique()
 
Out [15] 21
```




What are the 21 different sectors and how many companies from
[fortune] belong to each one? The [size] method on the
[GroupBy] object returns a `Series` with the information.
The output below reveals that, for example, 25 companies within
[fortune] have a **Sector** column value of [\"Aerospace &
Defense\"].



```
In  [16] sectors.size()
 
Out [16] Sector
         Aerospace & Defense               25
         Apparel                           14
         Business Services                 53
         Chemicals                         33
         Energy                           107
         Engineering & Construction        27
         Financials                       155
         Food &  Drug Stores               12
         Food, Beverages & Tobacco         37
         Health Care                       71
         Hotels, Restaurants & Leisure     26
         Household Products                28
         Industrials                       49
         Materials                         45
         Media                             25
         Motor Vehicles & Parts            19
         Retailing                         77
         Technology                       103
         Telecommunications                10
         Transportation                    40
         Wholesalers                       44
         dtype: int64
```




Remember the trusty [value\_counts] method we\'ve previously
invoked on `Series`? It also exists on a [GroupBy] object
and counts the occurrences of each unique value in the **Sector**
`Series` in [fortune]. The returned `Series` holds the
same information as the `Series` above, but is sorted by number of
occurrences rather than by sector name.



```
In  [17] fortune["Sector"].value_counts()
 
Out [17] Financials                       155
         Energy                           107
         Technology                       103
         Retailing                         77
         Health Care                       71
         Business Services                 53
         Industrials                       49
         Materials                         45
         Wholesalers                       44
         Transportation                    40
         Food, Beverages & Tobacco         37
         Chemicals                         33
         Household Products                28
         Engineering & Construction        27
         Hotels, Restaurants & Leisure     26
         Aerospace & Defense               25
         Media                             25
         Motor Vehicles & Parts            19
         Apparel                           14
         Food &  Drug Stores               12
         Telecommunications                10
         Name: Sector, dtype: int64
```




Attributes and Methods on a GroupBy Object
----------------------------------------------------



Another way to visualize our [GroupBy] object is as a dictionary
that maps the 21 unique sectors to a collection of rows from
[fortune] belonging to each one. The [groups] attribute
reveals a dictionary with these group-to-row associations. The keys are
sector names and the values are [Index] objects that hold row
index positions from the [fortune] `DataFrame`. The results
below are truncated to the first two keys in the dictionary.



```
In  [18] sectors.groups
 
Out [18]
 
'Aerospace &  Defense': IntIndex([ 26,  50,  58,  98, 117, 118, 207, 224, 
                                     275, 380, 404, 406, 414, 540, 660, 
                                     661, 806, 829, 884, 930, 954, 955, 
                                     959, 975, 988], dtype='int64'),
 'Apparel': IntIndex([88, 241, 331, 420, 432, 526, 529, 554, 587, 678, 
                        766, 774, 835, 861], dtype='int64'),
```




As introduced in **The DataFrame Object** lab, the [loc]
accessor can target the cell at an intersection of a row and column
within a `DataFrame`. We can extract a sample row to confirm it is
being pulled into the correct sector group. Let\'s try 26, the first
index position listed in the [\"Aerospace & Defense\"] group.



```
In  [19] fortune.loc[26, "Sector"]
 
Out [19] 'Aerospace &  Defense'
```




Now that we understand the [GroupBy] object from a big-picture
perspective, let\'s explore some of its powerful operations.



What if wanted to find the highest performing company (by revenue)
within each sector? The [GroupBy] object\'s [first] method
extracts *the first* row listed for each sector in [fortune].
Because our [fortune] `DataFrame` is sorted by revenue, the
first company pulled out for each sector *will be* the highest
performing company within that sector. The return value of [first]
is a 21-row `DataFrame` (one company per sector).



```
In  [20] sectors.first().head(10)
 
Out [20]
 
                      Company  Revenues  Profits  Employees       Industry
Sector____________________________________________________________________                                                                                                                                      
Aerospace &...         Boeing   93392.0   8197.0     140800  Aerospace ...
Apparel                  Nike   34350.0   4240.0      74400        Apparel
Business Se...  ManpowerGroup   21034.0    545.4      29000  Temporary ...
Chemicals           DowDuPont   62683.0   1460.0      98000      Chemicals
Energy            Exxon Mobil  244363.0  19710.0      71200  Petroleum ...
Engineering...          Fluor   19521.0    191.4      56706  Engineerin...
Financials      Berkshire ...  242137.0  44940.0     377000  Insurance:...
Food &  Dru...         Kroger  122662.0   1907.0     449000  Food and D...
Food, Bever...        PepsiCo   63525.0   4857.0     263000  Food Consu...
Health Care     UnitedHeal...  201159.0  10558.0     260000  Health Car...
```




Conversely, the [last] method on the [GroupBy] object
extracts the *last* company from the [fortune] dataset that falls
under each sector. Again, this is based on the company\'s *order* within
the rows of the [fortune] `DataFrame`. The results below
reveal the companies with the lowest revenue per sector.



```
In  [21] sectors.last().head(10)
 
Out [21]
 
                      Company  Revenues  Profits  Employees       Industry
Sector____________________________________________________________________                                                                    
Aerospace &...  Aerojet Ro...    1877.0     -9.2       5157  Aerospace ...
Apparel         Wolverine ...    2350.0      0.3       3700        Apparel
Business Se...      CoreLogic    1851.0    152.2       5900  Financial ...
Chemicals              Stepan    1925.0     91.6       2096      Chemicals
Energy          Superior E...    1874.0   -205.9       6400  Oil and Ga...
Engineering...       TopBuild    1906.0    158.1       8400  Engineerin...
Financials                HCP    1848.0    414.2        190    Real estate
Food &  Dru...          Freds    2064.0   -140.3       7324  Food and D...
Food, Bever...      Universal    2071.0    106.3      24000        Tobacco
Health Care      Ensign Group    1849.0     40.5      21301  Health Car...
```




The [nth] method extracts rows at a specified index position
within their sector. Remember that the index starts counting at 0. Thus,
invoking the [nth] method with an argument of [0] will
return the *first* company listed within each sector. The result below
is identical to the result returned from invoking the [first]
method.



```
In  [22] sectors.nth(0).head(10)
 
                      Company  Revenues  Profits  Employees       Industry
Sector                                                                   
Aerospace &...         Boeing   93392.0   8197.0     140800  Aerospace ...
Apparel                  Nike   34350.0   4240.0      74400        Apparel
Business Se...  ManpowerGroup   21034.0    545.4      29000  Temporary ...
Chemicals           DowDuPont   62683.0   1460.0      98000      Chemicals
Energy            Exxon Mobil  244363.0  19710.0      71200  Petroleum ...
Engineering...          Fluor   19521.0    191.4      56706  Engineerin...
Financials      Berkshire ...  242137.0  44940.0     377000  Insurance:...
Food &  Dru...         Kroger  122662.0   1907.0     449000  Food and D...
Food, Bever...        PepsiCo   63525.0   4857.0     263000  Food Consu...
Health Care     UnitedHeal...  201159.0  10558.0     260000  Health Car...
```




In the next example, we pass the [nth] method an argument of 3 to
pull out the *fourth* *row* listed for each sector in the
[fortune] `DataFrame`. The results set thus includes the 21
companies that are ranked fourth-best by revenue within their sector.



```
In  [23] sectors.nth(3).head()
 
Out [23]
 
                      Company  Revenues  Profits  Employees       Industry
Sector____________________________________________________________________                                                                    
Aerospace &...  General Dy...   30973.0   2912.0      98600  Aerospace ...
Apparel          Ralph Lauren    6653.0    -99.3      18250        Apparel
Business Se...        Aramark   14604.0    373.9     215000  Diversifie...
Chemicals            Monsanto   14640.0   2260.0      21900      Chemicals
Energy          Valero Energy   88407.0   4065.0      10015  Petroleum ...
```




Notice that the value for the Apparel sector is [\"Ralph
Lauren\"]. We can confirm the output above is correct by filtering
for the Apparel rows from the [fortune] `DataFrame`. Notice
that [\"Ralph Lauren\"] is 4^th^ in line.



```
In  [24] fortune[fortune["Sector"] == "Apparel"].head()
 
Out [24]
 
          Company  Revenues  Profits  Employees   Sector Industry
88           Nike   34350.0   4240.0      74400  Apparel  Apparel
241            VF   12400.0    614.9      69000  Apparel  Apparel
331           PVH    8915.0    537.8      28050  Apparel  Apparel
420  Ralph Lauren    6653.0    -99.3      18250  Apparel  Apparel
432   Hanesbrands    6478.0     61.9      67200  Apparel  Apparel
```




The [head] and [tail] methods can be used to extract
*multiple* rows for each sector within [fortune]. In the next
example, [head(2)] extracts the first *two* rows for each sector
within [fortune]. The result is a `DataFrame` with 42 rows
(21 unique sectors with 2 rows for each sector). Don\'t confuse these
[head] and [tail] methods on the [GroupBy] object with
the equivalent ones on a `DataFrame` object.



```
In  [25] sectors.head(2)
 
Out [25]
 
          Company  Revenues  Profits  Employees        Sector      Industry
0         Walmart  500343.0   9862.0    2300000     Retailing  General M...
1     Exxon Mobil  244363.0  19710.0      71200        Energy  Petroleum...
2    Berkshire...  242137.0  44940.0     377000    Financials  Insurance...
3           Apple  229234.0  48351.0     123000    Technology  Computers...
4    UnitedHea...  201159.0  10558.0     260000   Health Care  Health Ca...
  …             …         …        …          …             …             …
160          Visa   18358.0   6699.0      15000  Business ...  Financial...
162  Kimberly-...   18259.0   2278.0      42000  Household...  Household...
163         AECOM   18203.0    339.4      87000  Engineeri...  Engineeri...
189  Sherwin-W...   14984.0   1772.3      52695     Chemicals     Chemicals
241            VF   12400.0    614.9      69000       Apparel       Apparel
```




The complementary [tail] method extracts the *last* rows for each
sector within [fortune]. For example, [tail(3)] will extract
the *last* three rows for each sector. The result is a 63-row
`DataFrame` (21 sectors x 3 rows).



```
In  [26] sectors.tail(3)
 
Out [26]
 
          Company  Revenues  Profits  Employees        Sector      Industry
473  Windstrea...    5853.0  -2116.6      12979  Telecommu...  Telecommu...
520  Telephone...    5044.0    153.0       9900  Telecommu...  Telecommu...
667  Weis Markets    3467.0     98.4      23000  Food &  D...  Food and ...
759  Hain Cele...    2853.0     67.4       7825  Food, Bev...  Food Cons...
774  Fossil Group    2788.0   -478.2      12300       Apparel       Apparel
  …             …         …        …          …             …             …
995  SiteOne L...    1862.0     54.6       3664   Wholesalers  Wholesale...
996  Charles R...    1858.0    123.4      11800   Health Care  Health Ca...
997     CoreLogic    1851.0    152.2       5900  Business ...  Financial...
998  Ensign Group    1849.0     40.5      21301   Health Care  Health Ca...
999           HCP    1848.0    414.2        190    Financials   Real estate
```




If we wanted to target *all* the rows for a given sector, we can use the
[get\_group] method, which extracts a nested `DataFrame`
from the [GroupBy] object. In the next example, we display all
companies within the [\"Energy\"] sector. Notice that the
[fortune] `DataFrame`\'s **Sector** column is no longer
present in the output; there is no need for it because all companies
listed would have the same value of [\"Energy\"].



```
In  [27] sectors.get_group("Energy").head()
 
Out [27]
 
               Company  Revenues  Profits  Employees            Industry
1          Exxon Mobil  244363.0  19710.0      71200  Petroleum Refining
12             Chevron  134533.0   9195.0      51900  Petroleum Refining
27         Phillips 66   91568.0   5106.0      14600  Petroleum Refining
30       Valero Energy   88407.0   4065.0      10015  Petroleum Refining
40  Marathon Petroleum   67610.0   3432.0      43800  Petroleum Refining
```



Aggregate Operations
------------------------------



The [GroupBy] object can apply an aggregate operation to every
internal group. In the next example, the [sum] method calculates
the sum per sector for all numeric columns (**Revenues**, **Profits**,
**Employees**) in the [fortune] `DataFrame`.



```
In  [28] sectors.sum().head(10)
 
Out [28]
 
                             Revenues   Profits  Employees
Sector____________________________________________________                                                    
Aerospace & Defense          383835.0   26733.5    1010124
Apparel                      101157.3    6350.7     355699
Business Services            316090.0   37179.2    1593999
Chemicals                    251151.0   20475.0     474020
Energy                      1543507.2   85369.6     981207
Engineering & Construction   172782.0    7121.0     420745
Financials                  2442480.0  264253.5    3500119
Food &  Drug Stores          405468.0    8440.3    1398074
Food, Beverages & Tobacco    510232.0   54902.5    1079316
Health Care                 1507991.4   92791.1    2971189
```




Let\'s double-check the calculation. The total sum of revenues across
all companies in the [\"Aerospace & Defense\"] sector is listed as
383,835. We\'ll use the [get\_group] method to retrieve the nested
`DataFrame` that holds all [\"Aerospace & Defense\"]
companies, target its **Revenues** column, and calculate its sum. The
value of 383835.0 is equal to the one in the table above.



```
In  [29] sectors.get_group("Aerospace & Defense").head(2)
 
Out [29]
 
         Company  Revenues  Profits  Employees        Sector      Industry
26        Boeing   93392.0   8197.0     140800  Aerospace...  Aerospace...
50  United Te...   59837.0   4552.0     204700  Aerospace...  Aerospace...
 
In  [30] sectors.get_group("Aerospace & Defense").loc[:,"Revenues"].head(2)
 
Out [30] 26    93392.0
         50    59837.0
         Name: Revenues, dtype: float64
 
In  [31] sectors.get_group("Aerospace & Defense").loc[:, "Revenues"].sum()
 
Out [31] 383835.0
```




In a single [sum] method call, `Pandas` applies the
calculation logic above to *each* nested `DataFrame` in the
[GroupBy] object. It\'s a pretty powerful way to perform an
aggregate analysis of all groups within a column.



The [GroupBy] object has other aggregate methods. In the next
example, we use the [mean] method to calculate the average of the
**Revenues**, **Profits**, and **Employees** columns per sector. Again,
only the numeric columns are targeted in a calculation like this one.



```
In  [32] sectors.mean().head()
 
Out [32]
 
                         Revenues      Profits     Employees
Sector______________________________________________________                                                     
Aerospace & Defense  15353.400000  1069.340000  40404.960000
Apparel               7225.521429   453.621429  25407.071429
Business Services     5963.962264   701.494340  30075.452830
Chemicals             7610.636364   620.454545  14364.242424
Energy               14425.300935   805.373585   9170.158879
```




What if we only wanted to target a single numeric column from
[fortune]? Let\'s see what happens when we pass the column name
inside square brackets after the [GroupBy] object.



```
In  [33] sectors["Revenues"]
 
Out [33] <pandas.core.groupby.generic.SeriesGroupBy object at 0x114778210>
```




Under the hood, `Pandas` is storing a collection of
[SeriesGroupBy] objects. These objects can perform aggregate
operations on an individual column from [fortune], also organized
by sector. In the next two examples, we output the sum of revenues and
average of revenues by sector.



```
In  [34] sectors["Revenues"].sum().head()
 
Out [34] Sector
         Aerospace & Defense     383835.0
         Apparel                 101157.3
         Business Services       316090.0
         Chemicals               251151.0
         Energy                 1543507.2
         Name: Revenues, dtype: float64
 
In  [35] sectors["Revenues"].mean().head()
 
Out [35] Sector
         Aerospace & Defense    15353.400000
         Apparel                 7225.521429
         Business Services       5963.962264
         Chemicals               7610.636364
         Energy                 14425.300935
         Name: Revenues, dtype: float64
```




Other helpful aggregate methods are also available. Th [max]
method returns the maximum value for a given column within
[fortune], organized by sector. In the example below, we extract
the highest profit value per sector. For example, the best-performing
company within the [\"Aerospace & Defense\"] sector has profits of
8197.



```
In  [36] sectors["Profits"].max().head()
 
Out [36] Sector
         Aerospace & Defense     8197.0
         Apparel                 4240.0
         Business Services       6699.0
         Chemicals               3000.4
         Energy                 19710.0
         Name: Profits, dtype: float64
```




The complementary [min] method returns the *minimum* value within
a column, organized by sector. The next example displays the minimum
employee count for a company within a sector. In the [\"Energy\"]
sector, for example, the smallest number of employees that a company has
is 593.



```
In  [37] sectors["Employees"].min().head()
 
Out [37] Sector
         Aerospace & Defense    5157
         Apparel                3700
         Business Services      2338
         Chemicals              1931
         Energy                  593
         Name: Employees, dtype: int64
```




The [agg] method can apply different aggregate operations to
different columns. It accepts a dictionary as its argument, where the
keys represent the column names from the `DataFrame`, and the
values represent the aggregate operation. The next example extracts the
lowest revenue, highest profit, and average number of employees for each
sector.



```
In  [38] aggregations = {
             "Revenues": "min",
             "Profits": "max",
             "Employees": "mean"
         }
 
         sectors.agg(aggregations).head()
 
Out [38]
 
                     Revenues  Profits     Employees
Sector______________________________________________                                              
Aerospace & Defense    1877.0   8197.0  40404.960000
Apparel                2350.0   4240.0  25407.071429
Business Services      1851.0   6699.0  30075.452830
Chemicals              1925.0   3000.4  14364.242424
Energy                 1874.0  19710.0   9170.158879
```



Applying an Operation to all Groups
---------------------------------------------



It\'s likely we\'ll want to apply some custom operations to each nested
group within a [GroupBy] object.



The [GroupBy] object\'s max method can find each sector\'s maximum
revenue *value* but cannot extract the corresponding company row. Let\'s
say we wanted to get the *company* with the highest revenue in *each*
sector. A `DataFrame` has a [nlargest] method that can
extract the rows with the greatest value in a specified columns. Here\'s
a refresher using the [fortune DataFrame.]



```
In  [39] fortune.nlargest(n = 5, columns = "Profits")
 
Out [39]
 
         Company  Revenues  Profits  Employees        Sector      Industry
3          Apple  229234.0  48351.0     123000    Technology  Computers...
2   Berkshire...  242137.0  44940.0     377000    Financials  Insurance...
15       Verizon  126034.0  30101.0     155400  Telecommu...  Telecommu...
8           AT&T  160546.0  29450.0     254000  Telecommu...  Telecommu...
19  JPMorgan ...  113899.0  24441.0     252539    Financials  Commercia...
```




**We\'d like to invoke the** [nlargest method on each nested
DataFrame] within the [GroupBy] object. The apply method is
optimal here. It expects a function as an argument. The cleanest
solution is an anonymous lambda function inline (see the **Python Crash
Course** in the Appendix for a review).



The [apply] method passes [each] grouped `DataFrame`
from the [GroupBy] object into the lambda function.  It then
aggregate the return values returned from the lambda function
invocations. In the next example, we invoke the [nlargest] method
on each `DataFrame` passed in. The method extracts the 1 row with
the greatest value in that [DataFrame\'s] **Revenues** column. The
resulting rows are then aggregated into a new `DataFrame`. Each
sector is listed alongside the company with the highest revenue within
it.



```
In  [40] sectors.apply(lambda df: df.nlargest(1, "Revenues")).head()
 
Out [40]
 
                       Company  Revenues  Profits  Employees      Industry
Sector_____________________________________________________________________                                                                    
Aerospace ... 26         Boeing   93392.0   8197.0     140800  Aerospace...
Apparel       88           Nike   34350.0   4240.0      74400       Apparel
Business S... 142  ManpowerG...   21034.0    545.4      29000  Temporary...
Chemicals     46      DowDuPont   62683.0   1460.0      98000     Chemicals
Energy        1     Exxon Mobil  244363.0  19710.0      71200  Petroleum...
```




Grouping by Multiple Columns
--------------------------------------

A [GroupBy] object can also be created with values from multiple
`DataFrame` columns. Much like with a [MultiIndex], this
operation is optimal when two values can serve as identifiers for a
given grouping. In the next example, we pass a list of strings to the
groupby method to group first by the values in the **Sector** column,
then by the values in the **Industry** column. Remember, a company\'s
industry is a subcategory within a larger sector category.



```
In  [41] sector_and_industry = fortune.groupby(by = ["Sector", "Industry"])
```




The [GroupBy] object\'s [size] method now returns a
[MultiIndex] `Series` with a count of rows within each
internal `DataFrame`. The [GroupBy] object has a length of
82, which means there are 82 unique combinations of sector and industry
within [fortune].



```
In  [42] sector_and_industry.size()
 
Out [42]
 
Sector               Industry                                    
Aerospace & Defense  Aerospace and Defense                            25
Apparel              Apparel                                          14
Business Services    Advertising, marketing                            2
                     Diversified Outsourcing Services                 14
                     Education                                         2
                                                                      ..
Transportation       Trucking, Truck Leasing                          11
Wholesalers          Wholesalers: Diversified                         24
                     Wholesalers: Electronics and Office Equipment     8
                     Wholesalers: Food and Grocery                     6
                     Wholesalers: Health Care                          6
Length: 82, dtype: int64
```




The [get\_group] method now requires a tuple of values to extract
any nested `DataFrame`. In the next example, we target the
companies with a sector of [\"Business Services\"] and an industry
of [\"Education\"].



```
In  [43] sector_and_industry.get_group(("Business Services", "Education"))
 
Out [43]
 
          Company  Revenues  Profits  Employees        Sector   Industry
567  Laureate ...    4378.0     91.5      54500  Business ...  Education
810  Graham Ho...    2592.0    302.0      16153  Business ...  Education
```




All aggregate operations will now return a [MultiIndex DataFrame]
with the calculations. Here, we calculate the sum of the three numeric
columns in [fortune] (**Revenues**, **Profits**, **Employees**),
organized first by sector and then by the industries within each sector.



```
In  [44] sector_and_industry.sum().head()
 
Out [44]
 
                                          Revenues  Profits  Employees
Sector              Industry                                         
Aerospace & Defense Aerospace and Def...  383835.0  26733.5    1010124
Apparel             Apparel               101157.3   6350.7     355699
Business Services   Advertising, mark...   23156.0   1667.4     127500
                    Diversified Outso...   74175.0   5043.7     858600
                    Education               6970.0    393.5      70653
```




Individual columns from [fortune] can be targeted for aggregate
calculations as well. The syntax remains the same; write the column
whose values should be aggregated in square brackets after the
[GroupBy] object, then invoke the aggregation method. The next
example calculates the average of revenues for companies within each
sector / industry combo.



```
In  [45] sector_and_industry["Revenues"].mean().head(5)
 
Out [45]
 
Sector               Industry                       
Aerospace & Defense  Aerospace and Defense               15353.400000
Apparel              Apparel                              7225.521429
Business Services    Advertising, marketing              11578.000000
                     Diversified Outsourcing Services     5298.214286
                     Education                            3485.000000
Name: Revenues, dtype: float64
```




Coding Challenge
--------------------------



Our dataset for the coding challenge, [cereals.csv], is a listing
of 80 popular breakfast cereals. Each row includes the cereal\'s name,
manufacturer, type (hot or cold), as well as the calories, fiber grams,
and sugar grams per serving. Let\'s take a look.



```
In  [46] cereals = pd.read_csv("cereals.csv")
         cereals.head()
 
Out [46]
 
                  Name    Manufacturer  Type  Calories  Fiber  Sugars
0            100% Bran         Nabisco  Cold        70   10.0       6
1    100% Natural Bran     Quaker Oats  Cold       120    2.0       8
2             All-Bran        Kelloggs  Cold        70    9.0       5
3  All-Bran with Ex...        Kelloggs  Cold        50   14.0       0
4       Almond Delight  Ralston Purina  Cold       110    1.0       8
```




Here are the challenges:


1.  [Group the cereals by the manufacturers.
2.  [Determine the total number of groups and the number of cereals per
    group.
3.  [Extract all the cereals that belong to the manufacturer / group of
    [\"Nabisco\"].
4.  [Calculate the averages for all numeric columns (**Calories**,
    **Fiber** and **Sugars**) for the cereals within each
    manufacturer.
5.  [Find the maximum value in the **Sugars** column for each
    manufacturer.
6.  [Find the minimum value in the **Fiber** column for each
    manufacturer.
7.  [Extract the cereal with the lowest amount of sugar grams per
    manufacturer in a new `DataFrame`.


Let\'s dive into it! For \#1, we can invoke the [groupby] method
on our [cereals] `DataFrame`, passing in the column whose
values should be used to create groups.



```
In  [47] manufacturers = cereals.groupby("Manufacturer")
```




To find the total number of groups / manufacturers for Question \#2, we
can pass the resulting [GroupBy] object into Python\'s built-in
[len] function



```
In  [48] len(manufacturers)
 
Out [48] 7
 
The GroupBy object's size method returns a Series with a count of cereals per group.
 
In  [49] manufacturers.size()
 
Out [49] Manufacturer
         American Home Food Products     1
         General Mills                  22
         Kelloggs                       23
         Nabisco                         6
         Post                            9
         Quaker Oats                     8
         Ralston Purina                  8
         dtype: int64
```




Question\#3 asks for all cereals belonging to the [\"Nabisco\"]
group. We can invoke the [get\_group] method on our
[GroupBy] object to return the nested `DataFrame` with
[\"Nabisco\"] rows.



```
In  [50] manufacturers.get_group("Nabisco")
 
Out [50]
 
                        Name Manufacturer  Type  Calories  Fiber  Sugars
0                  100% Bran      Nabisco  Cold        70   10.0       6
20    Cream of Wheat (Quick)      Nabisco   Hot       100    1.0       0
63            Shredded Wheat      Nabisco  Cold        80    3.0       0
64    Shredded Wheat 'n'Bran      Nabisco  Cold        90    4.0       0
65  Shredded Wheat spoon ...      Nabisco  Cold        90    3.0       0
68   Strawberry Fruit Wheats      Nabisco  Cold        90    3.0       5
```




For Question \#4, to calculate the averages of the numeric columns
within [cereals] grouped by manufacturer, we can invoke the
[mean] method on the [manufacturers] [GroupBy] object.
It will aggregate all numeric columns in [cereals] by default.



```
In  [51] manufacturers.mean()
 
Out [51]
 
                               Calories     Fiber    Sugars
Manufacturer_______________________________________________                                              
American Home Food Products  100.000000  0.000000  3.000000
General Mills                111.363636  1.272727  7.954545
Kelloggs                     108.695652  2.739130  7.565217
Nabisco                       86.666667  4.000000  1.833333
Post                         108.888889  2.777778  8.777778
Quaker Oats                   95.000000  1.337500  5.250000
Ralston Purina               115.000000  1.875000  6.125000
```




Question \#5 asks for the maximum sugars value per manufacturer. We can
use square brackets after a [GroupBy] object to identify the
column whose values should be aggregated, then invoke the correct
aggregate method.



```
In  [52] manufacturers["Sugars"].max()
 
Out [52] Manufacturer
         American Home Food Products     3
         General Mills                  14
         Kelloggs                       15
         Nabisco                         6
         Post                           15
         Quaker Oats                    12
         Ralston Purina                 11
         Name: Sugars, dtype: int64
```




The same logic applies for Question \#6. We just have to swap the column
to **Fiber** and invoke the [min] method to identify the smallest
fiber value per manufacturer.



```
In  [53] manufacturers["Fiber"].min()
 
Out [53] Manufacturer
         American Home Food Products    0.0
         General Mills                  0.0
         Kelloggs                       0.0
         Nabisco                        1.0
         Post                           0.0
         Quaker Oats                    0.0
         Ralston Purina                 0.0
         Name: Fiber, dtype: float64
```




The last question asks for the one cereal row from each manufacturer
with the lowest value in the **Sugars** column. We can solve this with a
combination of the apply method, a lambda function, and the nsmallest
method.



```
In  [54] manufacturers.apply(lambda df: df.nsmallest(1, "Sugars"))
 
Out [54]
 
                          Name  Manufacturer  Type  Calories  Fiber  Sugars
Manufacturer_______________________________________________________________                                                              
American H... 43         Maypo  American ...   Hot       100    0.0       3
General Mills 11      Cheerios  General M...  Cold       110    2.0       1
Kelloggs      3   All-Bran ...      Kelloggs  Cold        50   14.0       0
Nabisco       20  Cream of ...       Nabisco   Hot       100    1.0       0
Post          33    Grape-Nuts          Post  Cold       110    3.0       3
Quaker Oats   57  Quaker Oa...   Quaker Oats   Hot       100    2.7      -1
Ralston Pu... 61     Rice Chex  Ralston P...  Cold       110    0.0       2
```





Summary
-----------------


- A `GroupBy` object is a container of
    `DataFrames`.
- The grouped `DataFrames` are organized by a value within one
    or more columns in the original `DataFrame`.
- The `first` and `last` methods return the first and
    last rows from each grouping within the `GroupBy` object. The
    order of the rows within each group is determined by their order in
    the original `DataFrame`.
- The `head` and `tail` methods extract *multiple* rows
    from each group within the `GroupBy` object based on their
    positions in the original `DataFrame`.
- The `nth` method extracts a row from each group within the
    `GroupBy` object by its index position.
- Aggregate calculations such as sum or average will be calculated
    for each group within a `GroupBy` object.
- The `apply` method can be used to apply a consistent
    operation to each `DataFrame` in the `GroupBy`
    object.

