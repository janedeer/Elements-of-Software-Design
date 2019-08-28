#  Description: This program determines if a string is a palindrome
# If it is not, it creates the shortest palindrome from the word
# input file palindrome.txt

# this function checks if the string is palindrome
# returns bool
def is_palindrome(s):
    return s == s[::-1]

# turns string into shortest palindrome by adding letters to beginning
# returns new string
def make_palindrome(s):
    i = 0
    j = -1
    new_s = s
    s_list = list(s)
    while is_palindrome(new_s) == False: # while not palindrome
        i -= 1
        j += 1
        s_list.insert(j, s[i]) # add ith letter to jth position of s_list
        new_s = "".join(letter for letter in s_list) # new string
    return new_s
    

def main():
    inf = open("palindrome.txt", "r")
    for line in inf:
        line = line.strip()
        if is_palindrome(line):
            print(line)
        else:
            print(make_palindrome(line))


    inf.close()

           
main()
