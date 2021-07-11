
Configuring pandas
=====================

### This lab covers:

- Configuring pandas display settings for both the Notebook and a
    single cell
- Limiting the number of printed `DataFrame` rows and
    columns
- Altering the precision of decimal-point numbers
- Truncating text content in a `DataFrame` cell
- Rounding numeric values when they fall below a floor


Getting and Setting pandas Options
----------------------------------------

Let\'s begin by importing the pandas library and assigning it an alias of `pd`.



```
In  [1] import pandas as pd
```




This lab\'s dataset, `happiness.csv`, is a ranking of the world\'s
nations by happiness. The polling form Gallup gathers the data with
support from the United Nations. Each row includes a nation\'s aggregate
score alongside individual scores for GDP per capita, social support,
life expectancy, and generosity. The dataset holds 6 columns and 156
rows.



```
In  [2] happiness = pd.read_csv("happiness.csv")
        happiness.head()
 
Out [2]
 
       Country  Score  GDP per cap…  Social sup…  Life expect…   Generosity
0      Finland  7.769         1.340        1.587         0.986        0.153
1      Denmark  7.600         1.383        1.573         0.996        0.252
2       Norway  7.554         1.488        1.582         1.028        0.271
3      Iceland  7.494         1.380        1.624         1.026        0.354
4  Netherlands  7.488         1.396        1.522         0.999        0.322
```




Pandas stores its settings in a single `options` object at the top level
of the library. Each option belongs to a parent category. Let\'s start
with the `display` category, which holds settings for the printed
representation of pandas\' data structures.



The top-level `describe_option` function returns the documentation for a
given setting. We pass it a string with the setting\'s name. Let\'s look
into the `max_rows` option, which is nested within the `display` parent
category. The `max_rows` setting configures the maximum number of rows
that pandas prints before it truncates a `DataFrame`.



```
In  [3] pd.describe_option("display.max_rows")
 
        display.max_rows : int
            If max_rows is exceeded, switch to truncate view. Depending on
            `large_repr`, objects are either centrally truncated or printed         
            as a summary view. 'None' value means unlimited.
 
            In case python/IPython is running in a terminal and         
            `large_repr` equals 'truncate' this can be set to 0 and pandas  
            will auto-detect the height of the terminal and print a 
            truncated object which fits the screen height. The IPython 
            notebook, IPython qtconsole, or IDLE do not run in a terminal  
            and hence it is not possible to do correct auto-detection.
           [default: 60] [currently: 60]
```




Notice that the documentation includes the setting\'s default value
*and* its current value at the end of the output.



Pandas uses regular expressions to search for the function\'s argument
amongst the library\'s available settings. As a reminder, a **regular
expression** (RegEx) is a search pattern for text. Pandas will print all
options that match the string argument. The next example passes an
argument of `"max_col"`; there are 2 settings that match the term.



```
In [4] pd.describe_option("max_col")
 
display.max_columns : int
    If max_cols is exceeded, switch to truncate view. Depending on
    `large_repr`, objects are either centrally truncated or printed as
    a summary view. 'None' value means unlimited.
 
    In case python/IPython is running in a terminal and `large_repr`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the width of the terminal and print a truncated object which fits
    the screen width. The IPython notebook, IPython qtconsole, or IDLE
    do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    [default: 20] [currently: 5]
display.max_colwidth : int or None
    The maximum width in characters of a column in the repr of
    a pandas data structure. When the column overflows, a "..."
    placeholder is embedded in the output. A 'None' value means unlimited.
    [default: 50] [currently: 9]
```




While regular expressions are appealing*,* I recommend writing out the
full name of the setting, including its parent category. Explicit code
tends to lead to fewer errors.



There are two ways to get a setting\'s current value. The first is the
`get_option` function at the top level of pandas. Like
`describe_option`, it accepts a string argument with the setting\'s
name. The second approach is to access the parent category and the
specific setting as attributes on the top-level `pd.options` object. The
following example shows the syntax for both strategies. Both lines of
code return 60, which means pandas will truncate any `DataFrame` output
that is greater than 60 rows in length.



```
In  [5] # The two lines below are equivalent
        pd.get_option("display.max_rows")
        pd.options.display.max_rows
 
Out [5] 60
```




Similarly, there are two ways to *set* a new value for a setting. The
`set_option` function at the top-level of pandas accepts the setting as
its first argument and its new value as the second argument.
Alternatively, we can access the equivalent option via attributes on the
`pd.options` object and assign the new value with an equal sign.



```
In  [6] # The two lines below are equivalent
        pd.set_option("display.max_rows", 6)
        pd.options.display.max_rows = 6
```




We\'ve instructed pandas to truncate the `DataFrame` output if it is
longer than 6 rows.



```
In  [7] pd.options.display.max_rows
 
Out [7] 6
```




Let\'s see it in action. The next example asks to see the first 6 rows
of `happiness`. The threshold of 6 max rows is not crossed, so pandas
prints all 6 rows.



```
In  [8] happiness.head(6)
 
Out [8]
 
       Country  Score  GDP per cap…  Social sup…  Life expect…   Generosity
0      Finland  7.769         1.340        1.587         0.986        0.153
1      Denmark  7.600         1.383        1.573         0.996        0.252
2       Norway  7.554         1.488        1.582         1.028        0.271
3      Iceland  7.494         1.380        1.624         1.026        0.354
4  Netherlands  7.488         1.396        1.522         0.999        0.322
5  Switzerland  7.480         1.452        1.526         1.052        0.263
```




Let\'s now cross over the threshold and ask pandas to print the first 7
rows. Pandas evenly divides the rows so that an equal number are visible
*before* and *after* the truncation. It prints 3 rows from the beginning
of the output and 3 rows from the end of the output. It truncates the
middle row in between (index 3).



```
In  [9] happiness.head(7)
 
Out [9]
 
       Country  Score  GDP per cap…  Social sup…  Life expect…   Generosity
0      Finland  7.769         1.340        1.587         0.986        0.153
1      Denmark  7.600         1.383        1.573         0.996        0.252
2       Norway  7.554         1.488        1.582         1.028        0.271
…            …      …             …            …             …            …  
4  Netherlands  7.488         1.396        1.522         0.999        0.322
5  Switzerland  7.480         1.452        1.526         1.052        0.263
6       Sweden  7.343         1.387        1.487         1.009        0.267
 
7 rows × 6 columns
```




The complementary `display.max_columns` option sets the maximum number
of printed *columns*. The default value is 20.



```
In  [10] # The two lines below are equivalent
         pd.get_option("display.max_columns")
         pd.options.display.max_columns
 
In  [10] 20
```




Once again, we can use either the `set_option` function, passing in the
setting name and its new value, or directly access the nested
`max_columns` attribute and assign it a new value.



```
In  [11] # The two lines below are equivalent
         pd.set_option("display.max_columns", 2)
         pd.options.display.max_columns = 2
```




If we set an even number of max columns, pandas will exclude the
truncation column from its column count. The `happiness` `DataFrame` has
6 columns, but the next output only displays 2 of them. Pandas includes
the first and last columns, **Country** and **Generosity**. It also
places a truncation column in between the two.



```
In  [12] happiness.head(7)
 
Out [12]
 
       Country  …  Generosity
0      Finland          0.153
1      Denmark  …       0.252
2       Norway  …       0.271
…            …  …           …
4  Netherlands  …       0.322
5  Switzerland  …       0.263
6       Sweden  …       0.267
 
7 rows × 6 columns
```




If we set an *odd* number of max columns, pandas *will* include the
truncation column in its column count. An odd number ensures an equal
number of columns on both sides of the truncation. The next example sets
`max_columns` to 5. The `happiness` output displays the two leftmost
columns (**Country** and **Score**), the truncation column, and the two
rightmost columns (**Life expectancy** and **Generosity**). Pandas
prints 4 of the original 6 columns.



```
In  [13] # The two lines below are equivalent
         pd.set_option("display.max_columns", 5)
         pd.options.display.max_columns = 5
 
In  [14] happiness.head(7)
 
Out [14]
 
       Country  Score  …  Life expectancy   Generosity
0      Finland  7.769  …            0.986        0.153
1      Denmark  7.600  …            0.996        0.252
2       Norway  7.554  …            1.028        0.271
…            …      …  …                …            …
4  Netherlands  7.488  …            0.999        0.322
5  Switzerland  7.480  …            1.052        0.263
6       Sweden  7.343  …            1.009        0.267
 
7 rows × 6 columns
```




To reset a setting to its original value, pass its name to the
`reset_option` function at the top level of pandas. The next example
brings the `max_rows` setting back to its original value of 60.



```
In  [15] pd.reset_option("display.max_rows")
 
In  [16] pd.get_option("display.max_rows")
 
Out [16] 60
```




Precision
---------------



The `display.precision` option sets the number of digits pandas includes
after the decimal point in a floating-point number. The default value is
6.



```
In  [17] pd.describe_option("display.precision")
 
         display.precision : int
             Floating point output precision (number of significant  
             digits). This is only a suggestion
             [default: 6] [currently: 6]
```




The next example sets the precision to 2. The setting affects values in
all 4 of the floating-point columns in `happiness`.



```
In  [18] # The two lines below are equivalent
         pd.set_option("display.precision", 2)
         pd.options.display.precision = 2
 
In  [19] happiness.head()
 
Out [19]
 
       Country  Score  …  Life expectancy  Generosity
0      Finland   7.77  …             1.34        0.15
1      Denmark   7.60  …             1.38        0.25
2       Norway   7.55  …             1.49        0.27
3      Iceland   7.49  …             1.38        0.35
4  Netherlands   7.49  …             1.40        0.32
 
5 rows × 6 columns
```




The `precision` setting alters only the *presentation* of floating-point
numbers. Pandas preserves the original values within the `DataFrame`. We
can prove this by using the `loc` accessor to extract a sample value
from a floating-point column like **Score**.



```
In  [20] happiness.loc[0, "Score"]
 
   Out [20] 7.769
```




Maximum Column Width
--------------------------



The `display.max_colwidth` setting sets the maximum number of characters
in a cell before pandas truncates the text.



```
In  [21] pd.describe_option("display.max_colwidth")
 
         display.max_colwidth : int or None
             The maximum width in characters of a column in the repr of
             a pandas data structure. When the column overflows, a "..."
             placeholder is embedded in the output. A 'None' value means  
             unlimited.
            [default: 50] [currently: 50]
```




The next example configures pandas to truncate text if its length is
greater than or equal to 9 characters.



```
In  [22] # The two lines below are equivalent
         pd.set_option("display.max_colwidth", 9)
         pd.options.display.max_colwidth = 9
```




Let\'s see what happens when we output `happiness`. Pandas shortens the
final 3 values (Afghanistan, Central African Republic, and South Sudan).
The first two values in the output (Rwanda at 6 characters and Tanzania
at 8 characters) remain unaffected.



```
In  [23] happiness.tail()
 
Out [23]
 
            Country  Score  …  Life expectancy  Generosity
151          Rwanda   3.33  …             0.61        0.22
152        Tanzania   3.23  …             0.50        0.28
153          Afgha…   3.20  …             0.36        0.16
154    Central Afr…   3.08  …             0.10        0.23
155          South…   2.85  …             0.29        0.20
 
5 rows × 6 columns
```




Chop Threshold
--------------------



In some analyses, we may consider values to be insignificant if they are
close to 0. For example, your business domain may consider the value
0.10 to be \"as good as 0\" or \"effectively 0\". The
`display.chop_threshold` option sets a floor that a floating-point value
must cross to have its value printed. Pandas will output any value below
the threshold as 0. The example below sets 0.25 as the chop threshold.



```
In  [24] pd.describe_option("display.chop_threshold") 
 
         display.chop_threshold : float or None
             if set to a float value, all float values smaller then the  
             given threshold will be displayed as exactly 0 by repr and 
             friends.
            [default: None] [currently: None]
 
In  [25] pd.set_option("display.chop_threshold", 0.25)
```




In the next output, notice how pandas prints the values in the **Life
expectancy** and **Generosity** columns for index 154 (0.105 and 0.235,
respectively) as 0.00 in the output.



```
In  [26] happiness.tail()
 
Out [26]
 
            Country  Score  …  Life expectancy  Generosity
151          Rwanda   3.33  …             0.61        0.00
152        Tanzania   3.23  …             0.50        0.28
153     Afghanistan   3.20  …             0.36        0.00
154  Central Afr...   3.08  …             0.00        0.00
155     South Sudan   2.85  …             0.29        0.00
```




Much like the `precision` setting, `chop_threshold` does *not* change
the underlying values in the `DataFrame`, only their printed
representation.



Option Context
--------------------



When we change a setting, we alter the output of *all* Jupyter Notebook
cells we execute afterward. The technical term for a setting like this
is *global*. A global setting persists until we assign a new value to
it. For example, if we set `display.max_columns` to 6, Jupyter will
output `DataFrames` with a maximum of 6 columns for all future cell
executions.



Sometimes, we\'ll want to customize presentation options for only a
*single cell* execution. Pandas\' top-level `option_context` function
can be paired with Python\'s built-in `with` keyword to create a
*context* block. Think of a context block as a temporary execution
environment. The `option_context` function sets *temporary* values for
pandas options while the code inside the block executes; global pandas
settings are *not* affected.



We pass settings to the `option_context` function as sequential
arguments. The next example prints the `happiness` `DataFrame` with:


- the `display.max_columns` option set to 5
- the `display.max_rows` option set to 10
- the `display.precision` option set to 3


Jupyter does not recognize the `with` block\'s contents as the final
statement executed within the Notebook cell. Thus, we use a function
called `display` to make the Notebook output the DataFrame.



```
In  [27] with pd.option_context(
             "display.max_columns", 5, 
             "display.max_rows", 10, 
             "display.precision", 3
         ):
            display(happiness)
Out [27]
 
            Country  Score  …  Life expectancy  Generosity
0           Finland  7.769  …            0.986       0.153
1           Denmark  7.600  …            0.996       0.252
2            Norway  7.554  …            1.028       0.271
3           Iceland  7.494  …            1.026       0.354
4       Netherlands  7.488  …            0.999       0.322
…                 …      …  …                …           …
151          Rwanda  3.334  …            0.614       0.217
152        Tanzania  3.231  …            0.499       0.276
153     Afghanistan  3.203  …            0.361       0.158
154  Central Afr...  3.083  …            0.105       0.235
155     South Sudan  2.853  …            0.295       0.202
```




Because we used the `with` keyword, we *did not* alter global Notebook
settings for these 3 options. They keep their original values.



The `option_context` function helps assign different pandas options to
different cell executions. If you\'d like a uniform presentation for all
output, set the pandas options once in a cell at the top of your Jupyter
Notebook.



Summary
-------------


- The `describe_option` function returns documentation for
    a pandas setting.
- The `set_option` function sets a new value for a setting. We can
    also change a setting by accessing and overwriting attributes on the
    `pd.options` object.
- The `reset_option` function changes a pandas setting back to its
    default value.
- The `display.max_rows` and `display.max_columns` options set the
    numeric thresholds at which pandas truncates rows and columns in the
    output.
- The `display.precision` setting alters the number of digits pandas
    prints after a decimal point.
- The `display.max_colwidth` option sets the numeric threshold at
    which pandas truncates printed characters.
- The `display.chop_threshold` option sets a numeric floor. If values
    do not cross the threshold, pandas will print them as zeroes.
- Pair the `option_context` function and the `with` keyword to create
    a *temporary* execution context for a block. Pandas will set
    configuration options for the block only, not for the whole
    Notebook.
