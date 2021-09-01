def count_char(st,key):
    ''' This function will accept the word or phrase or sentence as first argument and
         the character which i call it key to be counted  as the second argument , and it will return the number
         of occurrences of that character in the string '''
    
    count=0
    for i in st:
        if i==key:
           count+=1
    return count    


string=input('Enter ==> ').lower()
target=input('Targeted character ==> ').lower()

# we will count number of target charachter
print(count_char(string,target))

