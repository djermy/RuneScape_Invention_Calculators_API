def json_cleaner(filename, filename2):
    '''
    Takes 2 'complete' filename strings. Converts filename1 into filename2 by removing-
    empty lines.
    '''

    data = load_data(filename)
    cleaned_data = remove_empty_data(data)
    dump_clean_data(cleaned_data, filename2)

# helper functions
def load_data(filename):
    '''
    Takes filename as string and returns the loaded JSON lines as list object.
    '''

    data = None
    with open(filename, 'r') as f:
        data = f.readlines()
    
    return data

def remove_empty_data(data):
    '''
    Takes list of JSON strings and removes empty list items.
    '''

    cleaned_data = [item for item in data if item != '[]\n']

    return cleaned_data

def dump_clean_data(cleaned_data, filename):
    '''
    Takes cleaned list of JSON strings and writes them to new file.
    WARNING this is in WRITE MODE!, if file exists it WILL be overwritten.
    '''

    with open(filename, 'w') as f:
        f.writelines(cleaned_data)
    
    print(f'{filename} has been successfully created in the current directory!')