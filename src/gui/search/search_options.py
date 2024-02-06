#Database Search Script
#Niko Nagengast
#240201 - v1



#import libraries
import os
import pandas as pd


class DataFrame:
    def __init__(self, file_path: str, df: pd.DataFrame = None):
        self.file_path = file_path #TODO: Adapt to GUI structure
        self.dataframe = df


    def load_excel_to_dataframe(self):
        """
        Load an Excel file into a DataFrame.

        Returns:
        - df: DataFrame containing the data from the Excel file
        """
        try:
            df = pd.read_excel(self.file_path)
            return df
        except Exception as e:
            print("Error loading Excel file:", e)
            return None

    @staticmethod
    def get_attr_tuples(dataframe):
        """
        Get the attribute tuples (column name tuples) of the DataFrame as a list.

        Parameters:
        - dataframe (DataFrame): The DataFrame for which to retrieve the column names.

        Returns:
        - column_names (list): A list of column names.
        """
        attr_tuples=[]

        for el in list(dataframe.columns):
            if(el.count(" ") >= 1):
                print('ErrorWhitespace: Check {} for whitespaces!'.format(el))#TODO: Insert as Error-message in Gui
            else:
                attr = el[1:-1].split(',')
                tuple_attr = tuple(elem.strip() for elem in attr)
                attr_tuples.append(tuple_attr)


        return attr_tuples

    @staticmethod
    def get_attr_information(attr_tuples):
        """
        split the attribute tuples in their groups

        Parameters:
        - attr_tuples (tuples): complete attribute description in a 4-tuple
        (full_name,descriptive,-,main_polymer_group_of_the_material)

        Returns:
        - attribute_names (list): list of attribute parameters - actual column name
        - attribute_class (list): list of atrriute class names - high-level category
        - attr_unit (list): list of parameter units
        - attr_info (list): list of short explanation parameter
        - attr_class_unique (list): list of unique attribute class names
        """
        attr_names, attr_class, attr_unit, attr_info = [], [], [], []
        try:
            attr_names, attr_class, attr_unit, attr_info = [t[0] for t in attr_tuples], [t[1] for t in attr_tuples],\
                                                           [t[2] for t in attr_tuples], [t[3] for t in attr_tuples]
            for t in attr_tuples:
                attr_names.append(t[0])
                attr_class.append(t[1])
                attr_unit.append(t[2])
                attr_info.append(t[3])

            #get whitespaces
            attr_names, attr_class, attr_unit, attr_info = [n.replace("_", " ") for n in attr_names], \
                                                           [c.replace("_", " ") for c in attr_class],\
                                                           [u.replace("_", " ") for u in attr_unit], \
                                                           [i.replace("_", " ") for i in attr_info]

            #get unique high level attribue classes
            attr_class_unique = set(attr_class)

            return attr_names, attr_class, attr_unit, attr_info, attr_class_unique #TODO: How can we put a nice description as information into the Gui (parameter, unit, information)

        except:
            print('InvalidAttributes: Check naming convention for attributes')



class Search:
    def __init__(self, df: DataFrame = None, sel_attr: list = None, attr: list = None, weights: list = None):
        self.df = df
        self.attr = attr
        self.weights = weights
        self.sel_attr = sel_attr

    #TODO: Check how to store the selected attributes in a list from the user | perhaps for the beginning a max. of 10 parameters
    # TODO: Get a zipped list from the user with ('parameter',importance (1-10)
    def weight(self):
        weight_l = []
        attr_length = len(self.sel_attr)
        # Sum the second elements of each tuple
        total_sum = sum(second_tuple[1] for second_tuple in sel_attr)
        for el in self.sel_attr:
            weight = el[1]/total_sum
            weight_l.append(weight)
        print(weight_l)
        return attr_length


        #simple single search


        #simple weighted search (multiple)
        #cumulative search
        #geographic search
        #material comparison

'''
class DataModification(DataFrame): #TODO: should it be in the dataframe class
    def __init__(self, file_path, df):
        super()__init__(self,file_path,df)

        #concatenation
        #row entry
        #column entry
        #multiple entries
        #error handling
'''


# Example usage:
file_path = os.path.join(os.environ.get('HOME'),'Desktop')

# Create an instance of ExcelLoader with the file path
df = DataFrame(file_path + "/AM_filaments_FFF_small.xlsx")

# Load the Excel file into a DataFrame
df = df.load_excel_to_dataframe()

# Use the class method to get column names as a list
attr_tuples = DataFrame.get_attr_tuples(df)

attr_names, attr_class, attr_unit, attr_info, attr_class_unique = DataFrame.get_attr_information(attr_tuples)

sel_attr = [('youngs_modulus',10), ('yield_point',3), ('elongation_at_break',7)]

search_1 = Search(df,sel_attr)

#get weight amount

amount = search_1.weight()
print(amount)



