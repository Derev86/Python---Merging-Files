# make the required library imports for the program
# pandas library is used to read the data in csv file
import pandas as pd

def read_csv(filename):
    '''
    This function reads the given csv file and returns its data.
    Parameter:
        filename - the name of the csv file
    Returns:
        tuple of column header list and data rows list
    '''
    data=pd.read_csv(filename) # read the csv file and make a dataframe from that data
    column_headers=data.columns.tolist() # get the column headers from the dataframe and make it a list using 'tolist()' method
    # 'data.values.tolist()' is used to get the column data into a nested list structure
    return (column_headers,data.values.tolist()) # return the final tuple

def read_txt(filename):
    '''
    This function reads the given txt file and returns its data.
    Parameter:
        filename - the name of the txt file
    Returns:
        nested list of data rows
    '''
    input_file=open(filename,'r') # open the file
    text_data=input_file.read().split('\n') # read the content and split by new lines
    input_file.close() # close the file

    data=[] # to store the row data
    for line in text_data: # iterate over data rows
        if line!='': # neglect the empty data rows
            data.append(line.split(',')) # non empty data rows are splited in to list by commas and add to the main list
    
    return data

def merge_data(data_1,data_2):
    '''
    This function merges the data in given two lists to a single list.
    Parameter:
        data_1 - row data nested list in csv file
        data_2 - row data nested lits in txt file
    Returns:
        nested list of merged data rows
    '''
    merged_data=[] # to store the merged data
    for i in range(len(data_1)):
        temp=data_1[i] # store the data list of csv file in a variable
        for j in range(len(data_2)):
            # compare the first elements of the csv file's data row list and txt file's data row list after converting them into integers
            if int(data_1[i][0])==int(data_2[j][0]): 
                # when above two elements are matched, the "temp" list is extended by the data in txt file's data row
                # for this we use elements except first one, since it is the 'ID' element and it is already present in the csv file's data row list
                temp.extend(data_2[j][1:])
                # add the merged data row list to the storing variable
                merged_data.append(temp)
                # since there is only one match between two files, after finding the first match, we stops the iteration for that element to save operations
                break

    return merged_data

def convert_to_str(data_list):
    '''
    This function converts a list containing interger values to a list which contains only strings. In other words,
    this function converts integer elements in a list to string values.
    Parameter:
        data_list - list of data
    Returns:
        only string elements list
    '''
    for k in range(len(data_list)): # iterate over the elements in the list
        data_list[k]=str(data_list[k]) # convert element to string
    return data_list

def write_data(filename,data):
    '''
    This function writes the given data to a text file.
    Parameter:
        filename - the name of the txt file
        data - nested list of data that needs to be written into the file
    Returns:
        nothing is returned
    '''
    out_file=open(filename,'w') # open the file in writing mode
    for dt in data: # iterate over the data list
        dt=convert_to_str(dt) # convert the list of data into string list
        out_file.write(','.join(dt)+'\n') # join this string list by commas and write that single string and a new line to the file
    out_file.close() # close the file


def main():
    '''
    This function combines all the above defined functions to perform the required task.
    '''
    # read the csv file and get headers and row data to two variables
    csv_header,csv_data=read_csv('user data.csv')
    # read the txt file and get the data into a list variable
    txt_data_out=read_txt('user details.txt')
    print('The data from the files are loaded succesfully.')
    # divide above nested data list into two parts to filter out the headers and the data rows
    # the fisrt element is the headers list
    # all the other list elements are the data row lists
    txt_headers,txt_data=txt_data_out[0],txt_data_out[1:]
    # combine two header lists into a single list
    csv_header.extend(txt_headers[1:])
    # merge the two data row lists into a single list
    merged_data_list=sorted(merge_data(csv_data, txt_data))
    # combine the merged headers list and the data rows list into a single nested data list
    merged_data_list.insert(0, csv_header)
    print('The data is merged.')
    # write merged data into the output txt file
    write_data('merged data.txt', merged_data_list)
    print('Merged data is succesfully written into the merged data.txt file.')

# call the main function to run the program
main()
    