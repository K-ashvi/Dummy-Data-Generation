import pandas as pd
import random
import string
#1 lakh rows
num_rows = 100000

#random strings
def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))
#specify number of characters in the columns

string_data = {
    'Names': [random_string(5) for _ in range(num_rows)],
    'Address': [random_string(20) for _ in range(num_rows)]
}
#random integers
#specify number of digits in each
int_data = {
    'Phone_Number': [random.randint(7000000000,9999999999) for _ in range(num_rows)],
    'Age': [random.randint(21,65) for _ in range(num_rows)]
}

# random boolean 
bool_data = {
    
    #try 0s and 1s
    'Present': [random.randint(0,1) for _ in range(num_rows)]
    #'Present': [random.choice([True, False]) for _ in range(num_rows)]
}

#indiviually done
string_df = pd.DataFrame(string_data)
int_df = pd.DataFrame(int_data)
bool_df = pd.DataFrame(bool_data)

#combine
result_df = pd.concat([string_df, int_df, bool_df], axis=1)

result_df.to_csv(r'C:\Users\kashv\Downloads\dummy.csv', index=False)

