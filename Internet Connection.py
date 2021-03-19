#Corinne Haley
#Practice Script
#Description: The purpose of this script is to check for internet connection
#using a URL.

#start by inporting the urllib module which is for opening and reading URLs
import urllib.request

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
print('\n')
#Test the code to see if it works.  A print string can contain a variable.
print('You are connected!\n' if connect() else 'no internet!\n' )


