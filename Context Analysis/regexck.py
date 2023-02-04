import datetime
from datetime import date
import re

def use_regex(input_text):
    
    pattern1 =re.search(" ".join(["venkat", "\d{1,2}-year-old"]),input_text)
    if(pattern1!=None):
        return date.today().year-int(''.join(re.findall("\d{1,2}",pattern1.string[pattern1.start():pattern1.end()])))

    pattern2 =re.search(" ".join(["venkat", "\d{1,2} year old"]),input_text)
    if(pattern2!=None):
        return date.today().year-int(''.join(re.findall("\d{1,2}",pattern2.string[pattern2.start():pattern2.end()])))
    
    pattern3 =re.search(" ".join(["venkat", "\d{1,2} years old"]),input_text)
    if(pattern3!=None):
        return date.today().year-int(''.join(re.findall("\d{1,2}",pattern3.string[pattern3.start():pattern3.end()])))

    pattern4 =re.search(" ".join(["venkat","\d{1,2}"]),input_text)
    if(pattern4!=None):
        return date.today().year-int(''.join(re.findall("\d{1,2}",pattern4.string[pattern4.start():pattern4.end()])))

    pattern5 =re.search(", ".join(["venkat", "\d{1,2}"]),input_text)
    if(pattern5!=None):
        return date.today().year-int(''.join(re.findall("\d{1,2}",pattern5.string[pattern5.start():pattern5.end()])))
    
    pattern6 =re.search(" ".join(["venkat", "\([0-9][0-9]\)"]),input_text)
    if(pattern6!=None):
        return date.today().year-int(''.join(re.findall("\d{1,2}",pattern6.string[pattern6.start():pattern6.end()]))) 
    


if __name__=="__main__":
    data='''todays news venkat 99  arresyed due to illrgal activity'''
    print(use_regex(data))

    