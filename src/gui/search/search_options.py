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

            #get whitespaces
            attr_names, attr_class, attr_unit, attr_info = [n.replace("_", " ") for n in attr_names], \
                                                           [c.replace("_", " ") for c in attr_class],\
                                                           [u.replace("_", " ") for u in attr_unit], \
                                                           [i.replace("_", " ") for i in attr_info]

            #get unique values
            attr_class_unique = set(attr_class)


            return attr_names, attr_class, attr_unit, attr_info, attr_class_unique #TODO: How can we put a nice description as information into the Gui (parameter, unit, information)

        except:
            print('InvalidAttributes: Check naming convention for attributes')



class Search:
    def __init__(self, df: DataFrame = None, sel_attr: list = None, attr: list = None, attr_names: list = None, weights: list = None):
        self.df = df
        self.attr = attr
        self.attr_names = attr_names
        self.sel_attr = sel_attr
        self.weights = weights

    #TODO: Check how to store the selected attributes in a list from the user | perhaps for the beginning a max. of 10 parameters
    #TODO: Error message, when selected parameter doubled
    # TODO: Get a zipped list from the user with ('parameter',importance (1-10))
    def weight(self):
        """
        calculates the weights for each selected parameter by an integer of importance

        Returns:
        - weight_l (list): list of tuples with weights for each selected parameter

        """
        weight_l = []
        attr_length = len(self.sel_attr)
        # Sum the second elements of each tuple
        total_sum = sum(second_tuple[1] for second_tuple in sel_attr)
        for el in self.sel_attr:
            weight = el[1]/total_sum
            weight_attr = (el[0],weight)
            weight_l.append(weight_attr)

        return weight_l, self.attr

    def quicksearch(self):
        """
        finds all the rows where either abbreviation or trade name correspond to a certain user input

        Returns:
        - filtered_value_abbr (dataframe): all results in form of a df based on user input regarding a
        certain abbreviation
        - filtered_value_tn (dataframe): all results  in form of a df based on user input regarding a
        certain trade name

        """

        #TODO: Dropdown Quicksearch -> Second Dropdown (abbreviation, trade_name) and Search to put in name -> Not found if not compatible
        userinput = input('Select trade_name or abbreviation: ')

        if userinput == 'abbreviation': #TODO: Just shows functionality -> replace by button click or search
            abbreviation = input('Type in abbreviation: ')
            position = [i for i,tup in enumerate(self.attr) if tup[0] == 'abbreviation']

            filtered_value_abbr = self.df[self.df.iloc[:,position[0]].str.contains(abbreviation, case=False)]


            if not filtered_value_abbr.empty:
                filtered_value_abbr.columns = self.attr_names

            else:
                raise TypeError('Check abbreviation spelling of {}. '
                                'Otherwise the abbreviation might not listed.'.format(abbreviation))

            return filtered_value_abbr


        elif userinput == 'trade_name': #TODO: Just shows functionality -> replace by button click or search
            trade_name = input('Type in trade_name: ')
            position = [i for i, tup in enumerate(self.attr) if tup[0] == 'trade_name']

            filtered_value_tn = self.df[self.df.iloc[:,position[0]].str.contains(trade_name, case=False)]

            if not filtered_value_tn.empty:
                filtered_value_tn.columns = self.attr_names

            else:
                raise TypeError(
                    'Check abbreviation spelling of {}. '
                    'Otherwise the trade name might not listed.'.format(trade_name))

            return filtered_value_tn

    # TODO: Dropdown Attribute Search -> Dropdown with attributes to click on
    def attribute_search(self):
        userinput = input('Select attribute: ') #TODO: Just shows functionality -> replace by button click or search; Maybe hint regarding lower upper case

        availability = [True for i, tup in enumerate(self.attr) if tup[0] == userinput]
        print(availability)
        if availability[0] == True:

            position = [i for i, tup in enumerate(self.attr) if tup[0] == userinput]
            print(position)
            filtered_attribute = self.df.iloc[:,position[0]]
            print(filtered_attribute)

        else:
            raise TypeError('Something went wrong. Check spelling of {}. '
                            'Otherwise this attribute might not be listed.'.format(userinput))

    # TODO: Addtional Configuration Button where little window pups up with min/max filter
    #def _attribute_search(self, attr_search_df):



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

sel_attr = [('youngs_modulus',10), ('yield_point',3), ('elongation_at_break',7), ('elongation_z',7), ('yield_point_t',3) ]

search_1 = Search(df,sel_attr, attr_tuples, attr_names)

#get weight amount

weight, attr = search_1.weight()

#quicksearch
#quick = search_1.quicksearch()

#attributesearch
attr_search = search_1.attribute_search()




