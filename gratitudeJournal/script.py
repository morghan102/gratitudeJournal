import datetime
import os

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
    #fetch the content
    #generate filename
    #add author's name, title, and date
    #fix spacing of doc and add to txt file
    