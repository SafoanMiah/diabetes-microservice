import pandas as pd
import numpy as np
from abc import ABC, abstractmethod

class DataPreProcessing:
    def __init__(self, data, processors):
        self.data = data
        self.pipeline = processors #list of methods which are going to be implemented

    def clean(self):
        result = self.data
        for processor in self.pipeline:
            result = processor.process(result)
        return result

# Builder
class DataPreProcessingBuilder:
    def __init__(self):
        self.processors = []
        self.data = None
        self.datetime = None

    #you may note that  load_data datetime_conversion is not decoupled from a component, it's because their purpose is not to clean the entire dataframe.
    def load_df(self, data):
        self.data = data
        return self
    # I did this for datetime_conversion because the clean method applies the processors in self.pipeline to the entire data set and I wanted this to be column specific.

    def null_data(self):
        self.processors.append(NullData()) #adds the class NullData to the list processors in order for it to be implemented on the data
        return self   #if the method is called by the user then the cleaning operation will not be conducted.

    def case_sensitivity(self):
        self.processors.append(CaseSensitivity())
        return self

    def remove_duplicates(self):
        self.processors.append(RemoveDuplicates())
        return self

    def to_string(self):
        self.processors.append(RemoveDuplicates())
        return self

    def build(self):
        return DataPreProcessing(self.data, self.processors) #puts all the components together by giving an instance of the DataProcessing
        # class the necessary instance variables to actually produce something

# Abstract Component
class DataProcessor(ABC): #creates a template for which to create components as the DataPreProcessing builder will always use the .process() method
    @abstractmethod       # by ensuring that all the processors have the same method to implement their cleaning operation we ensure that the DataPreProcessing class can iterate through the processors properly
    def process(self, data):
        pass

# Concrete Component
class NullData(DataProcessor):
    def process(self, data):
        # Implement
        return data.dropna() #drops rows with any missing values

class CaseSensitivity(DataProcessor):
    def process(self,data):
        for column in data.columns: #for loop to check if the column types are objects to avoid an error caused by trying to implement this onto a column with floats or date-times
            if data[column].dtype == "object":
                data[column]= data[column].str.lower()  # makes them all lower case as capital letters and lowercase letters are not processed as the same.
        return data

class RemoveDuplicates(DataProcessor):
    def process(self,data):
        return data.drop_duplicates() #will remove rows based on whether the entire row is a duplicate. There will be columns such as Aggregate, date and even the cpih where multiple rows have the same values.

