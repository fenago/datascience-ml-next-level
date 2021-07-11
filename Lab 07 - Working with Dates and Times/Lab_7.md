
Working with dates and times
===============================

### This lab covers:

- Converting string columns to datetime columns
- Accessing date and time information from datetime values
- Rounding dates to week, month, and quarter ends
- Adding and subtracting datetimes from each other

In This lab, we\'ll review Python\'s built-in solutions for
datetimes and how `Pandas` improves upon them with the
[Timestamp] and [Timedelta] objects. We\'ll see how we can
use the library to convert strings to dates, add and subtract offsets of
time, calculate durations, and more. Let\'s dive in.


#### How Python works with datetimes

Let\'s spin up a fresh Jupyter Notebook and import the module along with the `Pandas` library.



```
In  [1]  import datetime as dt
         import pandas as pd
```




Let\'s explore four classes nestled within the module: [date],
[time], [datetime,] and [timedelta].



 A [date] represents a single day in history. The object does not
store either the time of day or the time. The [date] class
constructor accepts [year], [month], and [day]
parameters, all of which are passed sequentially as integers. The three
arguments can also be passed either with keyword arguments. The next
example instantiates a date object for my birthday, April 12th, 1991.
April is the 4^th^ month of the year.



```
In  [2] birthday = dt.date(1991, 4, 12) # is the same as
        birthday = dt.date(year = 1991, month = 4, day = 12)
        birthday
 
Out [2] datetime.date(1991, 4, 12)
```




[year], [month], and [day] attributes are available on
the [date] object.



```
In  [3] birthday.year
 
Out [3] 1991
 
In  [4] birthday.month
 
Out [4] 4
 
In  [5] birthday.month
 
Out [5] 12
```




A date object is **immutable**. Its internal state cannot change once it
has been created. An attempt to overwrite any of the attributes will
raise an [AttributeError] exception.



```
In  [6] birthday.month = 10
 
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-15-2690a31d7b19>
in <module>
----> 1
birthday.month = 10
 
AttributeError: attribute 'month' of 'datetime.date' objects is not writable
```




The complementary [time] class represents a specific time of day,
irrespective of date. The first three parameters accept integer
arguments for the [hour], [minute], and [second]. Like
a [date] object, a [time] object is immutable. The next
example uses a [time] object to model 6:43:25 AM.



```
In  [7] alarm_clock = dt.time(6, 43, 25) # is the same as
        alarm_clock = dt.time(hour = 6, minute = 43, second = 25)
        alarm_clock
 
Out [7] datetime.time(6, 43, 25)
```




0 is the default argument for all three parameters. If a [time]
object is instantiated without any arguments, the hours, minutes, and
seconds will fall back to 0. The [time] will represent  midnight
(12:00:00AM), which is 0 hours, 0 minutes, and 0 seconds into the day.



```
In  [8] dt.time()
 
Out [8] datetime.time(0, 0)
```




The next example passes in 9 for the [hour] parameter, 42 for the
[second] parameter, and no value for the [minute] parameter.
The [time] object uses 0 in the minutes place. The resulting time
is 9:00:42AM.



```
In  [9] dt.time(hour = 9, second = 42)
 
Out [9] datetime.time(9, 0, 42)
```




The [time] constructor is based on a 24-hour clock. To represent a
time in the afternoon or evening, pass in a [hour] value greater
than or equal to 12. The [time] object in the next example
represents 19:43:22 or, equivalently, 7:43:22PM.



```
In  [10] dt.time(hour = 19, minute = 43, second = 22)
 
Out [10] datetime.time(19, 43, 22)
```




The [hour], [minute], and [second] attributes reveal
the internal makeup of a [time] object.



```
In  [11] alarm_clock.hour
 
Out [11] 6
 
In  [12] alarm_clock.minute
 
Out [12] 43
 
In  [13] alarm_clock.second
 
Out [13] 25
```




Next in line is the [datetime] object, which holds both a date and
a time. Its first six parameters represent the [year],
[month], [day], [hour], [minute], and
[second].



```
In  [14] moon_landing = dt.datetime(1969, 7, 20, 22, 56, 20)
         # is the same as
         moon_landing = dt.datetime(year = 1969, month = 7, day = 20,
                                    hour = 22, minute = 56, second = 20)
 
         moon_landing
 
Out [14] datetime.datetime(1969, 7, 20, 22, 56, 20)
```




Arguments are only required for the date-related parameters,
[year], [month], and [day]. The time-related
attributes are optional and default to 0. The next example models
January 1^st^, 2021, at midnight (12:00:00 AM). The [year],
[month], and [day] parameters are passed in explicitly while
the [hour], [minute], and [second] implicitly fall
back to 0.



```
In  [15] dt.datetime(2021, 1, 1)
 
Out [15] datetime.datetime(2020, 1, 1, 0, 0)
```




Finally, we come to the [datetime] module\'s [timedelta]
object, which models a duration, a length of time. All of the
[timedelta] constructor\'s arguments are optional and default to
0. The object will add the times passed to it when calculating the total
duration. In the next example, eight weeks and six days are added for a
total of 62 days (8 weeks \* 7 days + 6). Similarly, 3 hours, 38
minutes, and 12 seconds are summed to 14,292 seconds.



```
In  [16] dt.timedelta(weeks = 8,
                      days = 6,
                      hours = 3,
                      minutes = 58,
                      seconds = 12)
 
Out [16] datetime.timedelta(days=62, seconds=14292)
```




#### How pandas works with datetimes

A [Timestamp] object is instantiated with the same parameters as a
[datetime] object. Day-related parameters like [year],
[month] and [day] parameters are required. Time-related
parameters are optional and default to 0.



```
In  [17] pd.Timestamp(1991, 4, 12) # is the same as
         pd.Timestamp(year = 1991, month = 4, day = 12)
 
Out [17] Timestamp('1991-04-12 00:00:00')
```




`Pandas` considers a [Timestamp] to be equal to a
[date] / [datetime] if the two objects store the same
information.



```
In  [18] (pd.Timestamp(year = 1991, month = 4, day = 12)
            == dt.date(year = 1991, month = 4, day = 12))
 
Out [18] True
 
In  [19] (pd.Timestamp(year = 1991, month = 4, day = 12, minute = 2)
            == dt.datetime(year = 1991, month = 4, day = 12, minute = 2))
 
Out [19] True
```




Any variation in date or time values will make the two objects unequal.
In the next example, we pass a [minute] value of 2 to the
[Timestamp]. Lacking an explicit argument for the [minute]
parameter, the [datetime] falls back to a [minute] value of
0. The two objects are deemed unequal.



```
In  [20] (pd.Timestamp(year = 1991, month = 4, day = 12, minute = 2)
            == dt.datetime(year = 1991, month = 4, day = 12))
 
Out [20] False
```




The [Timestamp] constructor accepts a variety of inputs. Here\'s
where we can start to see some of the flexibility of the object. The
next example passes a *string* into the constructor instead of a
sequence of integers. The string stores a date in the common YYYY-MM-DD
format (4-digit year, 2-digit month, 2-digit day).



```
In  [21] pd.Timestamp("2015-03-31")
 
Out [21] Timestamp('2015-03-31 00:00:00')
```




`Pandas` will attempt to decipher the format of the string date
and parse its datetime information. It is smart enough to recognize the
most common storage formats. The first of the next two examples replaces
the dashes in the date string with slashes. The second one passes a
string in the MM/DD/YYYY format.



```
In  [22] pd.Timestamp("2015/03/31")
 
Out [22] Timestamp('2015-03-31 00:00:00')
 
In  [23] pd.Timestamp("03/31/2015")
 
Out [23] Timestamp('2015-03-31 00:00:00')
```




The string can also include time in a variety of formats.



```
In  [24] pd.Timestamp("2021-03-08 08:35:15")
 
Out [24] Timestamp('2021-03-08 08:35:15')
 
In  [25] pd.Timestamp("2021-03-08 6:13:29 PM")
 
Out [25] Timestamp('2021-03-08 18:13:29')
```




Finally, the Timestamp constructor plays friendly with Python\'s native
date, time, and datetime objects. Let\'s pass in a datetime object
directly.



```
In  [26] pd.Timestamp(dt.datetime(2000, 2, 3, 21, 35, 22))
 
Out [26] Timestamp('2000-02-03 21:35:22')
```




All [datetime] attributes previously mentioned in This lab are
implemented on [Timestamp] objects.



```
In  [27] my_time = pd.Timestamp(dt.datetime(2000, 2, 3, 21, 35, 22))
         my_time.year, my_time.month, my_time.day
 
Out [27] (2000, 2, 3)
 
In  [28] my_time.hour, my_time.minute, my_time.second
 
Out [28] (21, 35, 22)
```




Storing Multiple Timestamps in a DatetimeIndex
-----------------------------------------------------



An **index** refers to the collection of labels attached to a
`Pandas` data structure. The most frequently encountered index
we\'ve seen throughout this text is the [RangeIndex], which holds
a sequence of ascending or descending numeric values. We can access the
index of a `Series` or a `DataFrame` via the [index]
attribute.



```
In  [29] pd.Series([1, 2, 3]).index
 
Out [29] RangeIndex(start=0, stop=3, step=1)
```




Another available index object within the `Pandas` library is
[Index], which stores strings. Notice how the index that
`Pandas` attaches to the `Series` changes based on its
contents.



```
In  [30] pd.Series([1, 2, 3], index = ["A", "B", "C"]).index
 
Out [30] Index(['A', 'B', 'C'], dtype='object')
```




The `DatetimeIndex` is an index for storing [Timestamp]
objects. If we pass a list of [Timestamps] to the `Series`
constructor\'s [index] parameter, a `DatetimeIndex` will
automatically be applied to the `Series`.



```
In  [31] timestamps = [
             pd.Timestamp("2020-01-01"),
             pd.Timestamp("2020-02-01"),
             pd.Timestamp("2020-03-01"),
         ]
 
         pd.Series([1, 2, 3], index = timestamps).index
 
Out [31] DatetimeIndex(['2020-01-01', '2020-02-01', '2020-03-01'],        
         dtype='datetime64[ns]', freq=None)
```




The same rules apply for a list of Python [datetime] objects.



```
In  [32] datetimes = [
             dt.datetime(2020, 1, 1),
             dt.datetime(2020, 2, 1),
             dt.datetime(2020, 3, 1),
         ]
 
         pd.Series([1, 2, 3], index = datetimes).index
 
Out [32] DatetimeIndex(['2020-01-01', '2020-02-01', '2020-03-01'],
         dtype='datetime64[ns]', freq=None)
```




We can also create a `DatetimeIndex` from scratch. Its constructor
is available at the top level of the `Pandas` library. Its
[data] parameter expects an iterable of date values. The dates can
be represented as strings, datetimes, [Timestamps], or even a mix
of data types. `Pandas` will convert all values to equivalent
[Timestamps] and lodge them within the index.



```
In  [33] string_dates = ["2018/01/02", "2016/04/12", "2009/09/07"]
         pd.DatetimeIndex(data = string_dates)
 
Out [33] DatetimeIndex(['2018-01-02', '2016-04-12', '2009-09-07'],
         dtype='datetime64[ns]', freq=None)
 
In  [34] mixed_dates = [dt.date(2018, 1, 2),
                        "2016/04/12",
                        pd.Timestamp(2009, 9, 7)]
 
         dt_index = pd.DatetimeIndex(mixed_dates)
         dt_index
 
Out [34] DatetimeIndex(['2018-01-02', '2016-04-12', '2009-09-07'],  
         dtype='datetime64[ns]', freq=None)
```




Now that we have a `DatetimeIndex` assigned to a [dt\_index]
variable, we can attach it to a `Pandas` data structure. The next
example connects the index to a `Series`.



```
In  [35] s = pd.Series(data = [100, 200, 300], index = dt_index)
         s
 
Out [35] 2018-01-02    100
         2016-04-12    200
         2009-09-07    300
         dtype: int64
```




Date- and time-related operations become possible in `Pandas` only
when our values are stored as [Timestamps] rather than as strings.
`Pandas` can\'t deduce a day of the week from a string like
[\"2018-01-02\"] because it views it as a collection of digits and
dashes, not as an actual date. That\'s why it\'s imperative to convert
all relevant string columns to datetimes when importing a dataset for
the first time.



A `DatetimeIndex` can be sorted in either ascending or descending
order. Below, we invoke the [sort\_index] method on the [s]
`Series` to sort the dates from earliest to latest.



```
In  [36] s.sort_index()
 
Out [36] 2009-09-07    300
         2016-04-12    200
         2018-01-02    100
         dtype: int64
```




`Pandas` is smart enough to account for both dates and times in
any sort of datetime comparison. If two [Timestamps] share the
same date, `Pandas` will compare their hours, their minutes, their
seconds, and so on. A variety of sorting and comparison operations are
available out of the box. The next example uses the less than symbol (\<
) to see if one [Timestamp] occurs earlier then another.



```
In  [37] morning = pd.Timestamp("2020-01-01 11:23:22 AM")
         evening = pd.Timestamp("2020-01-01 11:23:22 PM")
         morning < evening
 
Out [37] True
```




Converting a Column or Index to Store Datetimes
------------------------------------------------------



Our first dataset for this lab, [disney.csv], holds nearly 60
years of stock prices for the Walt Disney Company, one of the world\'s
most recognized entertainment brands. Each row includes a date, the
stock\'s highest and lowest value throughout that day, and the stock\'s
opening and closing price.



```
In  [38] disney = pd.read_csv("disney.csv")
         disney.head()
 
Out [38]
 
         Date      High       Low      Open     Close
0  1962-01-02  0.096026  0.092908  0.092908  0.092908
1  1962-01-03  0.094467  0.092908  0.092908  0.094155
2  1962-01-04  0.094467  0.093532  0.094155  0.094155
3  1962-01-05  0.094779  0.093844  0.094155  0.094467
4  1962-01-08  0.095714  0.092285  0.094467  0.094155
```




Let\'s access the [dtypes] attribute on the `DataFrame`.
Notice that the **Date** column has a data type of \"object\", the
`Pandas` designation for a string. The [read\_csv] method
imports all non-numeric column values as strings by default.



```
In  [39] disney.dtypes
 
Out [38] Date      object
         High     float64
         Low      float64
         Open     float64
         Close    float64
         dtype: object
```




We have to explicit tell `Pandas` which columns\' values to
convert to datetimes. One option is to add a [parse\_dates] parameter to the
[read\_csv] method. It can be passed a list of strings
representing the columns whose values should be parsed as datetimes.



```
In  [40] disney = pd.read_csv("disney.csv", parse_dates = ["Date"])
```




An alternative solution is the [to\_datetime] conversion function
at the top level of the `Pandas` library. The function accepts an
iterable object (i.e., a Python list, tuple, `Series`, index,
etc.), converts its values to datetimes, and returns the new values in a
`DatetimeIndex`. Here\'s a small example.



```
In  [41] string_dates = ["2015-01-01", "2016-02-02", "2017-03-03"]
         dt_index = pd.to_datetime(string_dates)
         dt_index
 
Out [41] DatetimeIndex(['2015-01-01', '2016-02-02', '2017-03-03'],      
         dtype='datetime64[ns]', freq=None)
```




Let\'s try passing the [to\_datetime] function the complete
**Date** `Series` from the [disney] `DataFrame`.



```
In  [42] pd.to_datetime(disney["Date"]).head()
 
Out [42] 0   1962-01-02
         1   1962-01-03
         2   1962-01-04
         3   1962-01-05
         4   1962-01-08
         Name: Date, dtype: datetime64[ns]
```




Now that we have a `Series` of datetimes, we can *overwrite* the
original **Date** string column in the [disney] `DataFrame`.
Remember, the expression on the right side of an equal sign is evaluated
first. In the next code sample, we first generate a datetime
`Series`, then overwrite the original column from which the
datetime values were derived.



```
In  [43] disney["Date"] = pd.to_datetime(disney["Date"])
 
Let's check on the Date column again via the dtypes attribute.
 
In  [44] disney.dtypes
 
Out [44] Date     datetime64[ns]
         High            float64
         Low             float64
         Open            float64
         Close           float64
         dtype: object
```




We now have a datetime column!



Using the DatetimeProperties Object
------------------------------------------


A datetime `Series` holds a special [dt] attribute that
exposes a [DatetimeProperties] object. We can access attributes
and invoke methods on this nested object to extract information from
each datetime value in the column. The [dt] accessor is to
datetime values what the [str] accessor is to string values.
Both specialize in manipulations on a specific *type* of data.



```
In  [45] disney["Date"].dt
 
Out [45] <pandas.core.indexes.accessors.DatetimeProperties object at
         0x116247950>
```




Let\'s begin our exploration of the [DatetimeProperties] object
with the [day] attribute, which pulls out the day from each date.
The values are returned in a new `Series`.



```
In  [46] disney["Date"].head(3)
 
Out [46] 0   1962-01-02
         1   1962-01-03
         2   1962-01-04
         Name: Date, dtype: datetime64[ns]
 
In  [47] disney["Date"].dt.day.head(3)
 
Out [47] 0    2
         1    3
         2    4
         Name: Date, dtype: int64
```




The complementary [month] and [year] attributes return new
`Series` with the months and years from each row value. January
has a [month] value of 1, February has a [month] value of 2,
and so on.



```
In  [48] disney["Date"].dt.month.head(3)
 
Out [48] 0    1
         1    1
         2    1
         Name: Date, dtype: int64
 
In  [49] disney["Date"].dt.year.head(3)
 
Out [49] 0    1962
         1    1962
         2    1962
         Name: Date, dtype: int64
```




We can ask `Pandas` to extract more interesting pieces of
information. One example is the [dayofweek] attribute, which
returns a `Series` of numbers. A 0 marks a Monday, a 1 marks a
Tuesday, and so on up to 6 for Sunday. In the output below, the value of
1 at index position 0 indicates that January 2^nd^, 1962, fell on a
Tuesday.



```
In  [50] disney["Date"].dt.dayofweek.head()
 
Out [50] 0    1
         1    2
         2    3
         3    4
         4    0
         Name: Date, dtype: int64
```




What if we wanted the weekday *name* instead of its number? There\'s no
need to write a custom mapping function; the [day\_name] method
will provide us what we need. Be careful with the syntax. Remember,
invoke the method on the [dt] object, *not* on the `Series`
itself.



```
In  [51] disney["Date"].dt.day_name().head()
 
Out [51] 0      Tuesday
         1    Wednesday
         2     Thursday
         3       Friday
         4       Monday
         Name: Date, dtype: object
```




We can pair these [dt] attributes and methods with other
`Pandas` features for advanced analyses. Here\'s an example.
Let\'s calculate the average performance of the stock for the five
weekdays in the dataset. We\'ll begin by attaching the `Series`
returned from the [dt.day\_name] method to the [disney]
`DataFrame`.



```
In  [52] disney["Day of Week"] = disney["Date"].dt.day_name()
```



We can group the rows based on the values in the new **Day of Week** column.


```
In  [53] group = disney.groupby("Day of Week")
```




We can invoke the [GroupBy] object\'s [mean] method to
calculate the average of values for each grouping.



```
In  [54] group.mean()
 
Out [54]
 
                  High        Low       Open      Close
Day of Week____________________________________________    
Friday       23.767304  23.318898  23.552872  23.554498
Monday       23.377271  22.930606  23.161392  23.162543
Thursday     23.770234  23.288687  23.534561  23.540359
Tuesday      23.791234  23.335267  23.571755  23.562907
Wednesday    23.842743  23.355419  23.605618  23.609873
```




The complementary month\_name method returns a Series with the names of
the months.



```
In  [55] disney["Date"].dt.month_name().head()
 
Out [55] 0    January
         1    January
         2    January
         3    January
         4    January
         Name: Date, dtype: object
```




Some attributes on the [dt] object return Booleans. Imagine we
wanted to explore Disney\'s stock performance at the start of each
quarter in its history. The four quarters of a business year start on
January 1^st^, April 1^st^, July 1^st^, and October 1^st^. The
[is\_quarter\_start] attribute returns a Boolean `Series`
where a True value confirms that the row\'s date fell on a quarter start
day.



```
In  [56] disney["Date"].dt.is_quarter_start.tail()
 
Out [56] 14722    False
         14723    False
         14724    False
         14725     True
         14726    False
         Name: Date, dtype: bool
```




We can use the Boolean `Series` from above to extract the rows
from the [disney] `DataFrame` that fell at the beginning of
a quarter.



```
In  [57] disney[disney["Date"].dt.is_quarter_start].head()
 
Out [57]
 
         Date      High       Low      Open     Close Day of Week
189 1962-10-01  0.064849  0.062355  0.063913  0.062355      Monday
314 1963-04-01  0.087989  0.086704  0.087025  0.086704      Monday
377 1963-07-01  0.096338  0.095053  0.096338  0.095696      Monday
441 1963-10-01  0.110467  0.107898  0.107898  0.110467     Tuesday
565 1964-04-01  0.116248  0.112394  0.112394  0.116248   Wednesday
```




The [is\_quarter\_end] attribute can pull out the dates that fell
at the *end* of a quarter.



```
In  [58] disney[disney["Date"].dt.is_quarter_end].head()
 
Out [58]
 
          Date      High       Low      Open     Close Day of Week
251 1962-12-31  0.074501  0.071290  0.074501  0.072253      Monday
440 1963-09-30  0.109825  0.105972  0.108541  0.107577      Monday
502 1963-12-31  0.101476  0.096980  0.097622  0.101476     Tuesday
564 1964-03-31  0.115605  0.112394  0.114963  0.112394     Tuesday
628 1964-06-30  0.101476  0.100191  0.101476  0.100834     Tuesday
```




The complementary [is\_month\_start] and [is\_month\_end]
methods confirm that a date fell at the beginning or end of a month. The
[is\_year\_start] and [is\_year\_end] methods do the same
for the beginning and end of a year.



Adding and Subtracting Durations of Time
-----------------------------------------------



We can add or subtract consistent durations of time with the
[DateOffset] object, which is available at the top level of the
`Pandas` library. Its constructor accepts keyword parameters for
[years], [months], [days], and more.



```
In  [59] pd.DateOffset(years = 3, months = 4, days = 5)
 
Out [59] <DateOffset: days=5, months=4, years=3>
```




Here\'s a reminder of the first five rows of the [disney
DataFrame].



```
In  [60] disney["Date"].head()
 
Out [60] 0   1962-01-02
         1   1962-01-03
         2   1962-01-04
         3   1962-01-05
         4   1962-01-08
         Name: Date, dtype: datetime64[ns]
```




For the sake of example, let\'s imagine that our recordkeeping system
malfunctioned, and the dates in the **Date** column are off by five
days. We can add a consistent amount of time to each date in a datetime
`Series` with a plus sign ( + ) and a [DateOffset] object.
The plus sign means \"move forward\" or \"into the future\". The next
example adds five days to each date in the **Date** column.



```
In  [61] (disney["Date"] + pd.DateOffset(days = 5)).head()
 
Out [61] 0   1962-01-07
         1   1962-01-08
         2   1962-01-09
         3   1962-01-10
         4   1962-01-13
         Name: Date, dtype: datetime64[ns]
```




Similarly, when paired with a [DateOffset], the minus sign ( - )
subtracts a duration from each date in a datetime `Series`. The
minus signs means \"move backward\" or \"into the past\". Here, we move
each date back by three days.



```
In  [62] (disney["Date"] - pd.DateOffset(days = 3)).head()
 
Out [62] 0   1961-12-30
         1   1961-12-31
         2   1962-01-01
         3   1962-01-02
         4   1962-01-05
         Name: Date, dtype: datetime64[ns]
```




Although it is not present in the visual output above, the
[Timestamp] objects are still storing a time internally. It is a
consistent time of midnight. No explicit value was passed for the
time-related attributes, so the datetimes defaulted to zeroes for hours,
minutes, and seconds. In the next example, we include the [hours]
parameter in [DateOffset] constructor to add ten days and six
hours to each datetime in **Date**. The resulting `Series`
displays the date *and* time.



```
In  [63] (disney["Date"] + pd.DateOffset(days = 10, hours = 6)).head()
 
Out [63] 0   1962-01-12 06:00:00
         1   1962-01-13 06:00:00
         2   1962-01-14 06:00:00
         3   1962-01-15 06:00:00
         4   1962-01-18 06:00:00
         Name: Date, dtype: datetime64[ns]
```




The process works the same away when using the minus sign to subtract a
consistent duration. Here\'s a complex example that subtracts a length
of 1 year, 3 months, 10 days, 6 hours, and 3 minutes from each date.



```
In  [64] (disney["Date"] - pd.DateOffset(years = 1, months = 3, days = 10,
                                         hours = 6, minutes = 3)).head()
 
Out [64] 0   1960-09-21 17:57:00
         1   1960-09-22 17:57:00
         2   1960-09-23 17:57:00
         3   1960-09-24 17:57:00
         4   1960-09-27 17:57:00
         Name: Date, dtype: datetime64[ns]
```




Date Offsets
-------------------



The [DateOffset] object is optimal for adding or subtracting a
*consistent* amount of time to or from each date. Real-world analyses
often demand a more dynamic calculation. Let\'s say we wanted to round
each date to the end of its current month. Each date is a *different*
number of days from the end of its month; a consistent
[DateOffset] addition won\'t suffice.



`Pandas` ships with multiple offset objects, each of which holds
business logic for dynamic time-based calculations. They are contained
in a nested file within the `Pandas` library called
[offsets.py]. Offsets referenced in our Jupyter Notebook have to
be prefixed with their complete path: [pd.tseries.offsets]. To
clarify,


- `Pandas` is the library. It is referenced by the alias
    [pd].
- [tseries] is a **package** within the `Pandas` library.
    A package is just a directory of Python code files. The file we\'re
    looking for is found within the [tseries] folder.
- [offsets.py] is the Python file in which the offset classes
    are defined. The [py] extension is not needed when referencing
    the file in Jupyter Notebook.


One sample offset is [MonthEnd]; it rounds each date to the next
month end. Here\'s a refresher on the last five rows in the **Date**
column.



```
In  [65] disney["Date"].tail()
 
Out [65] 14722   2020-06-26
         14723   2020-06-29
         14724   2020-06-30
         14725   2020-07-01
         14726   2020-07-02
         Name: Date, dtype: datetime64[ns]
```




The addition and subtraction syntax from the previous section can be
applied to offset objects. The next example returns a new `Series`
where each datetime has been rounded to the month-end. The addition sign
moves the date *forward* in time. 



```
In  [66] (disney["Date"] + pd.tseries.offsets.MonthEnd()).tail()
 
Out [66] 14722   2020-06-30
         14723   2020-06-30
         14724   2020-07-31
         14725   2020-07-31
         14726   2020-07-31
         Name: Date, dtype: datetime64[ns]
```




A date cannot be rounded to the same date; there has to be some
movement. Thus, if a date falls at the end of a month, it will be
rounded to the end of the *next* month. For example, 2020-06-30 at index
position 14724 is rounded to 2020-07-31, the *next* available month end.



When paired with an offset, the minus sign moves each date backward in
time. The next example uses the [MonthEnd] offset to round the
dates to the *previous* month end. The first three values (2020-06-26,
2020-06-29, and 2020-06-30) are rounded to 2020-05-31, the last day in
May. The final two values (2020-07-01 and 2020-07-02) are rounded to
2020-06-30, the last day in June.



```
In  [67] (disney["Date"] - pd.tseries.offsets.MonthEnd()).tail()
 
Out [67] 14722   2020-05-31
         14723   2020-05-31
         14724   2020-05-31
         14725   2020-06-30
         14726   2020-06-30
         Name: Date, dtype: datetime64[ns]
```




The complementary [MonthBegin] offset performs similar
calculations for the first date of a month. The next example rounds each
date to the *next* beginning of a month. The first three dates
(2020-06-26, 2020-06-29 and 2020-06-30) are rounded to 2020-07-01, the
beginning of the month of July. The two remaining dates of 2020-07-01
and 2020-07-02, both of which occur in July, are rounded to the first
day of August, 2020-08-01.



```
In  [68] (disney["Date"] + pd.tseries.offsets.MonthBegin()).tail()
 
Out [68] 14722   2020-07-01
         14723   2020-07-01
         14724   2020-07-01
         14725   2020-08-01
         14726   2020-08-01
         Name: Date, dtype: datetime64[ns]
```




When paired with the [MonthBegin] offset, the subtraction sign
rounds a date *backward* to the beginning of a month. In the next
example, the first three dates (2020-06-26, 2020-06-29, and 2020-06-30)
are rounded to the beginning of June, 2020-06-01. The last date,
2020-07-02, is rounded to the beginning of July, 2020-07-01. The curious
case is 2020-07-01 at index position 14725. As mentioned earlier, a date
cannot be rounded to the same date. There has to be some movement in the
given direction. Because there has to be some step backward,
`Pandas` calculates the previous month beginning to be 2020-06-01.



```
In  [69] (disney["Date"] - pd.tseries.offsets.MonthBegin()).tail()
 
Out [69] 14722   2020-06-01
         14723   2020-06-01
         14724   2020-06-01
         14725   2020-06-01
         14726   2020-07-01
         Name: Date, dtype: datetime64[ns]
```




A special set of offsets is available for business time calculations.
Their names always begin with a capital B. For example, the Business
Month End ([BMonthEnd]) offset rounds to the last business day of
the month. The five business days are Monday, Tuesday, Wednesday,
Thursday, and Friday.



Consider the following `Series` of three datetimes. The three
dates fall on a Thursday, Friday, and Saturday, respectively.



```
In  [70] may_dates = ["2020-05-28", "2020-05-29", "2020-05-30"]
         end_of_may = pd.Series(pd.to_datetime(may_dates))
         end_of_may
 
Out [70] 0   2020-05-28
         1   2020-05-29
         2   2020-05-30
         dtype: datetime64[ns]
```




Let\'s compare the [MonthEnd] and [BMonthEnd] offsets. When
paired with the plus sign, the [MonthEnd] offset rounds all three
dates to the last day in May, 2020-05-31. Whether that date falls on a
business day or the weekend is irrelevant.



```
In  [71] end_of_may + pd.tseries.offsets.MonthEnd()
 
Out [71] 0   2020-05-31
         1   2020-05-31
         2   2020-05-31
         dtype: datetime64[ns]
```




The [BMonthEnd] offset returns a different set of results. The
last business day of May 2020 is Friday the 29^th^ (2020-05-29). The
first date in the `Series`, 2020-05-28, is rounded to the 29^th^.
The next date, 2020-05-29, falls *on* the last business day of the
month. Once again, a date cannot be rounded to the same date. 2020-05-29
is thus rounded to the last business day of June, 2020-06-30, a Tuesday.
The last date in the `Series`, 2020-05-30, is a Saturday. There
are no business days left in May, so the date is similarly rounded to
the last business day of June, 2020-06-30.



```
In  [72] end_of_may + pd.tseries.offsets.BMonthEnd()
 
Out [72] 0   2020-05-29
         1   2020-06-30
         2   2020-06-30
         dtype: datetime64[ns]
```




The [pd.tseries.offsets] package includes additional offsets for
rounding to starts and ends of quarters, business quarters, years,
business years, and more. Feel free to explore them in your free time.



The timedelta Object
---------------------------



The [Timestamp] object introduced in the previous sections
represents a moment in time. A separate but related concept when working
with datetimes is duration. A duration like \"1 hour\" represents a
*length* of time. It does not have a specific date or time attached to
it. Duration measures the *distance* or *difference* between two dates.



The [Timedelta] constructor is available at the top level of the
`Pandas` library. Much like the [datetime] module\'s
[timedelta] constructor, it accepts keyword parameters for units
of time like [days], [hours], [minutes], and
[seconds]. It\'s easy to confuse the two objects;
[timedelta] is built into Python, [Timedelta] is built into
`Pandas`. The two are mostly interchangeable when used with
`Pandas` operations.



```
In  [73] duration = pd.Timedelta(days = 8, hours = 7,
                                 minutes = 6, seconds = 5)
         duration
 
Out [73]
Timedelta('8 days 07:06:05')
```




The [to\_timedelta] function at the top-level of the
`Pandas` library converts its argument to a [Timedelta]
object. It is to [Timedeltas] what [to\_datetimes] is to
datetimes. Below, we convert a string to a [Timedelta] object.



```
In  [74] duration = pd.to_timedelta("3 hours, 5 minutes, 12 seconds")
 
Out [74] Timedelta('0 days 03:05:12')
```




We can also pass an integer to the [to\_timedelta] function along
with the [unit] parameter. The [unit] parameter accepts a
string representing the unit of time the number represents. Accepted
arguments include [\"hour\"], [\"day\"], [\"minute\"],
and more.



```
In  [75] pd.to_timedelta(5, unit = "hour")
 
Out [75] Timedelta('0 days 05:00:00')
```




If we pass an iterable object as an argument, the [to\_timedelta]
function will convert all of the iterable\'s values into
[Timedeltas] and return them within a [TimedeltaIndex]
object. A [TimedeltaIndex] is yet another index that
`Pandas` offers out of the box. It can serve as the index of a
data structure or as a column in a `DataFrame`.



```
In  [76] pd.to_timedelta([5, 10, 15], unit = "day")
 
Out [76] TimedeltaIndex(['5 days', '10 days', '15 days'], 
         dtype='timedelta64[ns]', freq=None)
```




Usually, [Timedelta] objects are *derived* rather than created
from scratch. For example, the subtraction of one [Timestamp] from
another will return a [Timedelta] automatically.



```
In  [77] pd.Timestamp("1999-02-05") - pd.Timestamp("1998-05-24")
 
Out [77] Timedelta('257 days 00:00:00')
```




Let\'s import our second dataset for the lab,
[deliveries.csv]. It\'s a record of product shipments for a
fictional company. Each row includes the date an order was placed and
the date it was delivered.



```
In  [78] pd.read_csv("deliveries.csv").head()
 
Out [78]
 
  order_date delivery_date
0    5/24/98        2/5/99
1    4/22/92        3/6/98
2    2/10/91       8/26/92
3    7/21/92      11/20/97
4     9/2/93       6/10/98
 
In  [79] deliveries = pd.read_csv("deliveries.csv")
```




Let\'s practice converting the values in the two columns to datetimes.
One option is invoking the [to\_datetime] function twice, once for
the **order\_date** column, and once for the **delivery\_date** column.
A more Pythonic solution is to use a [for] loop to iterate over
the column names, dynamically reference the column in
[deliveries], use [to\_datetime] to create a
`DatetimeIndex` of [Timestamps], and then overwrite the
original string column.



```
In  [80] for column in ["order_date", "delivery_date"]:
             deliveries[column] = pd.to_datetime(deliveries[column])
 
In  [81] deliveries.head()
 
Out [81]  
 
  order_date delivery_date
0 1998-05-24    1999-02-05
1 1992-04-22    1998-03-06
2 1991-02-10    1992-08-26
3 1992-07-21    1997-11-20
4 1993-09-02    1998-06-10
```




Let\'s calculate the duration of each shipment. It\'s as simple as
subtracting the **order\_date** `Series` from the
**delivery\_date** Series.



```
In  [82] (deliveries["delivery_date"] - deliveries["order_date"]).head()
 
Out [82] 0    257 days
         1   2144 days
         2    563 days
         3   1948 days
         4   1742 days
         dtype: timedelta64[ns]
```




Let\'s attach the new `Series` to the end of the
[deliveries] `DataFrame`.



```
In  [83] deliveries["duration"] =
             (deliveries["delivery_date"] - deliveries["order_date"])
 
         deliveries.head()
 
Out [83]
 
  order_date delivery_date  duration
0 1998-05-24    1999-02-05  257 days
1 1992-04-22    1998-03-06 2144 days
2 1991-02-10    1992-08-26  563 days
3 1992-07-21    1997-11-20 1948 days
4 1993-09-02    1998-06-10 1742 days
 
We now have two columns of datetimes and one column of timedeltas.
 
In  [84] deliveries.dtypes
 
Out [84] order_date        datetime64[ns]
         delivery_date     datetime64[ns]
         duration         timedelta64[ns]
         dtype: object
```




The [Timedeltas] can be added to or subtracted from
[Timestamp] objects. In the next example, we subtract each row\'s
duration from the **delivery\_date** column. Predictably, the results in
the new `Series` are identical to the values in the
**order\_date** column.



```
In  [85] (deliveries["delivery_date"] - deliveries["duration"]).head()
 
Out [85] 0   1998-05-24
         1   1992-04-22
         2   1991-02-10
         3   1992-07-21
         4   1993-09-02
         dtype: datetime64[ns]
```




A plus symbol *adds* a timedelta to a datetime. Let\'s say we wanted to
find out the date of delivery if each package took *twice as long* to
arrive. We can add the [Timedelta] values in the **duration**
column to the [Timestamp] values in the **delivery\_date** column.



```
In  [86] (deliveries["delivery_date"] + deliveries["duration"]).head()
 
Out [86] 0   1999-10-20
         1   2004-01-18
         2   1994-03-12
         3   2003-03-22
         4   2003-03-18
         dtype: datetime64[ns]
```




The [sort\_values] method works with [Timedelta]
`Series`. The next example sorts the **duration** column in
ascending order, from the shortest delivery to the longest one.



```
In  [87] deliveries.sort_values("duration")
 
Out [87]
 
    order_date delivery_date  duration
454 1990-05-24    1990-06-01    8 days
294 1994-08-11    1994-08-20    9 days
10  1998-05-10    1998-05-19    9 days
499 1993-06-03    1993-06-13   10 days
143 1997-09-20    1997-10-06   16 days
  …          …             …         …
152 1990-09-18    1999-12-19 3379 days
62  1990-04-02    1999-08-16 3423 days
458 1990-02-13    1999-11-15 3562 days
145 1990-03-07    1999-12-25 3580 days
448 1990-01-20    1999-11-12 3583 days
```




Mathematical methods are also available on [Timedelta]
`Series`. The next few examples highlight some methods we\'ve used
throughout the course: [max] for the largest value, [min] for
the smallest value, and [mean] for the average.



```
In   [88] deliveries["duration"].max()
 
Out  [88] Timedelta('3583 days 00:00:00')
 
In   [89] deliveries["duration"].min()
 
Out  [89] Timedelta('8 days 00:00:00')
 
In   [90] deliveries["duration"].mean()
 
Out  [90] Timedelta('1217 days 22:53:53.532934')
```




Here\'s the next challenge. Let\'s extract the packages that took over a
year to deliver. We can use the greater than symbol ( \> ) to compare
each value in the **duration** column to a duration. We can actually
specify the length of time as a [Timestamp] or as a string.



```
In   [91] (deliveries["duration"] > pd.Timedelta(days = 365)).head()
          # is the same as
          (deliveries["duration"] > "365 days").head()
 
Out  [91] 0      False
          1       True
          2       True
          3       True
          4       True
          Name: Delivery Time, dtype: bool
```




Let\'s use the Boolean `Series` to filter for the
`DataFrame` rows with a delivery time greater than 365 days.



```
In   [92] deliveries[deliveries["duration"] > "365 days"].head()
 
Out  [92]
 
  order_date delivery_date  duration
1 1992-04-22    1998-03-06 2144 days
2 1991-02-10    1992-08-26  563 days
3 1992-07-21    1997-11-20 1948 days
4 1993-09-02    1998-06-10 1742 days
6 1990-01-25    1994-10-02 1711 days
```




We can get as granular as needed with the string or the
[Timestamp]. The next example includes the days, hours, and
minutes in the comparison duration, with the units of time separated by
commas.



```
In   [93] long_time = (deliveries["duration"]
                       > "2000 days, 8 hours, 4 minutes")
 
          deliveries[long_time].head()
 
Out  [93]
 
   order_date delivery_date  duration
1  1992-04-22    1998-03-06 2144 days
7  1992-02-23    1998-12-30 2502 days
11 1992-10-17    1998-10-06 2180 days
12 1992-05-30    1999-08-15 2633 days
15 1990-01-20    1998-07-24 3107 days
```




Coding Challenge
-----------------------



#### Questions



Citi Bike NYC is New York City\'s official bike-sharing program.
Residents and tourists can pick up and drop off a bicycle at hundreds of
locations around the city. Customers can either pay per ride or sign up
for a long-term subscription program. Ride data is publicly available
and released monthly by the
city(https://www.citibikenyc.com/system-data).
[citibike.csv] is a collection of \~1.9 million rides that
cyclists took in June 2020. For simplicity\'s sake, the dataset has been
modified from its original version. It includes only three columns:
each\'s ride\'s start time and end time, and the user\'s type
(single-ride customer or long-term subscriber). Let\'s import the
dataset and assign it to a [citi\_bike] variable.



```
In  [94] citi_bike = pd.read_csv("citibike.csv")
         citi_bike.head()
 
Out [94]
 
                start_time                 stop_time   user_type
0  2020-06-01 00:00:03.3720  2020-06-01 00:17:46.2080    Customer
1  2020-06-01 00:00:03.5530  2020-06-01 01:03:33.9360  Subscriber
2  2020-06-01 00:00:09.6140  2020-06-01 00:17:06.8330    Customer
3  2020-06-01 00:00:12.1780  2020-06-01 00:03:58.8640    Customer
4  2020-06-01 00:00:21.2550  2020-06-01 00:24:18.9650    Customer
```




The datetime entries in the **start\_time** and **end\_time** column
include the year, month, day, hour, minute, second, and microsecond. A
microsecond is a unit of time equal to one-millionth of a second.



We can use the `info` method to print a summary of the `DataFrame` that
includes the dataset\'s length, the columns\' data types, and the memory
usage. Notice that the two datetime columns have been imported as
strings.



```
In  [95] citi_bike.info()
 
Out [95]
 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1882273 entries, 0 to 1882272
Data columns (total 3 columns):
 #   Column      Dtype
---  ------      -----
 0   start_time  object
 1   stop_time   object
 2   user_type   object
dtypes: object(3)
memory usage: 43.1+ MB
```




Here are the challenges for this section:


1.  [Convert the **start\_time** and **stop\_time** columns to store
    datetime values instead of strings. To optimize the dataset, let\'s
    also convert the **user\_type** column to store categories.
2.  [Count the rides that occurred on each day of the week (i.e.,
    Monday, Tuesday, etc.). Which weekday is the most popular for a bike
    ride? Use the **start\_time** column as your starting point.
3.  [Count the rides per week for each week within the month. To do so,
    round each date in the **start\_time** column to its previous or
    current Monday. Assume each week starts on a Monday and ends on a
    Sunday. Thus, the first week of June would be Monday, June 1st
    through Sunday, June 7th. You\'ll have to think of a clever solution
    here; the offset objects might not work as you expect.
4.  [Calculate the duration of each ride and save the results to a new
    **duration** column.
5.  [Find the average duration of a bike ride.
6.  [Extract the 5 longest bike rides by duration from the
    dataset.


#### Answers



Question \#1 asks to convert the **start\_time** and **end\_time**
column values to datetimes. The [to\_datetime] conversion function
at the top-level of the `Pandas` library is a good option here.
The solution below iterates over a list of the column names with a
[for] loop, passes each column into the [to\_datetime]
function, and overwrites the existing string column with the new
datetime `Series`.



```
In  [96] for column in ["start_time", "stop_time"]:
             citi_bike[column] = pd.to_datetime(citi_bike[column])
```




The **user\_type** column has only two unique values. It\'s an excellent
candidate to convert to a category column. Let\'s extract the
**user\_type** `Series` and invoke the [astype] method on it
with an argument of [\"category.\"] Then, we can overwrite the
original **user\_type** column.



```
In  [97] citi_bike["user_type"] = citi_bike["user_type"].astype("category")
```




Let\'s call the [info] method again to compare the
before-and-after. We\'ve reduced the memory usage of the
`DataFrame` by \~30%. With our two datetime columns, we\'ve also
made it significantly easier to perform datetime analysis.



```
In  [98] citi_bike.info()
 
Out [98]
 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1882273 entries, 0 to 1882272
Data columns (total 3 columns):
 #   Column      Dtype        
---  ------      -----        
 0   start_time  datetime64[ns]
 1   stop_time   datetime64[ns]
 2   user_type   category     
dtypes: category(1), datetime64[ns](2)
memory usage: 30.5 MB
```




Question \#2 asks for a count of bike rides per weekday. There are two
steps to the solution. We first have to extract the weekday from *each*
datetime value in the **start\_time** column, then count the occurrences
of the weekdays. The [dt.day\_name] method returns a Series with
the weekday names for each date.



```
In  [99] citi_bike["start_time"].dt.day_name().head()
 
Out [99] 0    Monday
         1    Monday
         2    Monday
         3    Monday
         4    Monday
        Name: start_time, dtype: object
```




Then, we can invoke the trusty [value\_counts] method on the
returned `Series` to count the weekdays. In June 2020, Tuesday was
the most popular day for a bike ride.



```
In  [100] citi_bike["start_time"].dt.day_name().value_counts()
 
Out [100] Tuesday      305833
          Sunday       301482
          Monday       292690
          Saturday     285966
          Friday       258479
          Wednesday    222647
          Thursday     215176
          Name: start_time, dtype: int64
```




Question \#3 is a challenging one. We need to group each date into its
corresponding \"week\" bucket by rounding it to its previous or current
Monday. The [pd.tseries.offsets.Week] offset might seem promising
here, but it has the potential to round past the date we want.



Consider the start of our dataset. June 1^st^ falls on a Monday. We\'d
like June 1^st^ through June 7^th^ to be included in the same bucket.
But a date cannot be rounded to the same date. If we use the subtraction
sign, we\'ll end up rounding June 1st back to the previous Monday, May
25th.



```
In  [101] (citi_bike["start_time"] - pd.tseries.offsets.Week()).head()
 
Out [101] 0   2020-05-25 00:00:03.372
          1   2020-05-25 00:00:03.553
          2   2020-05-25 00:00:09.614
          3   2020-05-25 00:00:12.178
          4   2020-05-25 00:00:21.255
          Name: start_time, dtype: datetime64[ns]
```




Here\'s a clever solution. We can use the [dayofweek] attribute to
return a `Series` of numbers. A 0 marks a Monday, a 1 marks a
Tuesday, a 6 marks a Sunday, and so on.



```
In  [102] citi_bike["start_time"].dt.dayofweek.head()
 
Out [102] 0    0
          1    0
          2    0
          3    0
          4    0
          Name: start_time, dtype: int64
```




The weekday number also represents the *distance* from the closest
Monday in days. For example, Monday June 1^st^ has a [dayofweek]
value of 0. The date is 0 days away from the closest Monday. Similarly,
Tuesday June 2^nd^ has a [dayofweek] value of 1. The date is 1 day
away from the closest Monday (June 1^st^). If we subtract a number of
days from each date that is equal to the date\'s [dayofweek]
value, we\'ll arrive at a `Series` where each date is rounded to
its respective Monday \"week\" bucket.



```
In  [103] days_away_from_monday = citi_bike["start_time"].dt.dayofweek
 
In  [104] citi_bike["start_time"] - pd.to_timedelta(days_away_from_monday,
                                                    unit='day')
 
Out [104] 0         2020-06-01 00:00:03.372
          1         2020-06-01 00:00:03.553
          2         2020-06-01 00:00:09.614
          3         2020-06-01 00:00:12.178
          4         2020-06-01 00:00:21.255
                               ...         
             1882268   2020-06-29 23:59:41.116
             1882269   2020-06-29 23:59:46.426
             1882270   2020-06-29 23:59:47.477
             1882271   2020-06-29 23:59:53.395
             1882272   2020-06-29 23:59:53.901
             Name: start_time, Length: 1882273, dtype: datetime64[ns]
```




Let\'s save the new `Series` to a
[dates\_rounded\_to\_monday] variable.



```
In  [105] dates_rounded_to_monday = citi_bike["start_time"] -  
              pd.to_timedelta(days_away_from_sunday, unit='day')
```




We\'re halfway there. The dates are rounded to the correct date, but the
[value\_counts] method won\'t work just yet. The differences in
*times* between the dates will lead to them being deemed unequal.



```
In  [106] dates_rounded_to_monday.value_counts().head()
 
Out [106] 2020-06-22 17:17:39.740    3
          2020-06-08 17:17:29.498    3
          2020-06-15 19:24:26.737    3
          2020-06-01 15:40:32.959    3
          2020-06-01 16:23:36.623    3
          Name: start_time, dtype: int64
```




Let\'s use the [dt.date] attribute to return a `Series` with
just the *dates* from each datetime.



```
In  [107] dates_rounded_to_monday.dt.date.head()
 
Out [107] 0    2020-06-01
          1    2020-06-01
          2    2020-06-01
          3    2020-06-01
          4    2020-06-01
          Name: start_time, dtype: object
```




Now that we have the Monday dates by themselves, we can invoke the
[value\_counts] method to count each value\'s occurrences. The
week of Monday June 15^th^ - Sunday June 21^st^ saw the highest number
of bike rides throughout the month.



```
In  [108] dates_rounded_to_monday.dt.date.value_counts()
 
Out [108] 2020-06-15    481211
          2020-06-08    471384
          2020-06-22    465412
          2020-06-01    337590
          2020-06-29    126676
          Name: start_time, dtype: int64
```




Question \#4 asks to calculate the duration of each ride. We can
subtract the datetime values in the **start\_time** column from the
datetime values in the **stop\_time** column. The result will be a
`Series` of [Timedeltas], which we assign to a **duration**
column. Note that the subtraction below would lead to an error if the
columns were storing strings; that\'s why it\'s imperative to convert
them to datetimes first.



```
In  [109] citi_bike["duration"] = (citi_bike["stop_time"] - 
                                       citi_bike["start_time"])
 
          citi_bike.head()
 
Out [109]
 
              start_time              stop_time   user_type        duration
0 2020-06-01 00:00:03... 2020-06-01 00:17:46...    Customer 00:17:42.836000
1 2020-06-01 00:00:03... 2020-06-01 01:03:33...  Subscriber 01:03:30.383000
2 2020-06-01 00:00:09... 2020-06-01 00:17:06...    Customer 00:16:57.219000
3 2020-06-01 00:00:12... 2020-06-01 00:03:58...    Customer 00:03:46.686000
4 2020-06-01 00:00:21... 2020-06-01 00:24:18...    Customer 00:23:57.710000
```




Question 5 asks for the average duration of all bike rides. We can
invoke the [mean] method on the new **duration** column for the
calculation.



```
In  [110] citi_bike["duration"].mean()
 
Out [110] Timedelta('0 days 00:27:19.590506')
```




The final question asks for the 5 longest bike rides in the dataset. One
solution is sorting the **duration** column values in descending order
with the [sort\_values] method, then using the [head] method
to view the first 5 rows. These sessions likely belonged to individuals
who forgot to check in their bikes in after finishing their ride.



```
In  [111] citi_bike["duration"].sort_values(ascending = False).head()
 
Out [111] 50593    32 days 15:01:54.940000
          98339    31 days 01:47:20.632000
          52306    30 days 19:32:20.696000
          15171    30 days 04:26:48.424000
          149761   28 days 09:24:50.696000
          Name: duration, dtype: timedelta64[ns]
```




The [nlargest] method is another option here. It can be invoked on
either the **duration** `Series` or the `DataFrame` as a
whole. Let\'s go with the latter approach here.



```
In  [112] citi_bike.nlargest(n = 5, columns = "duration")
 
Out [112]
 
               start_time          stop_time user_type           duration
50593  2020-06-01 21:3... 2020-07-04 12:3...  Customer 32 days 15:01:5...
98339  2020-06-02 19:4... 2020-07-03 21:2...  Customer 31 days 01:47:2...
52306  2020-06-01 22:1... 2020-07-02 17:4...  Customer 30 days 19:32:2...
15171  2020-06-01 13:0... 2020-07-01 17:2...  Customer 30 days 04:26:4...
149761 2020-06-04 14:3... 2020-07-03 00:0...  Customer 28 days 09:24:5...
```




Summary
--------------


- The `Pandas` `Timestamp` object is a flexible and
    powerful replacement for Python\'s native `datetime`
    object.
- The `dt` accessor on a datetime `Series` reveals a
    `DatetimeProperties` object with attributes and methods for
    extracting information like day, month, weekday name, and
    more.
- The `Timedelta` object represents a duration or a length of
    time. `Timedelta` objects are created when two
    `Timestamp` objects are subtracted from each other.
- The `pd.tseries.offsets` package houses a collection of
    offset objects for dynamically rounding dates to the closest week,
    month, quarter and more. Dates are rounded forwards with the
    addition sign and backwards with the subtraction sign.
- A `DatetimeIndex` is a container for `Timestamp`
    values. It can be assigned as an index or as a column to a data
    structure. The `TimedeltaIndex` is an equivalent container for
    `Timedelta` objects.
- The `to\_datetime` function at the top level of
    `Pandas` converts an iterable of values to a
    `DatetimeIndex` of Timestamps.
