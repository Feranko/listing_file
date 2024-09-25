#!/usr/bin/
import os
import sys

class main:
    def __init__(self, **kwargs):
        
        self.working_path = ""
        lenght_input = len(sys.argv)

        if lenght_input >= 2:
            self.working_path = sys.argv[1]
        else:
            self.working_path = os.getcwd()
    
        self.control()

    def variable_holder(self):
        self.files_list = []
        self.folder_list = []
        self.runnable_files = []
        self.hiden_file_list = []
        self.hiden_folder_list = []

    def is_hide(self, file_path):#function to check 
        splited = file_path.split(".")# divid the string for the point in it
        if splited[0] == "":# if the first slot is empty return true
            return True
        else:# else return false
            return False

    def check(self):
        os.chdir(self.working_path)
        
        for file in os.listdir():
            if self.is_hide(file):#working with hided file
                if os.path.isfile(file):#check if is hiden file
                    self.hiden_file_list.append(file)

                if os.path.isdir(file):#check if is hiden folder
                    self.hiden_folder_list.append(file)

            else:#working with un hided file
                if os.path.isfile(file):
                    if os.access(file, os.X_OK):#check if is runnable
                        self.runnable_files.append(file)
                    else:#if is not runnable add to the generic folder
                        self.files_list.append(file)
                if os.path.isdir(file):
                    self.folder_list.append(file)

    def display(self, argument):
        if argument == None:
            print("|")
        else:
            for argv in argument:
                print(f"|{argv}")

    def output(self):
        if int(len(self.hiden_file_list)) == 0:
            pass
        else:
            print(f"\033[33m{len(self.hiden_file_list)}----hiden-file----")
            self.display(self.hiden_file_list)

        if int(len(self.hiden_folder_list)) == 0:
            pass
        else:
            print(f"\033[35m{len(self.hiden_folder_list)}----hiden-directory----")
            self.display(self.hiden_folder_list)
        
        if int(len(self.files_list)) == 0:
            pass
        else:
            print(f"\033[37m{len(self.files_list)}----files-----")
            self.display(self.files_list)

        if int(len(self.runnable_files)) == 0:
            pass
        else:
            print(f"\033[32m{len(self.runnable_files)}----runnable----")
            self.display(self.runnable_files)

        if int(len(self.folder_list)) == 0:
            pass
        else:
            print(f"\033[36m{len(self.folder_list)}----directory----")
            self.display(self.folder_list)

        print("\033[37m")

    def control(self):
        self.variable_holder()
        self.check()
        self.output()

if __name__=="__main__":
    main()
