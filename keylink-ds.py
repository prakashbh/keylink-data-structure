#Program: Implementation of keylink data structure
#Author:  Prakash B Hegade
#Email:   prakash.hegade@gmail.com
#Date:    25 July 2016
#Others:  Read Manual for more details

from bs4 import BeautifulSoup
import urllib.request

# Global list to capture all the keywords and the extracted links
keylink = []


# Add a new key to keylink list
# The link part is initialized to NULL
# The new key is appended to the existing list
def add_key():
    print("Enter the keyword [use a - as delimiter for more than one word]")
    k = input()
    key = [k, "NULL"]
    global keylink
    keylink.append(key)


# Display the list
# Prints the key and its link (NULL if not populated yet)
def show():
    global keylink
    if len(keylink) == 0:
        print("List is Empty")
    else:
        print("The Keylink list is as follows")
        print("KEY-->LINK")
        for k in keylink:
            print(k[0] + "-->" + k[1])


# Get the link for which the link value is NULL from the keylink list
# The function uses BeautifulSoup API to extract the first valid link
# from the google search page
# It picks up only the first valid link
# More links can be appended to the list based on the program needs and
# requirement
def get_links():
    global keylink
    index = 0

    if len(keylink) == 0:
        print("List is Empty")
    else:
        print("Getting the links...")
        for k in keylink:
            # Get the links only for the required keys
            if k[1] == "NULL":
                opener = urllib.request.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                url = "http://www.google.com/search?q=" + k[0] + "&start="
                page = opener.open(url)
                soup = BeautifulSoup(page, "html.parser")

                # Get the first valid link
                for cite in soup.find_all('cite'):
                    if cite.text.find("www") >= 0 and \
                       cite.text.find("...") == -1:
                        keylink[index][1] = cite.text
                        break
            index = index + 1
            print(".")
        print("Keylink Updated")


# Remove the user mentioned key from the list
# As the list 
def remove_key():
    global keylink
    flag = 0
    
    if len(keylink) == 0:
        print("List is Empty")
    else:
        print("Enter the key you want to delete")
        key = input()
        for k in keylink:
            if k[0] == key:
                keylink.remove(k)
                print("Key removed from the list")
                flag = 1
                break;

    if flag == 0:
        print("Specified Key Not found")


# Define the switch cases for each
def main():
    while True:
        print("Menu")
        print("--------------")
        print("1-Show\n2-Add Key\n3-Get Links\n4-Remove Key\n5-Exit")
        print("--------------")
        print("Enter your choice\n")
        choice = input()
        
        if choice == '1':
            show()
        elif choice == '2':
            add_key()
        elif choice == '3':
            get_links()
        elif choice == '4':
            remove_key()
        else:
            print("Program Terminates")
            break  
    
#call the main
main()
