#PARSER DELLA PAGINA 
#http://openlab.dibris.unige.it/index.php/lego
#PER RITORNARE UNA LISTA DI PROGETTI ATTIVI SOTTO FORMA DI STRINGA

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def funcParserHTML(url):

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        filterHTML = soup.find_all(headers="categorylist_header_title")
        filterHTML = str(filterHTML)
        soup = BeautifulSoup(filterHTML, 'html.parser')

        filterProjects = soup.get_text()
        filterProjects = filterProjects.replace(r'\t', '')
        filterProjects = filterProjects.replace(r'\n', '')
        filterProjects = filterProjects.replace(r']', '')
        filterProjects = filterProjects.replace(r'[', '')
        filterProjects = filterProjects.replace(r',', '\n\n')
        #print filterProjects
        return filterProjects