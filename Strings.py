def remove_new_lines(string_to_cleanse):
  str_array = string_to_cleanse.splitlines()
  new_string = ""
  for i in range(len(str_array)):
    new_string += str_array[i]
  return new_string

def remove_all_whitespace(string_to_cleanse):
  pass

# removes part of a string within specific indexes
def trim_string(index1, index2, string_to_change):
  pass

# insert string at specific index
def insert_string(index1, string_to_insert, string_to_change):
  pass

# searches for a string within another string
def search_string(criteria, string_to_search):
  pass

# Replaces specified number of a string with another
def string_replace(old, new, count, string_to_change):
  pass

# Replaces all instances of a string with another
def string_replace_all(old, new, string_to_change):
  pass

# Removes specified number of a string within a string
def string_remove(old, count, string_to_change):
  pass

# Removes all instances of a string within a string
def string_remove_all(old, string_to_change):
  pass

# convert string to ascii values
def string_to_ascii(string_to_convert):
  pass

# Add all char ascii values in a string
def string_total(string_to_total):
  pass

# sort a list of strings
def string_sort(strings_to_sort):
  pass

# sort words in a string
def word_sort(string_to_sort):
  pass

# sort chars in a string
def char_sort(string_to_sort):
  pass
