from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
from urllib.request import urlretrieve
from sys import stderr
import urllib.request
import cssutils
import sys 
import logging
import time

Bl='\033[30m'
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

os.system('clear')
stderr.writelines(f"""{Gr} 

        {Gr} ██╗                ╔██ █████╗██████╗       {Re} ██████╗██╗    ██████╗ ███╗   ██╗█████╗██████╗
        {Gr} ╚██╗      ██      ╔██╝ ██╔══╝██╔══██╗     {Re} ██╔════╝██║   ██╔═══██╗████╗  ██║██╔══╝██╔══██╗
        {Gr}  ╚██╗  ╔██╝╚██╗  ╔██╝  █████╗██████═╝{Wh}█████╗{Re}██║     ██║   ██║   ██║██╔██╗ ██║█████╗███████║  
        {Gr}   ╚██══██╝  ╚██══██╝   ██╔══╝██╔══██╗{Wh}╚════╝{Re}██║     ██║   ██║   ██║██║╚██╗██║██╔══╝██║  ║██╗ 
        {Gr}    ╚████╝    ╚████╝    █████╗██████╔╝      {Re}╚██████╗█████╗╚██████╔╝██║ ╚████║█████╗██║  ╚██║ 
        {Gr}     ╚══╝      ╚══╝     ╚════╝╚═════╝      {Re}  ╚═════╝╚════╝ ╚═════╝ ╚═╝  ╚═══╝╚════╝╚═╝   ╚═╝ 
        {Wh}  <----- {Gr}W E B       {Re}C L O N E R       {Wh}B Y      {Gr}G G A M E S{Wh}----->  
        """)
URL = input(f"\n       [ {Gr}+ {Wh}] URL DU SITE : {Re}")
def report(count, size, total):
        progress = [0, 0]       
        progress[0] = count * size
        if progress[0] - progress[1] > 1000000:
            progress[1] = progress[0]
            print("Téléchargement de {:,}/{:,} ...".format(progress[1], total))
            time.sleep(2)

print (f"\n{Wh}[ {Gr}+ {Wh}] Connexion au serveur")
time.sleep(2)
cssutils.log.setLevel(logging.CRITICAL)
directory = ''

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'),
                        ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                        ('Connection', 'keep-alive')
                    ]
urllib.request.install_opener(opener)

try:
    html_doc = urllib.request.urlopen(URL).read()
    print(f"\n{Wh}[ {Gr}+ {Wh}] {Gr}Connecté au serveur")
    time.sleep(2)
except ValueError as e:
    print(f"\n{Wh}[ {Re}- {Wh}] {Re}Erreur: URL incorrecte")
    sys.exit()
try :
        soup = BeautifulSoup(html_doc, 'html.parser')
        f = open( 'index.html', 'w' )
        f.write(str(soup))
        f.close()
        print (f"\n{Wh}[ {Gr}+ {Wh}] {Wh}Inisialiton de l'index")
        time.sleep(2)
        print (f"\n{Wh}[ {Gr}+ {Wh}] {Wh}Début du clone")
        time.sleep(2)
        print (f"\n{Wh}[ {Gr}1 {Wh}] {Wh}Images")
        a = soup.find_all('img')
        for i in range(len(a)):
            try:
                if(a[i].get('data-src')):
                    directory = a[i]['data-src']
                elif(a[i].get('src')):
                    directory = a[i]['src']
                else:
                    continue
                if "data:image" in directory:
                    continue
                if not os.path.exists(os.path.dirname(directory)):
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(URL+directory, directory, reporthook=report)
            except Exception as e:
                print (f"\n     {Wh}[ {Re}- {Wh}] {Wh}Problème : ",e)
        print (f"\n     {Wh}[ {Gr}+ {Wh}] {Gr}Les images sont loadées")
        time.sleep(2)
        print (f"\n{Wh}[ {Gr}2 {Wh}] {Wh}CSS")
        a = soup.find_all('link')
        for i in range(len(a)):
            try:
                directory =  a[i]['href']
                if(".css" not in directory):
                    continue
                if "http" in directory or "https" in directory:
                    continue
                if "/" not in directory:
                    print (f"\n     {Wh}[ {Gr}DIR {Wh}] {Re}Pas de directory")
                elif not os.path.exists(os.path.dirname(directory)):
                    print (f"\n     {Wh}[ {Gr}DIR {Wh}] {Wh}Création du directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(URL+directory, directory, reporthook=report)   
                urls = list( cssutils.getUrls(cssutils.parseFile(directory)))
                if "fontawesome" in directory:
                    continue
                if(len(urls)!=0):
                    for link in urls:
                        try:
                            if "http" in directory or "https" in link or "data:image/" in link:
                                continue
                            while("../" in link):
                                if("assets" in link):
                                    link = link[3:]
                                else:
                                    link = "assets/"+link[3:]
                            if "/" not in link:
                                    print (f"\n     {Wh}[ {Gr}DIR {Wh}] {Re}Pas de directory")
                            elif not os.path.exists(os.path.dirname(link)):
                                print (f"\n     {Wh}[ {Gr}DIR {Wh}] {Wh}Création du directory")
                                os.makedirs(os.path.dirname(link))
                            testfile, headers = urlretrieve(URL+link, link, reporthook=report)
                        except Exception as e:
                            print (f"\n     {Wh}[ {Re}- {Wh}] {Wh}Problème : ",e)
            except Exception as e:
                print (f"\n     {Wh}[ {Re}- {Wh}] {Wh}Problème CSS: ",e)
        print (f"\n     {Wh}[ {Gr}+ {Wh}] {Gr}Les CSS sont loadées")
        time.sleep(2)
        print (f"\n{Wh}[ {Gr}3 {Wh}] {Wh}JS")
        a = soup.find_all('script')
        for i in range(len(a)):
            try:
                if(a[i].get('src')):
                    directory=a[i]['src']
                else:
                    continue
                if "http" in directory or "https" in directory:
                    continue
                if not os.path.exists(os.path.dirname(directory)):
                    print (f"\n     {Wh}[ {Gr}DIR {Wh}] {Wh}Création du directory")
                    os.makedirs(os.path.dirname(directory))
                testfile, headers = urlretrieve(URL+directory, directory, reporthook=report)
            except Exception as e:
                print (f"\n     {Wh}[ {Re}- {Wh}] {Wh}Problème JS : ",e)
        print (f"\n     {Wh}[ {Gr}+ {Wh}] {Gr}Les JS sont loadées")
        print (f"\n{Wh}[ {Gr}+ {Wh}] {Gr}Tout est bien fini")
except Exception as e:
    print (f"\n     {Wh}[ {Re}- {Wh}] {Wh}Problème : ",e)