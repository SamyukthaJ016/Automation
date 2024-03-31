import os

def rename_files(file_names, new_names):
    # Check that the lengths of the two lists are equal
    if len(file_names) != len(new_names):
        raise ValueError('The lengths of file_names and new_names must be equal.')

    # Loop through the list of files and rename them
    for i, file_name in enumerate(file_names):
        new_name = new_names[i]
        src = os.path.join(directory, file_name)
        dst = os.path.join(directory, new_name)
        os.rename(src, dst)

# Example usage
directory = ''

file_names = ['file1.txt', 'file2.txt']
new_names = ['new_file1.txt', 'new_file2.txt']

rename_files(file_names, new_names)