#Database Search Script
#Niko Nagengast
#240218 - v2



#import libraries
import os
import pandas as pd
#from treelib import Node, Tree #TODO: Please add-in packages script


#######################
# DATAFRAME OPERATION #
#######################

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
            df = pd.read_excel(self.file_path, header = [0,1])#,index_col=[0,1])
            return df
        except Exception as e:
            print("Error loading Excel file:", e)
            return None

    @staticmethod
    def get_attr_indices(df: pd.DataFrame):
        """
        Get the attribute tuples of level 0 indices and the corresponding level 1 indices of the DataFrame as a list.

        Parameters:
        - df (DataFrame): The DataFrame for which to retrieve the level 0 and 1 column names.

        Returns:
        - level_0_index (list): A list of level 0 indices
        - level_1_index (list): A list of level 1 indices corresponding to level 0
        - multi_index_dic (dic): A dictionary of level 0 (key) - level 1 (value) pairs
        """

        level_0_index = df.columns.get_level_values(0).tolist()
        print(df)
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
    def get_attr_level_0_inf(level_0_index: list):
        """
        split the attribute tuples in their groups

        Parameters:
        - level_0_index (tuples): list of complete attribute description in a 4-tuple at level 0
        (full_name,descriptive,-,main_polymer_group_of_the_material)

        Returns:
        - attribute_names (list): list of attribute parameters - actual column name
        - attribute_class (list): list of atrriute class names - high-level category
        - attr_unit (list): list of parameter units
        - attr_info (list): list of short explanation parameter
        - attr_class_unique (list): list of unique attribute class names
        """
        #attr_names, attr_class, attr_unit, attr_info = [], [], [], []
     
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


    @staticmethod
    def get_attr_level_1_inf(df: pd.DataFrame, level_0_index: list, multi_index_dic: dict):
        """
        get 1st level indices information based on 0 level index selection

        Parameters:
        - level_0_index (tuples): complete attribute description in a 4-tuple
        (full_name,descriptive,-,main_polymer_group_of_the_material)
        - multi_index_dic (dictionary): dictionary of 0 level index tuple and corresponding 1 level index list
        - df (DataFrame): The DataFrame for which to retrieve the level 0 and 1 column names.

        Returns:
        - updated_dict (dict): dictionary of key(attr_name level 0) and list of index names level 1
        - level_1_index_spec (list): list of index names level 1 based on specific attr_name level 0
        - level_1_index: list of all index names level 1
        """

        try:

            ############################################################################################################
            #Todo: Check if necessary
            #dictionary with 0 level index name and corresponding 1st level indices
            updated_dict = {}

            # Iterate through the original dictionary
            for old_key, value in multi_index_dic.items():
                # Modify the key as needed
                new_key = old_key[0]
                # Add the key-value pair to the updated dictionary
                updated_dict[new_key] = value

            level_1_index = [value for sublist in updated_dict.values() for value in sublist]

            ############################################################################################################

            # search for 1st level indices based on 0 level index input
            df = df.T

            #TODO: change in gui -> user input based on click
            name = str(input('select 0 level property (number, name, '
                             'molecule_information, yield_strength_0, '
                             'properties_change_recycling,degradation_phot_oxidation, '
                             'coordinates_company_headquarters):'))


            for tup in level_0_index:
                if name not in tup:
                    pass
                elif name in tup:
                    target_tup = tup
                    #format string
                    formatted_string = "(" + ", ".join(str(item) for item in target_tup) + ")"
                    formatted_string = formatted_string.replace(", ", ",")

            level_1_index_spec = df.loc[str(formatted_string)].index.tolist()

            return level_1_index_spec, level_1_index, updated_dict

        except:
            print('InvalidAttributes: Check naming convention for attributes')

####################
# SEARCH OPERATION #
####################


class Search:
    def __init__(self, df: DataFrame = None, attr: list = None, attr_names: list = None,
                 weights: list = None, sel_attr: list = None):
        self.df = df
        self.attr = attr
        self.attr_names = attr_names
        self.sel_attr = sel_attr
        self.weights = weights

    @staticmethod
    def param_visualization(index_dict):
        """
        visualizes the input dictionary in a tree-like structure based on recursive parent child mapping

        Parameters:
        - index_dict(dictionary): dictionary of key(attr_name level 0) and list of index names level 1

         """
        #added = set()
        #tree = Tree()
        #while index_dict:

            #for key, value in index_dict.items():
                #if value['parent'] in added:
                    #tree.create_node(key, key, parent=value['parent'])
                    #added.add(key)
                    #index_dict.pop(key)
                    #break
                #elif value['parent'] is None:
                    #tree.create_node(key, key)
                    #added.add(key)
                    #index_dict.pop(key)
                    #break

        #tree.show()



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
"""
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

    #TODO: Dropdown Attribute Search -> Dropdown with attributes to click on
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
    
    
    #TODO: Check how to store the selected attributes in a list from the user | perhaps for the beginning a max. of 10 parameters
    #TODO: Error message, when selected parameter doubled
    #TODO: Get a zipped list from the user with ('parameter',importance (1-10))
    def weight(self):
        
        calculates the weights for each selected parameter by an integer of importance

        Returns:
        - weight_l (list): list of tuples with weights for each selected parameter
        
    
        weight_l = []
        attr_length = len(self.sel_attr)
        # Sum the second elements of each tuple
        total_sum = sum(second_tuple[1] for second_tuple in sel_attr)
        for el in self.sel_attr:
            weight = el[1]/total_sum
            weight_attr = (el[0],weight)
            weight_l.append(weight_attr)

        return weight_l, self.attr

"""
#################
# MAIN PROTOCOL #
#################

def main():

    # Example usage:
    file_path = os.path.join(os.environ.get('HOME'),'Desktop')

    ####################################################################################################################
    ##Dataframe operations

    # Create an instance of ExcelLoader with the file path
    df = DataFrame(file_path + "/filaments.xlsx")

    # Load the Excel file into a DataFrame
    df = df.load_excel_to_dataframe()
    # Use the class method to get column names as a list
    level_0_index,level_1_index,multi_index_dic = DataFrame.get_attr_indices(df)

    # get all information from index level 0
    attr_names, attr_class, attr_unit, attr_dtype, attr_class_unique = DataFrame.get_attr_level_0_inf(level_0_index)
    print(attr_names, attr_class, attr_unit, attr_dtype, attr_class_unique)
    # get all information from index level 1
    level_1_ind_spec, level_1_ind, index_dict = DataFrame.get_attr_level_1_inf(df,level_0_index, multi_index_dic)
    print(level_1_ind_spec, level_1_ind, index_dict)
    ####################################################################################################################
    ##Search operations



    #sel_attr = [('youngs_modulus', 10), ('yield_point', 3), ('elongation_at_break', 7), ('elongation_z', 7),
                #('yield_point_t', 3)]

    search_1 = Search(df)

    df_search = search_1.df.xs('abbreviation', axis=1, level=1, drop_level=False)
    df_search = df_search.reset_index(level=0, drop=True)
    print(df_search)

    # visualize indices structure
    #TODO: Bottom in search menu but should pop up in addtional window
    #search_1.param_visualization(index_dict)

    # get weight amount

    #weight, attr = search_1.weight()

    # quicksearch
    # quick = search_1.quicksearch()

    # attributesearch
    #attr_search = search_1.attribute_search()


if __name__ == "__main__":
    main()