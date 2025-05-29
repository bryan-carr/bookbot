"""
stats.py: Countains functions to generate statistical info about a book's text.
These functions will be used in the BookBot project.
"""

def count_words(text_to_count):
    """
    Funciton count_words: counts the words in the text that it is input
    """

    list_of_words = text_to_count.split()
    return len(list_of_words)

def count_characters(text_to_count):
    """
    Function to count the number of characters in the text input
    """

    count_dict = {}
    for character in text_to_count.lower():
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
#        print(count_dict)
    
    return count_dict

def sort_count(count_dict):
    """
    Funciton to sort the counted characters' dictionary, from highest count to lowest
    Converts the input dictionary to a List of smaller dictionaries
    then Sorts the list
    """

    list_to_sort = []

    for char in count_dict:
        list_to_sort.append({"char" : char, "num" : count_dict[char]})
    
    list_to_sort.sort(key=sort_on, reverse=True)

    return list_to_sort

def sort_on(dict):
    return dict["num"]

