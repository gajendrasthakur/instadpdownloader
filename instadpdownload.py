'''
Download Display Picture of an Instagram Account with Python
Author: Gajendra Singh Thakur
For more info visit:- http://http://gajendrasingh.tech/
'''

#import the necessary module!
import instaloader
#create an instance
test = instaloader.Instaloader()
#fetch the account details
acc = input('Enter the Account Username: ')
#download the data
test.download_profile(acc, profile_pic_only = True)  
