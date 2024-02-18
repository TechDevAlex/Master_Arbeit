#Database Search Script
#Niko Nagengast
#240218 - v2



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
            df = pd.read_excel(self.file_path, header=[0,1], index_col=[0,1])
            return df
        except Exception as e:
            print("Error loading Excel file:", e)
            return None

    @staticmethod
    def get_attr_indices(df: pd.DataFrame):
        """
        Get the attribute tuples of level 0 indices and the corresponding level 1 indices of the DataFrame as a list.

        Parameters:
        - dataframe (DataFrame): The DataFrame for which to retrieve the level 0 and 1 column names.

        Returns:
        - level_0_index (list): A list of level 0 indices
        - level_1_index (list): A list of level 1 indices corresponding to level 0
        - multi_index_dic (dic): A dictionary of level 0 (key) - level 1 (value) pairs
        """

        level_0_index = df.columns.get_level_values(0).tolist()
        level_0_index_l = []
        for el in range(len(level_0_index)):
            if(level_0_index[el].count(" ") >= 1):
                raise TypeError ('ErrorWhitespace: Check {} for whitespaces!'.format(el))#TODO: Insert as Error-message in Gui
            else:
                attr = level_0_index[el][1:-1].split(',')
                tuple_attr = tuple(elem.strip() for elem in attr)
                level_0_index_l.append(tuple_attr)
        level_0_index = list(dict.fromkeys(level_0_index_l))

        multi_index = df[df.columns.get_level_values(0)].columns.tolist()

        # Dictionary to store second string for each first string
        second_string_dict = {}

        # Iterate through the list of lists
        sublist=[]
        for el in list(multi_index):
            sublist.append(el)

        # Iterate through each tuple in the sublist and store in dictionary
        for first,second in sublist:

            if first in second_string_dict:
                second_string_dict[first].append(second)

            else:
                second_string_dict[first] = [second]

        level_1_index = [second_strings for second_strings in second_string_dict.values()]
        level_1_index = [list(set(el)) for el in level_1_index]


        for el in level_1_index:
            for el1 in el:
                if(el1.count(" ") >= 1):
                    raise TypeError ('ErrorWhitespace: Check {} for whitespaces!'.format(el))#TODO: Insert as Error-message in Gui

        multi_index_dic = {level_0_index[i]: level_1_index[i] for i in range(len(level_0_index))}

        return level_0_index, level_1_index, multi_index_dic

    @staticmethod
    def get_attr_level_0_inf(level_0_index):
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
            #level_0_index = eval(level_0_index)
            attr_names, attr_class, attr_unit, attr_dtype = [t[0] for t in level_0_index], \
                                                            [t[1] for t in level_0_index], \
                                                            [t[2] for t in level_0_index], \
                                                            [t[3] for t in level_0_index]

            # get whitespaces
            attr_names, attr_class, attr_unit, attr_dtype = [n.replace("_", " ") for n in attr_names],\
                                                            [c.replace("_", " ") for c in attr_class], \
                                                            [u.replace("_", " ") for u in attr_unit], \
                                                            [d.replace("_", " ") for d in attr_dtype]

            # get unique values
            attr_class_unique = set(attr_class)

            return attr_names, attr_class, attr_unit, attr_dtype, attr_class_unique,  # TODO: How can we put a nice description as information into the Gui (parameter, unit, information)

        except:
            print('InvalidAttributes: Check naming convention for attributes')


# Example usage:
file_path = os.path.join(os.environ.get('HOME'),'Desktop')

# Create an instance of ExcelLoader with the file path
df = DataFrame(file_path + "/filaments.xlsx")

# Load the Excel file into a DataFrame
df = df.load_excel_to_dataframe()
# Use the class method to get column names as a list
level_0_index,_,_ = DataFrame.get_attr_indices(df)

attr_names, attr_class, attr_unit, attr_dtype, attr_class_unique = DataFrame.get_attr_level_0_inf(level_0_index)

#print(df.columns.get_level_values(0))
#print(df.columns.get_level_values(1))

#df = df.T

#print(df.loc["(properties_change_recycling,ecological,%,float)"].index[2])
#print(df.loc["(properties_change_recycling,ecological,%,float)"].iloc[1][1])
