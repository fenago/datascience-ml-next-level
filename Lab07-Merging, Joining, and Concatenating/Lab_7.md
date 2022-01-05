
Lab 7: Merging, joining and concatenating
=========================================

### This lab covers:

- Concatenating `DataFrames`
- Merging `DataFrames` together with inner joins, outer joins and left joins
- Finding unique and shared values between `DataFrames`
- Joining `DataFrames` by column values and index values


Introducing the Datasets
------------------------------

Let\'s begin by importing the `Pandas` library and assigning it
the alias [pd].



```
In  [1] import pandas as pd
```

The CSV files for this lab are stored within a single [meetup]
directory. Let\'s begin with the `members1.csv` and
`member2.csv` files. These are listings of registered users on the
website. Each row include a user\'s unique **member\_id**, full name,
and location (city and state). Here\'s a preview of the first five rows
of `members1.csv`.



```
In  [2] pd.read_csv("meetup/members1.csv").head()
 
Out [2]
 
   member_id       member_name           city state
0          3       Matt Meeker       New York    NY
1          6   Scott Heiferman       New York    NY
2         36        Mark Hurst       New York    NY
3         65  Brad Fitzpatrick  San Francisco    CA
4         82     Maggie Nelson  San Francisco    CA
```




And here\'s a similar view for [members2.csv]. Notice that the two
CSVs have the same four columns. We can imagine that the data for these
two collections was somehow split and stored across two files instead of
one.



```
In  [3] pd.read_csv("meetup/members2.csv").head()
 
Out [3]
 
   member_id              member_name      city state
0  134851222                 Meghan D   Chicago    IL
1  134851522           Caitlin Martin  New York    NY
2  134851802     Jaleesa Stringfellow  New York    NY
3  134852292  Elisabete Melo Coutinho  New York    NY
4  134852562               Dana Veach   Chicago    IL
```




Let\'s import the two `DataFrames` and assign them to numbered
[members] variables. We\'ll come back to these shortly.



```
In  [4] members1 = pd.read_csv("meetup/members1.csv")
        members2 = pd.read_csv("meetup/members2.csv")
```




The [meetup/groups.csv] file is a listing of groups. Each one has
a unique identifier (**group\_id**) and a name. Each group also belongs
to a category, a city, and an organizer; these three columns consist of
foreign keys connecting to other datasets. The **organizer\_id** column
corresponds to the **member\_id** column in the [members]
`DataFrames` we just imported. The organizer is a user who
schedules and manages events for a group.



```
In  [5] pd.read_csv("meetup/groups.csv").head()
 
Out [5]
 
   group_id                  group_name  category_id  city_id  organizer_id
0      6388      Alternative Health NYC           14    10001       1513133
1      6510   Alternative Energy Meetup            4    10001       3955940
2      8458           NYC Animal Rights           26    10001       1809940
3      8940  The New York City Anime...           29    10001       2548151
4     10104          NYC Pit Bull Group           26    10001       1929168
```




Let\'s save this `DataFrame` to a [groups] variable.



```
In  [6] groups = pd.read_csv("meetup/groups.csv")
```




Let\'s come back to the **category\_id** and **city\_id** columns in the
[groups DataFrame]. The foreign keys in these two columns connect
to columns in the [categories.csv] and [cities.csv] files.
The [categories.csv] dataset maps category ids to category names.



```
In  [7] pd.read_csv("meetup/categories.csv").head()
 
Out [7]
 
   category_id            category_name
0            1           Arts & Culture
1            2        Career & Business
2            3       Cars & Motorcycles
3            4  Community & Environment
4            5                  Dancing
 
In  [8] categories = pd.read_csv("meetup/categories.csv")
```




The [cities.csv] dataset holds city information. Each row holds a
unique identifier for the city (**city\_id**) along with its name, state
and zip code.



```
In  [9] pd.read_csv("meetup/cities.csv")
 
Out [9]
 
   city_id            city state    zip
0     7093   West New York    NJ   7093
1    10001        New York    NY  10001
2    13417  New York Mills    NY  13417
3    46312    East Chicago    IN  46312
4    56567  New York Mills    MN  56567
 
In  [10] cities = pd.read_csv("meetup/cities.csv")
```




What about the meetups themselves? Much like the members, they are
stored in two datasets: [events1.csv] and [events2.csv].
Let\'s take a peek at the first one. Each event row includes a unique
event id, the event\'s name, and a foreign key connecting the event to
its associated group.



```
In  [11] pd.read_csv("meetup/events1.csv").head()
 
Out [11]
 
    event_id                                         event_name  group_id
0  153868222  Murder Mystery Dinner Crawl. Dine at 3 Restaur...   5817262
1  184167702  Friday Night Drinks with International Travele...   1627081
2  215200502            Dinner, Comedy, 100 Beers & Debauchery!   1627081
3  220826782                                Friday Night Drinks   5817262
4  227948102  AUSTRALIA DAY PARTY & Sausage Sizzle! $3 Beer/...   1627081
 
In  [12] events1 = pd.read_csv("meetup/events1.csv")
```




The [events2.csv] file has the same four columns as
[events1.csv]. Note that multiple events can share the same
**event\_name** and **group\_id**. This can happen when a group
schedules a recurring event such as a weekly or monthly social. The
**event\_id** will always be unique for each record.



```
In  [13] pd.read_csv("meetup/events2.csv").head()
 
Out [13]
 
       event_id                                   event_name  group_id
0  jrxkxlyxmbgc  NYC Creative and Business Professionals ...  10048442
1  jrxkxlyxnbdc  NYC Creative and Business Professionals ...  10048442
2  jsgfxlywqbhc  NYC Creative and Business Professionals ...   1576097
3  jsgfxlyxcbdc  NYC Creative and Business Professionals ...   1576097
4  jsgfxlyxdbjc  NYC Creative and Business Professionals ...   1576097
 
In  [14] events2 = pd.read_csv("meetup/events2.csv")
```




With our imports complete, we\'re all set to start joining these
datasets together.



Concatenating the Datasets
--------------------------------

For this section, let\'s assume the [members1] and
[members2] `DataFrames` represent the same fundamental
collection of users. Something funny happened during their export, and
the data was split up across two files. We\'d like to combine their rows
into a single `DataFrame`. **Concatenation** refers to the
appending of one [DataFrame\'s] rows to the end of another
`DataFrame`.

The shared column names between the two [members] datasets make
concatenation simple. Invoke the [concat] function at the
top-level of the `Pandas` library. Pass the function\'s
[objs] parameter a list of `DataFrame` objects. The
`DataFrames` will be concatenated in the order they are stored
within the [objs] list. In the next example, the concatenated
`DataFrame` adds the rows from [members2] to the end of the
rows from [members1].



```
In  [15] pd.concat(objs = [members1, members2])
 
Out [15]
 
        member_id       member_name           city state
0               3       Matt Meeker       New York    NY
1               6   Scott Heiferman       New York    NY
2              36        Mark Hurst       New York    NY
3              65  Brad Fitzpatrick  San Francisco    CA
4              82     Maggie Nelson  San Francisco    CA
     …          …                 …              …     …
587918  240845614             Priya       New York    NY
587919  240845866       Eric Seaman       New York    NY
587920  240846998     Janeille Pita       New York    NY
587921  240849026           HU Yang       New York    NY
587922  240852081       James Weitz       New York    NY
```




Let\'s output the lengths of the `DataFrames` to check our work.
Notice that the length of the concatenated `DataFrame` is equal to
the sum of the lengths of the two [members DataFrames].



```
In  [16] len(members1)
 
Out [16] 500000
 
In  [17] len(members2)
 
Out [17] 587923
 
In  [18] len(pd.concat(objs = [members1, members2]))
 
Out [18] 1087923
```




If there are over one million rows in the concatenated
`DataFrame`, why is the final index position above 587,922?
`Pandas` preserves the original index labels from the
[members] `DataFrames` in the concatenated
`DataFrame`. Remember, an index is permitted to have duplicate
values so `Pandas` does not care about the same number being
repeated more than once. We can pass the [ignore\_index] parameter
an argument of True to generate the standard ascending numeric index
starting at 0. Note that the original index labels will be lost.



```
In  [19] pd.concat(objs = [members1, members2], ignore_index = True)
 
Out [19]
 
         member_id     member_name           city state
0                3     Matt Meeker       New York    NY
1                6  Scott Heife...       New York    NY
2               36      Mark Hurst       New York    NY
3               65  Brad Fitzpa...  San Francisco    CA
4               82   Maggie Nelson  San Francisco    CA
      …          …               …              …     …
1087918  240845614           Priya       New York    NY
1087919  240845866     Eric Seaman       New York    NY
1087920  240846998   Janeille Pita       New York    NY
1087921  240849026         HU Yang       New York    NY
1087922  240852081     James Weitz       New York    NY
```


In the next example, the [members1] `DataFrame` is assigned
a key of [\"A\"] and the [members2] `DataFrame` is
assigned a key of [\"B\"]. The [concat] function returns a
[MultiIndex DataFrame] where the first level stores the keys and
the second level stores the index labels from the respective
`DataFrame`.



```
In  [20] pd.concat(objs = [members1, members2], keys = ["A", "B"])
 
Out [20]
          member_id       member_name           city state
A 0               3       Matt Meeker       New York    NY
  1               6   Scott Heiferman       New York    NY
  2              36        Mark Hurst       New York    NY
  3              65  Brad Fitzpatrick  San Francisco    CA
  4              82     Maggie Nelson  San Francisco    CA
       …          …                 …              …     …
B 587918  240845614             Priya       New York    NY
  587919  240845866       Eric Seaman       New York    NY
  587920  240846998     Janeille Pita       New York    NY
  587921  240849026           HU Yang       New York    NY
  587922  240852081       James Weitz       New York    NY
 
1087923 rows × 4 columns
```

Missing values can arise when column names differ between
`DataFrames`. Consider the [df1] and [df2]
`DataFrames` below. The [df1] `DataFrame` has a unique
**A** column and the [df2] `DataFrame` has a unique **C**
column. Both have a **B** column.

```
In  [21] df1 = pd.DataFrame(data = [
                   [1, 2],
                   [3, 4]
               ], columns = ["A", "B"])
 
         df1
 
Out [21]
 
   A  B
0  1  2
1  3  4
 
In  [22] df2 = pd.DataFrame(data = [
                  [5, 6],
                  [7, 8]
               ], columns = ["B", "C"])
 
         df2
 
Out [22]
 
   B  C
0  5  6
1  7  8
```




The concatenation of [df1] and [df2] creates missing values
in the **A** and **C** columns. [df1] has no relevant values to
place in column **C** and [df2] has no relevant values to place in
column **A**. The index labels of 0 and 1 are listed twice. The first
two rows come from [df1] and the last two rows come from
[df2].



```
In  [23] pd.concat(objs = [df1, df2])
 
Out [23]
 
     A  B    C
0  1.0  2  NaN
1  3.0  4  NaN
0  NaN  5  6.0
1  NaN  7  8.0
```




We can also concatenate two `DataFrames` together across the
vertical axis. The columns will be glued together instead of the rows.
The next example concatenates the [df1] and [df2 DataFrames]
on the column axis. The arguments of 1 and [\"columns\"] are
equally valid for the [axis] parameter of the [concat]
function.



```
In  [24] pd.concat(objs = [df1, df2], axis = 1) # is the same as
         pd.concat(objs = [df1, df2], axis = "columns")
 
Out [24]
 
   A  B  B  C
0  1  2  5  6
1  3  4  7  8
```

If one `DataFrame` had index positions that the other one does
not, similar [NaN] values would appear in the concatenation.
Let\'s take a look. We\'ll create another `DataFrame` with **E**
and **F** columns, and index positions 1 and 2.



```
In  [25] df3 = pd.DataFrame(data = [[6, 7], [8, 9]],
                            columns = ["E", "F"],
                            index = [1, 2])
 
         df3
 
Out [25]
 
   E  F
1  6  7
2  8  9
```




Here\'s a reminder of what [df1] looks like.



```
In  [26] df1
 
Out [26]
   A  B
0  1  2
1  3  4
```




The next concatenates [df3] to the end of [df1]. Columns
**A** and **B** are not found in [df3]. Columns **E** and **F**
are not found in [df1]. Once again, `Pandas` will place
[NaN] values in the relevant rows.  In the first two rows (the
rows from [df1]), [NaN] values are placed in columns **E**
and **F. In the last two rows (the rows from** [df3]**),**
[NaN] **values are placed in columns A and B.**



```
In  [27] pd.concat(objs = [df1, df3])
 
Out [27]
 
     A    B    E    F
0  1.0  2.0  NaN  NaN
1  3.0  4.0  NaN  NaN
1  NaN  NaN  6.0  7.0
2  NaN  NaN  8.0  9.0
```




Let\'s pass the [axis] parameter an argument of
[\"columns\".] Now, `Pandas` will glue columns **E** and
**F** from [df3] to the right side of columns **A** and **B** from
[df1]. Both `DataFrames` have a row with index position of
1. That row will be the only one without missing values.



```
In  [28] pd.concat(objs = [df1, df3], axis = "columns")
 
Out [28]
 
     A    B    E    F
0  1.0  2.0  NaN  NaN
1  3.0  4.0  6.0  7.0
2  NaN  NaN  8.0  9.0
```




Inner Joins
-----------------

Let\'s now turn our focus to the [events1] and [events2]
datasets. Let\'s assume the two are *distinct* from each other. For
example, let\'s say the two `DataFrames` reflect meetups across
two separate months. There is a *reason* why the two have been kept
separate. Here\'s a quick reminder of what both datasets look like.



```
In  [29] events1.tail(3)
 
Out [29]
 
          event_id                                   event_name  group_id
2497  jrxkxlyxjbhc  NYC Creative and Business Professionals ...  10048442
2498  jrxkxlyxkbfc  NYC Creative and Business Professionals ...  10048442
2499  jrxkxlyxlbkc  NYC Creative and Business Professionals ...  10048442
 
In  [30] events2.tail(3)
 
Out [30]
 
          event_id                        event_name  group_id
3304  zzsxdlyxlbbc  Chicago Realtor Mastermind Group  18278889
3305  zzsxdlyxmbwb  Chicago Realtor Mastermind Group  18278889
3306  zzsxdlyxnbtb  Chicago Realtor Mastermind Group  18278889
```




There are certain groups that held events across both months. Let\'s
identify them. We have to target the rows from the two
`DataFrames` that have an equal value in their **group\_id**
columns.



The [merge] method merges one `DataFrame` into another. In
this scenario, it doesn\'t matter whether we invoke the method on
[events1] or [events2].  An inner join identifies common
elements in both datasets; the results will be the same in either
direction. For the next example, let\'s call the method on
[events1].



The [right] parameter to the [merge] method expects the
second `DataFrame`. The terminology comes from the previous
diagram. The \"right\" `DataFrame` is the circle on the right, the
second dataset. The [how] parameter expects a string that declares
the type of join; we\'ll pass in [\"inner\"]. `Pandas` also
needs to know the columns that should be used to identify matches.
We\'re lucky in this case because *both* `DataFrames` have a
**group\_id** column. Let\'s pass the column name as a string to the
[on] parameter.



```
In  [31] events1.merge(right = events2,
                       how = "inner",
                       on = "group_id").head()
 
 
Out [31]
 
  event_id_x       event_name_x  group_id    event_id_y       event_name_y
0  153868222  Murder Mystery...   5817262  qrwlqhytcbcc  Drinks with In...
1  220826782  Friday Night D...   5817262  qrwlqhytcbcc  Drinks with In...
2  227967930  AUSTRALIA DAY ...   5817262  qrwlqhytcbcc  Drinks with In...
3  230034070  Dinner, Comedy...   5817262  qrwlqhytcbcc  Drinks with In...
4  184167702  Friday Night D...   1627081  kjmpllytpbfb  Murder Mystery...
```


Let\'s explore the inner join in greater depth to make sure we
understand what just happened. The first 4 rows of the merged
`DataFrame` have a **group\_id** of 5817262. We can filter for
that id in the [events1] and [events2] `DataFrames`.



```
In  [32] events1[events1["group_id"] == 5817262]
 
Out [32]
 
    event_id                                         event_name  group_id
0  153868222  Murder Mystery Dinner Crawl. Dine at 3 Restaur...   5817262
3  220826782                                Friday Night Drinks   5817262
5  227967930  AUSTRALIA DAY PARTY & Sausage Sizzle! $3 Beer/...   5817262
6  230034070       Dinner, Comedy Show, 100 Beers & Debauchery!   5817262
 
In  [33] events2[events2["group_id"] == 5817262]
 
Out [33]
 
          event_id                           event_name  group_id
1419  qrwlqhytcbcc  Drinks with International Travelers   5817262
```




The merged `DataFrame` creates one row for each **group\_id**
match across the two [events] `DataFrames`. There are 4 rows
in [events1] and 1 row in [events2] with a **group\_id** of
5817262. Each of the 4 rows in [events1] is paired with the single
row in [events2]. Thus, a total of 4 rows (4 x 1) are store in the
merged `DataFrame`.  Because an inner join creates a new row for
each combination, the merged `DataFrame` can be significantly
larger in size than the original ones.



The [suffixes] parameter alters the suffixes added to columns from
each respective `DataFrame`. The next example uses
[\"\_M1\"] for month 1 and [\"\_M2\"] for month 2.



```
In  [34] events1.merge(right = events2,
                       how = "inner",
                       on = "group_id",
                       suffixes = ["_M1", "_M2"]).head()
 
Out [34]
 
  event_id_M1      event_name_M1  group_id   event_id_M2      event_name_M2
0   153868222  Murder Mystery...   5817262  qrwlqhytcbcc  Drinks with In...
1   220826782  Friday Night D...   5817262  qrwlqhytcbcc  Drinks with In...
2   227967930  AUSTRALIA DAY ...   5817262  qrwlqhytcbcc  Drinks with In...
3   230034070  Dinner, Comedy...   5817262  qrwlqhytcbcc  Drinks with In...
4   184167702  Friday Night D...   1627081  kjmpllytpbfb  Murder Mystery...
```




We can also pass the [on] parameter a list to identify matches
across multiple columns. In the next example, the merged
`DataFrame` pulls together rows from [events1] and
[events2] that have equal values in both the **group\_id** and
**event\_name** columns. The results reveal which groups scheduled
events with the same name across the two datasets. Remember, even though
an event has a unique **event\_id,** it can still share a **group\_id**
and **event\_name** value with other events.



```
In  [35] events1.merge(right = events2,
                       how = "inner",
                       on = ["group_id", "event_name"],
                       suffixes = [" Month 1", " Month 2"]).head()
 
Out [35]
 
  event_id Month 1   event_name  group_id event_id Month 2
0       244352434   Story Time!   8726642    rhmtpnywnblc
1       244352434   Story Time!   8726642    rhmtpnywpbgb
2       244352434   Story Time!   8726642    rhmtpnywpbhc
3       244352434   Story Time!   8726642    rhmtpnywqbdb
4       244352434   Story Time!   8726642    rhmtpnywqbfc
```




The output above shows only the first 5 matches. There are actually 48
rows in the merged `DataFrame` with an **event\_name** of \"Story
Time!\" and a **group\_id** of 8726642. It looks like there\'s a lot of
recurring events for storytelling fans.



Outer Joins
-----------


Let\'s merge [events1] and [events2] with an outer join. All
group ids from both datasets will be present in the resulting
`DataFrame`. If there is a **group\_id** match between
[events1] and [events2], `Pandas` will merge the
columns from the `DataFrames` together in a single row.
`Pandas` will substitute missing values if a group\_id exists in
one [events] `DataFrame` but not the other.



```
In  [36] events1.merge(right = events2,
                       how = "outer",
                       on = "group_id").head()
 
Out [36]
 
  event_id_x       event_name_x  group_id    event_id_y       event_name_y
0  153868222  Murder Mystery...   5817262  qrwlqhytcbcc  Drinks with In...
1  220826782  Friday Night D...   5817262  qrwlqhytcbcc  Drinks with In...
2  227967930  AUSTRALIA DAY ...   5817262  qrwlqhytcbcc  Drinks with In...
3  230034070  Dinner, Comedy...   5817262  qrwlqhytcbcc  Drinks with In...
4  184167702  Friday Night D...   1627081  kjmpllytpbfb  Murder Mystery...
```


Let\'s take a look at the *last* five rows of the merged
`DataFrame` with the [tail] method. Notice the [NaN]
values in the first two columns.



```
In  [37] events1.merge(right = events2,
                       how = "outer",
                       on = "group_id").tail()
 
Out [37]
 
       event_id_x event_name_x  group_id    event_id_y       event_name_y
281052        NaN          NaN  18278889  zzsxdlyxjbxb  Chicago Realto...
281053        NaN          NaN  18278889  zzsxdlyxkbvb  Chicago Realto...
281054        NaN          NaN  18278889  zzsxdlyxlbbc  Chicago Realto...
281055        NaN          NaN  18278889  zzsxdlyxmbwb  Chicago Realto...
281056        NaN          NaN  18278889  zzsxdlyxnbtb  Chicago Realto...
```




There are group ids that are
present in [events1] that do not exist in [events2]. The
[events1] rows for these groups are still present in the merged
`DataFrame`. The values for the **event\_id** and **event\_name**
columns from [events2] will be [NaN]. Here\'s a sample
extraction of rows from the merged `DataFrame` that shows this.



```
In  [38] events1.merge(right = events2,
                       how = "outer",
                       on = "group_id").iloc[8:13]
 
Out [38]
 
   event_id_x              event_name_x  group_id event_id_y event_name_y
8   233755101  The Founding Moms Exc...   1415286        NaN          NaN
9   241206928  The Founding Moms' Ex...   1415286        NaN          NaN
10  241206937  The Founding Moms' Ex...   1415286        NaN          NaN
11  243650743  The Founding Moms' Ex...   1415286        NaN          NaN
12  244483624  The Founding Moms' Ex...   1415286        NaN          NaN
```




We can pass True to the [indicator] parameter to identify whether
the **group\_id** exists in the left `DataFrame`
([events1]), the right `DataFrame` ([events2]), or
both. The merged `DataFrame` will include a **\_merge** column
that stores the values [\"both\"], [\"left\_only\"], and
[\"right\_only\"].



```
In  [39] events1.merge(right = events2,
                       how = "outer",
                       on = "group_id",
                       indicator = True).head()
 
Out [39]
 
       event_id_x event_name_x  group_id event_id_y event_name_y     _merge
0       153868222  Murder...     5817262  qrwlqh...  Drinks...         both
1       220826782  Friday...     5817262  qrwlqh...  Drinks...         both
2       227967930  AUSTRA...     5817262  qrwlqh...  Drinks...         both
3       230034070  Dinner...     5817262  qrwlqh...  Drinks...         both
4       184167702  Friday...     1627081  kjmpll...  Murder...         both
     …          …          …           …          …          …            … 
281052        NaN        NaN    18278889  zzsxdl...  Chicag...    right_...
281053        NaN        NaN    18278889  zzsxdl...  Chicag...    right_...
281054        NaN        NaN    18278889  zzsxdl...  Chicag...    right_...
281055        NaN        NaN    18278889  zzsxdl...  Chicag...    right_...
281056        NaN        NaN    18278889  zzsxdl...  Chicag...    right_...
```




We can use the **\_merge** column to filter rows based on inclusion in
either of the [events] `DataFrames`. The next example
extracts rows with a value of [\"left\_only\"] in the **\_merge**
column or, equivalently, the rows whose **group\_id** is only present in
[events1], the left `DataFrame`.



```
In  [40] outer_join = events1.merge(right = events2,
                                    how = "outer",
                                    on = "group_id",
                                    indicator = True)
 
         in_left_only = outer_join["_merge"] == "left_only"
 
         outer_join[in_left_only].head()
 
Out [40]
 
   event_id_x     event_name_x  group_id event_id_y event_name_y     _merge
8   233755101  The Founding...   1415286        NaN          NaN  left_only
9   241206928  The Founding...   1415286        NaN          NaN  left_only
10  241206937  The Founding...   1415286        NaN          NaN  left_only
11  243650743  The Founding...   1415286        NaN          NaN  left_only
12  244483624  The Founding...   1415286        NaN          NaN  left_only
```




Left and Right Joins
--------------------


The [groups] dataset is ideal for a left join. Here\'s a quick reminder of what it looks like.



```
In  [41] groups.head(1)
 
Out [41]
 
   group_id              group_name  category_id  city_id  organizer_id
0      6388  Alternative Health NYC           14    10001       1513133
```


Let\'s try a left join. The **category\_id** column in [groups]
references ID values in the [categories] `DataFrame`. Once
again, let\'s invoke the [merge] method. We\'ll pass the
[how] parameter a string of [\"left\"] and the [on]
parameter a string of [\"category\_id\".] We can only use the
[on] parameter because **category\_id** is the column name in both
the [groups] and [categories] `DataFrames`.



```
In  [42] groups.merge(right = categories,
                      how = "left",
                      on = "category_id").head()
 
Out [42]
 
   group_id   group_name  category_id  city_id  organizer_id category_name
0      6388  Alternat...           14    10001      1513133   Health &...
1      6510  Alternat...            4    10001      3955940   Communit...
2      8458  NYC Anim...           26    10001      1809940           NaN
3      8940  The New ...           29    10001      2548151   Sci-Fi &...
4     10104  NYC Pit ...           26    10001      1929168           NaN
```




There it is! The category information is pulled in each for group. Note
that if a **category\_id** value is not found within the
[categories] `DataFrame`, the columns from
[categories] will display [NaN] values. We can see an
example on rows 2 and 4 in the previous output.



The left\_on and right\_on Parameters
-------------------------------------------



So far, the datasets that we\'ve merged together have shared column
names. We have to pass different parameters to the [merge] method
if the column names differ. Let\'s begin by using the [rename]
method to change the column name in the [cities] `DataFrame`
from **city\_id** to **city identifier**.



```
In  [43] cities.head(2)
 
Out [43]
 
   city_id           city state    zip
0     7093  West New York    NJ   7093
1    10001       New York    NY  10001
 
In  [44] cities.rename(columns = { "city_id": "city identifier" },
                       inplace = True)
 
         cities.head(2)
 
Out [44]
 
   city identifier           city state    zip
0            7093   West New York    NJ   7093
1           10001        New York    NY  10001
```




There\'s now a mismatch of column names between [groups] and
[cities]. The [groups] `DataFrame` has a **city\_id**
column of foreign keys that associates with the values in the
**city\_identifier** column in the [cities] `DataFrame`.



We can pass the [left\_on] and [right\_on] parameters to the
[merge] method different strings to indicate the column names in
the respective `DataFrames`. Below, we do a left join to merge
city information into the [groups] `DataFrame`. A few
columns are removed from the output to fit onto the page.



```
In  [45] groups.merge(cities, how = "left",
                      left_on = "city_id",
                      right_on = "city identifier").head()
 
Out [45]
 
   group_id group_name  city_id  city identifier      city state    zip
0      6388  Altern...    10001      10001        New York    NY  10001
1      6510  Altern...    10001      10001        New York    NY  10001
2      8458  NYC An...    10001      10001        New York    NY  10001
3      8940  The Ne...    10001      10001        New York    NY  10001
4     10104  NYC Pi...    10001      10001        New York    NY  10001
```




Unlike the on parameter, the [left\_on] and [right\_on]
parameters will keep both columns from the two `DataFrames`. We
can see the presence of **city\_id** and **city\_identifier** in the
output above.



Merging by Indexes
------------------------



A `DataFrame` that we\'d like to merge into another one may have
its ids stored in its index rather than in a column. Let\'s simulate
this scenario. We can invoke the [set\_index] method on
[members1] to set the **member\_id** column as the
`DataFrame` index.



```
In  [46] members1.head(2)
 
Out [46]
 
   member_id      member_name      city state
0          3      Matt Meeker  New York    NY
1          6  Scott Heiferman  New York    NY
 
In  [47] members1.set_index(keys = "member_id", inplace = True)
         members1.head(2)
 
Out [47]
 
               member_name      city state
member_id_________________________________                                
3              Matt Meeker  New York    NY
6          Scott Heiferman  New York    NY
```




Let\'s merge the [groups] and [members1] `DataFrames`.
Here\'s a quick reminder of what the [groups] `DataFrame`
looks like. The **organizer\_id** column is a collection of foreign keys
that connect to **member\_id** values in the [members1] index. A
left join works well here. We want to compare the values in the
**organizer\_id** column in the [groups] `DataFrame` with
the index values of the [members] `DataFrame`.



```
In  [48] groups.head(2)
 
Out [48]
 
   group_id                 group_name  category_id  city_id  organizer_id
0      6388     Alternative Health NYC           14    10001       1513133
1      6510  Alternative Energy Meetup            4    10001       3955940
```




When we invoke the [merge] method, let\'s pass the
[right\_index] parameter a value of True. This tells
`Pandas` to look for **organizer\_id** matches in the right
[DataFrame\'s] index.



```
In  [49] groups.merge(right = members1,
                      how = "left",
                      left_on = "organizer_id",
                      right_index = True).head()
 
Out [49]
 
   group_id  category_id  city_id  organizer_id member_name      city state
0      6388         14      10001    1513133       Joel E.   New York    NY
1      6510          4      10001    3955940     Yair G...   New York    NY
2      8458         26      10001    1809940        Santos   New York    NY
3      8940         29      10001    2548151     Al Mejias   New York    NY
4     10104         26      10001    1929168           Amy   New York    NY
```




A complementary [left\_index] parameter is also available. Pass
the parameter an argument of True to indicate that the merge should look
for shared values in the index of the \"left\" `DataFrame`, the
one that the [merge] method is invoked upon.



Coding Challenge
----------------------

The datasets for this coding challenge are located within the
[restaurant] folder. This is a collection of tables related to
operations in a fictional dining establishment. The
[week\_1\_sales.csv] and [week\_2\_sales.csv] files are
listings of weekly transactions in the restaurant. Each order associates
a customer with a food item they purchased. Here\'s a preview of the
first 5 rows of [week\_1\_sales]. The [week\_2\_sales] has a
similar shape.



```
In  [50] pd.read_csv("restaurant/week_1_sales.csv").head()
 
Out [50]
 
   Customer ID  Food ID
0          537        9
1           97        4
2          658        1
3          202        2
4          155        9
 
In  [51] week1 = pd.read_csv("restaurant/week_1_sales.csv")
         week2 = pd.read_csv("restaurant/week_2_sales.csv")
```




The **Customer ID** column in the two [week] `DataFrames`
holds foreign keys pointing to the ID column in [customers.csv].
The customers dataset includes each customer\'s first name, last name,
gender, company and occupation. We\'ll import that dataset with the
[read\_csv] method and set its **ID** column as the index with the
[index\_col] parameter.



```
In  [52] pd.read_csv("restaurant/customers.csv", index_col = "ID").head()
 
Out [52]
 
   First Name Last Name  Gender  Company                     Occupation
ID_____________________________________________________________________
1      Joseph   Perkins    Male  Dynazzy  Community Outreach Specialist
2    Jennifer   Alvarez  Female     DabZ        Senior Quality Engineer
3       Roger     Black    Male  Tagfeed              Account Executive
4      Steven     Evans    Male     Fatz               Registered Nurse
5        Judy  Morrison  Female  Demivee                Legal Assistant
 
In  [53] customers = pd.read_csv("restaurant/customers.csv",
                                 index_col = "ID")
```




There\'s another foreign key column in the [weeks]
`DataFrames`. The **Food ID** values connect to the **ID** column
within [foods.csv]. The foods dataset connects an id to a food
item and its price. When we import the dataset, let\'s again set the
**ID** column as the index.



```
In  [54] pd.read_csv("restaurant/foods.csv", index_col = "Food ID")
 
Out [54]
 
          Food Item  Price
Food ID___________________
1             Sushi   3.99
2           Burrito   9.99
3              Taco   2.99
4        Quesadilla   4.25
5             Pizza   2.49
6             Pasta  13.99
7             Steak  24.99
8             Salad  11.25
9             Donut   0.99
10            Drink   1.75
 
In  [55] foods = pd.read_csv("restaurant/foods.csv", index_col = "Food ID")
```




Here are the challenges:


1.  Concatenate the two weeks of sales data into one
    `DataFrame`. Assign the [week1] `DataFrame` a key
    of [\"Week 1\"] and the [week2] `DataFrame` a key
    of [\"Week 2\"].
2.  [ Find the customers who ate at the restaurant during *both*
    weeks.
3.  [ Find the customers who ate at the restaurant during *both* weeks
    and ordered the same item each week.
4.  [ Identify which customers came in on Week 1, Week 2 and both
    weeks.
5.  [ Each row in the [week1] `DataFrame` identifies the
    customer who purchased a food item. Pull in the customer information
    for each row in the `DataFrame`.


Challenge \#1 asks to combine the two weeks of restaurant sales data
into a single `DataFrame`. The [concat] function at the
top-level of the `Pandas` library offers a perfect solution. We
can pass in the two `DataFrames` inside a list to the [objs]
parameter. To assign each `DataFrame` its own key in a MultiIndex,
we\'ll also provide the [keys] parameter a list with the level
labels.



```
In  [56] pd.concat(objs = [week1, week2], keys = ["Week 1", "Week 2"])
 
Out [56]
 
            Customer ID  Food ID
Week 1 0            537        9
       1             97        4
       2            658        1
       3            202        2
       4            155        9
     …   …            …        …
Week 2 245          783       10
       246          556       10
       247          547        9
       248          252        9
       249          249        6
```




Challenge \#2 asks for the customers who visited the restaurant in both
weeks. From a technical perspective, we need to identify the Customer
IDs that are present in *both* the week1 and week2 `DataFrames`.
An inner join is what we\'re looking for here. Let\'s invoke the
[merge] method on [week1] and pass in [week2] as the
right `DataFrame`. We\'ll declare the join type to be
[\"inner\"] and specify [\"Customer ID\"] as the column to
look for shared values in.



```
In  [57] week1.merge(right = week2,
                     how = "inner",
                     on = "Customer ID").head()
 
Out [57]
 
   Customer ID  Food ID_x  Food ID_y
0          537          9          5
1          155          9          3
2          155          1          3
3          503          5          8
4          503          5          9
```




Remember, the inner merge shows all matches of customer IDs across the
two week `DataFrames`. If we wanted a list of just the customers
themselves, we could target the unique values in **Customer ID** column
above.



Challenge \#3 requests the customers who visited the restaurant in both
weeks and ordered the same item. Once again, an inner join is the right
choice for finding values present in both the left and right
`DataFrames`. This time around, however, we have to pass the
[on] parameter a list with two columns. The values in both the
**Customer ID** and **Food ID** columns must match between [week1]
and [week2].



```
In  [58] week1.merge(right = week2,
                     how = "inner",
                     on = ["Customer ID", "Food ID"])
 
Out [58]
 
   Customer ID  Food ID
0          304        3
1          540        3
2          937       10
3          233        3
4           21        4
5           21        4
6          922        1
7          578        5
8          578        5
```




Challenge \#4 wants to differentiate between the customers who came in
both weeks versus the ones who only came in one week. One solution is to
use an outer join and match all records across the two
`DataFrames` by the values in the **Customer ID** column. We can
pass the [indicator] parameter a value of True to add a
**\_merge** column. The column will indicate whether the **Customer ID**
exists in only the left table [(\"left\_only]\"), only the right
table ([\"right\_only\"]), or both ([\"both\"]). Moving
forward, we can create a Boolean `Series` to filter down to one of
the three categories.



```
In  [59] week1.merge(right = week2,
                     how = "outer",
                     on = "Customer ID",
                     indicator = True).head()
 
Out [59]
 
   Customer ID  Food ID_x  Food ID_y     _merge
0          537        9.0        5.0       both
1           97        4.0        NaN  left_only
2          658        1.0        NaN  left_only
3          202        2.0        NaN  left_only
4          155        9.0        3.0       both
```




The last challenge asks to pull in customer information for each
Customer ID in the [week1] table. A left join is the optimal
solution here. Invoke the [merge] method on the [week1]
`DataFrame`, passing in the [customers] `DataFrame` as
the \"right\" dataset. Pass the [how] parameter an argument of
[\"left\"].



The tricky part here is that the customer ids are stored in the
**Customer ID** column of the [week1] `DataFrame` and in the
index values of [customers] `DataFrame`. To solve the
problem, pass the [left\_on] parameter the column name from the
[week1] `DataFrame` and the [right\_index] parameter a
value of True.



```
In  [60] week1.merge(right = customers,
                     how = "left",
                     left_on = "Customer ID",
                     right_index = True).head()
 
Out [60]
 
   Customer ID  Food ID First Name Last Name  Gender    Company Occupation
0        537          9     Cheryl   Carroll  Female   Zoombeat  Regist...
1         97          4     Amanda   Watkins  Female        Ozu  Accoun...
2        658          1    Patrick      Webb    Male  Browsebug  Commun...
3        202          2      Louis  Campbell    Male  Rhynoodle  Accoun...
4        155          9    Carolyn      Diaz  Female   Gigazoom  Databa...
```




Summary
-------------


- A **foreign key** is a value in a dataset that references an
    identifier in another dataset.
- A **join** merges two `DataFrames` together based on some
    logical criteria. Different situations call for different
    joins.
- An **inner join** finds values in common between two
    `DataFrames`.
- An **outer join** combines two `DataFrames` based on values
    in a column, regardless of whether they are exclusive or
    shared.
- A **left join** pulls in information from one `DataFrame`
    into. This is equivalent to a VLOOKUP operation in Excel.

