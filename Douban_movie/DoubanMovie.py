#!/usr/bin/env python
# encoding=utf-8

import requests
import re
import codecs
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
dest_filename = 'Movie.xlsx'
ws1 = wb.active
ws1.title = 'MovieTop250'

DOWNLOAD_URL = 'http://movie.douban.com/top250/'

def download_page(url):
    header = {
        'User-Agent': 'Mozilla/5.0'
    }
