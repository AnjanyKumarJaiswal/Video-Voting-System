import urllib.request

# Creating a python file to generate Yotube links

class Generate_links:
    
    def __init(self,ytlink,twichlink,videolink):
        self.ytlink = ytlink
        self.twichlink = twichlink
        self.videolink = videolink
    
    def reqlink(request1 , request2):
        # request = input()
        response = urllib.request.urlopen(request1)
        print()
        response2 = urllib.request.URLopener(request2)
        # data = response.read()
        
    reqlink(input("Enter the first url:"), input("Enter the second url:"))
    
    
