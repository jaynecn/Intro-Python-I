"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"


import os
print(os.getcwd())


with open('src/foo.txt') as foo:
    text_doc = foo.read()

print(text_doc)

print('----------------------------------------------------')


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain


with open('src/bar.txt', 'w') as bar:
    write_new = bar.write('O Flower of Scotland\nWhen will we see \nyour like again?')

with open('src/bar.txt') as new_bar:
    read_bar_doc = new_bar.read()

print(read_bar_doc) 