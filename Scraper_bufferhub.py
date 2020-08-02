#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
import math
import csv 
import time

class RateMyProfScraper:
        def __init__(self,schoolid):
            self.UniversityId = schoolid
            self.professorlist = self.createprofessorlist()
            self.indexnumber = False

        def createprofessorlist(self):#creates List object that include basic information on all Professors from the IDed University
            tempprofessorlist = []
            #num_of_prof = self.GetNumOfProfessors(self.UniversityId)
            #print(num_of_prof)
            #num_of_pages = math.ceil(num_of_prof / 20)
            i = 1
           
            #while (i <= num_of_pages):# the loop insert all professor into list
            while (i <= 200):
                print(i)
                page = requests.get("http://www.ratemyprofessors.com/filter/professor/?&page=" + str(
                    i) + "&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    self.UniversityId))
                #print(page)
              
                # only proceed if I have a 200 response which is saved in status_code
                if (page.status_code != 200):  
                   print("An error has occured. [Status code", page.status_code, "] Sleeping for 10 secs")
                   time.sleep(10)
                   continue
                    
               # else:
                #    data = page.json() #Only convert to Json when status is OK.
                
                temp_jsonpage = json.loads(page.content)
                #print(temp_jsonpage)
                temp_list = temp_jsonpage['professors']
                if not temp_list:
                    print("Empty JSON...skip after sleeping for 10 secs")
                    print(temp_jsonpage)
                    time.sleep(10)
                    i += 1
                    continue
                    
             
                 
                # now we will open a file for writing 
                data_file = open('file.csv', 'a+') 

                # create the csv writer object 
                csv_writer = csv.writer(data_file) 

                count = 0

                for prof in temp_list: 
                    if count == 0: 

                        # Writing headers of CSV file 
                        header = prof.keys() 
                        csv_writer.writerow(header) 
                        count += 1

                    # Writing data of CSV file 
                    csv_writer.writerow(prof.values()) 

                data_file.close() 
                tempprofessorlist.extend(temp_list)
                i += 1
          
           
            return tempprofessorlist

        def GetNumOfProfessors(self,id):  # function returns the number of professors in the university of the given ID.
            page = requests.get(
                "http://www.ratemyprofessors.com/filter/professor/?&page=1&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=" + str(
                    id))  # get request for page
            temp_jsonpage = json.loads(page.content)
            print(temp_jsonpage)
            num_of_prof = temp_jsonpage[
                              'remaining'] + 20  # get the number of professors at William Paterson University
            print(num_of_prof)
            return num_of_prof

        def SearchProfessor(self, ProfessorName):
            self.indexnumber = self.GetProfessorIndex(ProfessorName)
            self.PrintProfessorInfo()
            return self.indexnumber

        def GetProfessorIndex(self,ProfessorName):  # function searches for professor in list
            for i in range(0, len(self.professorlist)):
                if (ProfessorName == (self.professorlist[i]['tFname'] + " " + self.professorlist[i]['tLname'])):
                    return i
            return False  # Return False is not found

        def PrintProfessorInfo(self):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
            else:
                print(self.professorlist[self.indexnumber])

        def PrintProfessorDetail(self,key):  # print search professor's name and RMP score
            if self.indexnumber == False:
                print("error")
                return "error"
            else:
                print(self.professorlist[self.indexnumber][key])
                return self.professorlist[self.indexnumber][key]


WilliamPatersonUniversity = RateMyProfScraper(1112)
WilliamPatersonUniversity.SearchProfessor("John Lynn")
WilliamPatersonUniversity.PrintProfessorDetail("overall_rating")


# In[ ]:




