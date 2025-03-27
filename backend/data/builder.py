from abc import ABC, abstractmethod


class DataPreProcessing:
    def __init__(self, data, processors):
        self.data = data
        self.pipeline = processors  # list of methods which are going to be implemented

    def clean(self):
        result = self.data
        for (
            processor
        ) in self.pipeline:  # applies the different processors to the dataframe
            result = processor.process(result)
        return result


# Builder
class DataPreProcessingBuilder:
    def __init__(self):
        self.processors = []
        self.data = None

    # you may note that  load_data is not decoupled from a component, it's because their purpose is not to clean the entire dataframe.
    def load_df(self, data):
        self.data = data  # it's simply providing the data for the rest of the processors to clean.
        return self

    def null_data(self):
        self.processors.append(
            NullData()
        )  # adds the class NullData to the list processors in order for it to be implemented on the data
        return self  # if the method is called by the user then the cleaning operation will not be conducted.

    def remove_duplicates(self):
        self.processors.append(RemoveDuplicates())
        return self

    def to_float(self):
        self.processors.append(ConversiontoFloats())
        return self

    def drop_column(self, column):
        self.processors.append(DropColumn(column))
        return self

    def rename_column(self, column, new_column):
        self.processors.append(RenameColumn(column, new_column))
        return self

    def build(self):
        return DataPreProcessing(
            self.data, self.processors
        ).clean()  # puts all the components together by giving an instance of the DataProcessing
        # class the necessary instance variables to actually produce something


# Abstract Component
class DataProcessor(
    ABC
):  # creates a template for which to create components as the DataPreProcessing builder will always use the .process() method
    @abstractmethod  # by ensuring that all the processors have the same method to implement their cleaning operation we ensure that the DataPreProcessing class can iterate through the processors properly
    def process(self, data):
        pass


# Concrete Component
class NullData(DataProcessor):
    def process(self, data):
        # Implement
        return data.dropna()  # drops rows with any missing values


class RemoveDuplicates(DataProcessor):
    def process(self, data):
        return data.drop_duplicates()  # will remove rows based on whether the entire row is a duplicate. There will be columns such as Aggregate, date and even the cpih where multiple rows have the same values.


class ConversiontoFloats(DataProcessor):
    def process(self, data):
        return data.astype(float)


class DropColumn(DataProcessor):
    def __init__(self, column):
        self.column = column  # the way the processor is set up is it's a loop that will apply to the entire dataframe and so the picking of a specific column to drop is easier implemented here.

    def process(self, data):
        return data.drop([self.column], axis=1)


class RenameColumn(DataProcessor):
    def __init__(self, column, new_name):
        self.column = column  # the way the processor is set up is it's a loop that will apply to the entire dataframe and so the picking of a specific column to drop is easier implemented here.
        self.new_name = new_name

    def process(self, data):
        return data.rename(columns={self.column: self.new_name})
