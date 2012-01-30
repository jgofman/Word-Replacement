##Jacob Gofman
##Due December 6th

##Create program that replaces holidays with dates
##
##Create a dictionary of 8 or more holidays for 2011 listing dates as strings of the form '12/25/2011' (e.g., Christmas)
##
##For simplicity, please either choose one word holidays or hyphenate multi-word holidays, e.g., Veteran's-Day
##
##Write a function that uses the dictionary to replace holidays in a string with the corresponding dates. The function should work as follows:
##    It should splits the string into words (use the split function)
##    To simplify the problem, hyphenate any multi-word holidays, e.g., Veteran's-Day
##    It should check if each word is in the dictionary and replace it in the list with its value, e.g., the list ['I','wish','you','a','merry','Christmas'] should become:
##    ['I','wish','you','a','merry', '12/25/2011']
##    Converts this list into a string using a for loop. Start with the empty string and add the items in the list, separated by spaces. Return the resulting string.
##    Your function in (ii) should deal with punctuation and capitalization in some way. For capitalization, you could simply convert to lower case and only store
##    lowercase items in your dictionary. For punctuation, you could strip off nonletter characters. Smoother ways of handling these issues are worth more points.

import re

holidays = {
    'christmas':'12/25/2011',
    'thanksgiving':'11/24/2011',
    'halloween':'10/30/2011',
    'passover':'04/19/2011',
    'kwanzaa':'12/26/2011',
    'chanukkah':'12/21/2011',
    'independence-day':'07/04/2011',
    'memorial-day':'05/30/2011' }
    
def replace_with_date():
    user_input = str(raw_input('Input string containing a holiday. Hyphenate multi-word holidays (i.e.: Veteran\'s-Day): '))
    mod_input = ''
    output = ''
    
    for char in user_input:
        if (char.isalnum() or char.isspace() or char == '-' or char == '\''): mod_input += char    
   
    new_list = mod_input.lower().split()
    last = ''
    
    for word in new_list:    
        if word in holidays:
            date = holidays.get(word)
            insert = word
            insert2 = word.capitalize()
            insert3 = ''
            if '-' in word:
                word_sublist = word.split('-')
                for part in word_sublist:
                    part = part.capitalize()
                    insert3 += (part + '-')
                insert3 = insert3.rstrip('-')
            if last == '':
                if insert in user_input: output = user_input.replace(insert, date)
                elif insert2 in user_input: output = user_input.replace(insert2, date)
                elif insert3 in user_input: output = user_input.replace(insert3, date)
            else:
                if insert in output: output = output.replace(insert, date)
                elif insert2 in output: output = output.replace(insert2, date)
                elif insert3 in output: output = output.replace(insert3, date)
        else: print('I\'m sorry, but there was no match found for the holiday you gave me.')
        last = word
        
    print(output)
    return

replace_with_date()

