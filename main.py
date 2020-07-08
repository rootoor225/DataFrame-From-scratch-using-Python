This can be useful for someone who needs help.

Create dataframes zithout libraries or framework using Python


# first of all, we must take each Column as a dictionnary.
# Afterwards, we must consider each sub columns of Columns as list of dictionnary # or dictionnary of list.
# Finally, we must put all them into a big dictionnary.
#
# colk-value is the value (string or integer, or any type else) of coli

BigDICT = dict()

BigDICT = { "Column 1" : { "col1" : [col1-value,col2-value,...,colk-value],
                           "col2" : [col1-value,col2-value,...,colk-value],
                           "col3" : [col1-value,col2-value,...,colk-value],
                           "col4" : [col1-value,col2-value,...,colk-value],
                           ..........
                           "colk-1" : [col1-value,col2-value,...,colk-value],
                           "colk" : [col1-value,col2-value,...,colk-value]
                          },
            "Column k" : { "col1" : [col1-value,col2-value,...,colk2-value],
                           "col2" : [col1-value,col2-value,...,colk2-value],
                           "col3" : [col1-value,col2-value,...,colk2-value],
                           "col4" : [col1-value,col2-value,...,colk2-value],
                           ..........
                          "colk-1" : [col1-value,col2-value,...,colk2-value],
                           "colk" : [col1-value,col2-value,...,colk2-value]
                          },
              ...............................................
             "Column N" : { "col1" : [col1-value,col2-value,...,colkN-value],
                           "col2" : [col1-value,col2-value,...,colkN-value],
                           "col3" : [col1-value,col2-value,...,colkN-value],
                           "col4" : [col1-value,col2-value,...,colkN-value],
                           ..........
                         "colkN-1" : [col1-value,col2-value,...,colkN-value],
                           "colkN" : [col1-value,col2-value,...,colkN-value]
                          }
 }

# access elements

# e.g Access column 1

A = BigDICT["Column 1"]

# access column 1 sub-columns

B = BigDICT["Column 1"]["col 1"]

# access column 1 subcolumn 1 first value

B = BigDICT["Column 1"]["col 1"][0]

# Manipulate more complex accessing elements skills using Python courses or documentation on lists and dictionnary

This code is useful for great beginners or n00bs. It can be modified in order to make it easy to use. I suggest its modification must be as the creation of this dataframe is dynamic. That means we don't know a priori th size of the Columns and their sub-columns
