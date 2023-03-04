import datetime
import os

author = ""

def create_journal():
    # user names journal
    name = input("Name your journal: ")

    #find curr working dir & create journal in same one
    cwd = os.getcwd()
    path = cwd + "/" + name #concat to create new path
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory")

def open_journal():
    #move into dir w/ file,
    os.chdir(os.getcwd())
    journal_list = os.listdir() # get a list of the journals w/in the curr dr

    # loop thru list of journals & print
    print("Current journals: " + str(len(journal_list)))
    for journal in journal_list:
        print(journal)

    #ask user to choose a journal in list
    name = input("Name of journal: ")
        #create path we're gonna move into & move into it
    cwd = os.getcwd()
    path = cwd + "/" + name
    os.chdir(path)

    # get a list of entries, print one by one
    directory_list = os.listdir()
    print("Current Entries: " + str(len(directory_list)))
    for entry in directory_list:
        print(entry)
def fetch_content():
    content = input("Write to your heart's content :) ")
    return content

def add_content():
    #ask for title of entry
    title = input("What's the title for this entry? ")
    content = fetch_content() #fetch the content
    filename = title.replace(" ", "") + ".txt" #generate filename
    entry = open(filename, "a") # create/open the file
    entry.write(author + "\n") #add author's name, title, and date
    entry.write(title + "\n")
    entry.write(str(datetime.datetime.now()) + "\n")
    #fix spacing of doc and add to txt file
    count = 0
    prev_i = 0
    for i in range(0, len(content) - 1):
        if content[i] == " ":
            entry.write(content[prev_i:1])
            count += 1
            prev_i = i
        if count == 10: #if we have 10 words already written
            count = 0
            entry.write("\n")
    entry.close()

def add_page():
    title = input("Name your entry: ")
    # filename = title.replace(" ", "") + ".txt"
    add_content()

def remove_page():
    title = input("What's the title of your entry?  ")
    filename = title.replace(" ","") + ".txt"
    os.remove(filename)

def controls():
    print('''What would you like to do?: 
    Try typing any of the following commands:
    1 or "create" to create a journal
    2 or "open" to open a journal
    3 or "new" to create a new entry
    4 or "insert" to add to an entry
    5 or "del" to delete an entry
    Your choice: 
    -----\n-----
    ''')

    def switch(user_input):
        if user_input == "1":
        # case "create":
            create_journal()
        elif user_input == "2":
            open_journal()
        elif user_input == "3":
            add_page()
        elif user_input == "4":
            add_content()
        elif user_input == "5":
            remove_page()
        else:
            print("I cannot do anything with that.")
            controls()
    switch(input())
    choice = input("Do you need anything else? y/n")
    if choice == "y" or choice == "yes":
        controls()
    else:
        print("See ya!")

author = input("What's your name?")
# controls()

if __name__ == '__main__':
    controls()
