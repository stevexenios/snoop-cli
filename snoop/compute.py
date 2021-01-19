"""This is the computation file."""
from collections import defaultdict
from statistics import mean
import pandas as pd
import time


class Compute:
    def __init__(self, input_csv_path):
        """
        Description: Initializes class Compute objects.
        Parameter: PATH (path for object to read data from, and hold in memory).
        """
        self.df = pd.read_csv(input_csv_path)
        
    
    def print_head(self, n = 10):
        """
        Description: Function to print out the first n rows of our df. 
        Parameter: n (number of lines to print, with default n = 10).
        """
        print("Printing the head(Top {} rows) of the df: ".format(n))
        print(self.df.head(n))

    
    def print_columns(self):
        """ Description: Function to print out the column labels of the df in memory. """
        print("Printing the column labels in the df: ")
        print(self.df.columns)

    
    def print_memory_usage(self):
        """ Description: Function to print out the memory usage of each column in bytes. """
        print("Printing the memory usage for each column(in bytes): ")
        print(self.df.memory_usage())
    

    def compute(self, output_path = '../out/sitters.csv'):
        """
        Description: Function to recompute data about sitters from available data.
        Parameter: output_path (path of where to store the final output. If output_path is
                   not supplied, use default path = '../out/sitters.csv'). 
        """

        # Columns labels for the final csv
        se = 'Sitter email'
        sn = 'Sitter name'
        ps = 'Profile Score'
        rs = 'Rating Score'
        ss = 'Search Score'


        self.df.columns = ['rating', 'sitter_image', 'end_date', 'text', 'owner_image', 'dogs', sn, 
        'owner', 'start_date', 'sitter_phone_number', se, 'owner_phone_number', 'owner_email', 'response_time_minutes']


        def profile_scorer(sitter_name):
            """
            Description: inner function that calculates the profile score value. 
            Parameter: string (a string value representing the sitter name).
            Returns: float value (limited to 2 decimal places) of Profile Score

            " 5 times the fraction of the English alphabet comprised by the 
            distinct letters in what we've recovered of the sitter's name.
            For example, the sitter name `Leilani R.` has 6 distinct letters."
            """
            # make string all lowercase..to help count distinct
            sitter_name = sitter_name.lower()

            # variable to hold count of distinct characters
            distinct_count = 0

            # check if sitter_name has all characters a-z
            if sitter_name.isalpha():
                # count length of set of distinct characters
                distinct_count = len(set(sitter_name))
            else:
            # if it happens that entire string is not comprised of alphabetical characters..
                distinct_set = set()
                # iterate over each value in the string..and check if isalpha
                for char in sitter_name:
                    if char.isalpha():
                        distinct_set.add(char)
                # assign count of distinct characters to distinct_count
                distinct_count = len(distinct_set)

            # return the Profile Score to 2 decimal places
            return round(5 * (distinct_count / 26.0), 2)


        # setting the column for Profile Score and values associated for each row
        self.df[ps] = self.df.apply(lambda row: profile_scorer(row[sn]), axis = 1)
        print('\nSuccessful completion of calculating Profile Score!')

        # setting the column for Rating Score and values associated for each row
        self.df[rs] = self.df.groupby(sn)['rating'].transform('mean')
        print('Successful completion of calculating Rating Score!')

        # setting the column for frequency of stays..for use in computing Search Score
        self.df['frequency'] = self.df.groupby(sn)[sn].transform('count')
        print('Successful completion of frequency of Stays!')

        # Select only one value, for each sitter..assuming the max is the best approximation
        # So sort df by frequency of stays then remove duplicates
        self.df = self.df.groupby(sn)
        self.df = self.df.head(1)

        # setting the column for Search Score and values associated for each row
        self.df[ss] = self.df.apply(lambda row: (row[ps]*0.5 + row['frequency']*0.25), axis = 1)
        print('Successful completion of calculating Search Score!')


        # Finalize df to 5 columns, with RS and SS column values rounded to 2 decimal places
        # Noticed that the frequency or stay count doesn't go too high such as to cause rating
        # greater than 5, thus left it as is (Without putting flags to collapse value > 5 to 5 or RS).
        self.df = self.df[[se, sn, ps, rs, ss]]
        self.df[rs] = self.df.apply(lambda row: round(row[rs], 2), axis = 1)
        self.df[ss] = self.df.apply(lambda row: round(row[ss], 2), axis = 1)
        print('Successful completion of 5 columns and rounding!')

        
        # Sorting the data frame by:
        # 1. Search Score (descending), 
        # 2. Sitter Name alphabetically (tie-breaker).
        self.df = self.df.sort_values([ss, sn], ascending=[False, True])

        # output to sitters.csv in directory ../out/
        self.df.to_csv(output_path)
        
        # console logs
        print('Output file location: {}'.format(output_path))

    
# file = '../in/reviews.csv'
# d = Compute(file)
# d.compute()
# d.print_columns()
# d.print_memory_usage()
