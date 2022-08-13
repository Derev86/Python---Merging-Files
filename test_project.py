# import the pytest module to make the test functions
import pytest
# import the functions from the project.py file that need to be checked
from project import read_csv,read_txt,merge_data,convert_to_str,write_data

def test_read_csv():
    '''
    This function tests the read_csv function.
    '''
    correct_output=['ID', 'Name', 'Date of Birth']
    # get the output from the read_csv file and compare it with the correct output
    assert read_csv('user data.csv')[0]==correct_output

def test_read_txt():
    '''
    This function tests the read_txt function.
    '''
    correct_output=['1005', 'Engineer', '$52000']
    # get the output from the read_txt file and compare it with the correct output
    assert read_txt('user details.txt')[2]==correct_output

def test_merge_data():
    '''
    This function tests the merge_data function.
    '''
    correct_output=[1001, 'Tom', '17/06/1985', 'Teacher', '$20000']
    # get the output from the merge_data file and compare it with the correct output
    assert merge_data(read_csv('user data.csv')[1], read_txt('user details.txt')[1:])[5]==correct_output

def test_convert_to_str():
    '''
    This function tests the convert_to_str function.
    '''
    correct_output=['1005', 'Engineer', '$52000']
    # get the output from the convert_to_str file and compare it with the correct output
    assert convert_to_str([1005, 'Engineer', '$52000'])==correct_output

def test_write_data():
    '''
    This function tests the write_data function.
    '''
    correct_output=['1011','Luci','08/02/1990','Developer','$42000']
    # get the output from the write_data file and compare it with the correct output
    assert read_txt('merged data.txt')[7]==correct_output