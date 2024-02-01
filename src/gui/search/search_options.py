import os
import pandas as pd


class DataFrame:
    def __init__(self, file_path, df=None):
        self.file_path = file_path
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

    @classmethod
    def get_attr_tuples(cls, dataframe):
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
                print('ErrorWhitespace: Check {} for whitespaces!'.format(el))#TODO: Insert as Erro-message in Gui
            else:
                attr = el[1:-1].split(',')
                tuple_attr = tuple(elem.strip() for elem in attr)
                attr_tuples.append(tuple_attr)


        return attr_tuples

    @classmethod
    def get_attr_information(cls, attr_tuples):
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








# Example usage:
file_path = os.path.join(os.environ.get('HOME'),'Desktop')




# Create an instance of ExcelLoader with the file path
df = DataFrame(file_path + "/AM_filaments_FFF_small.xlsx")

# Load the Excel file into a DataFrame
df = df.load_excel_to_dataframe()

# Use the class method to get column names as a list
attr_tuples = DataFrame.get_attr_tuples(df)

DataFrame.get_attr_information(attr_tuples)
#print(column_names)

# Display the DataFrame
#if df is not None:
    #print(df.head())




