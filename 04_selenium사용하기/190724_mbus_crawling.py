# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 19:23:28 2019

@author: hsh01
"""
# 셀레늄으로 동적 크롤링 해보기
# 주제 : mbus의 지하철역 검색&크롤링
# 사이트 : http://m.bus.go.kr/mBus/subway.bms

#%%
# 공통 실행 코드

## 1-2. import
from selenium import webdriver
from bs4 import BeautifulSoup

### 다운받은 크롬드라이브를 
driver = webdriver.Chrome('C:/Users/hsh01/python_class/class_01/chromedriver.exe')

### 3초간의 시간 주기
driver.implicitly_wait(3)

### 고객센터-자주 묻는 질문 url에 들어가기
driver.get('http://m.bus.go.kr/mBus/subway.bms')

# click radio button
#python_button = driver.find_elements_by_xpath('//*[@id="contents"]/div/div[1]/div[1]')[0]
#python_button.click()

# user_input으로 받아서 사용해보기
user_input = input('역명을 입력하세요.')

# 검색어 입력
# 창이 뜨더라도 무시하고 spyder로 돌아와 
# Console(출력창)으로 돌아와서 역명을 입력하세요.

# 하위 코드를 설명하자면 셀레늄 자체로 크롤링하려면 find가 아닌 find_element_by_~~()
# find_all이 아닌 find_elements_by_~~() 함수를 이용합니다.
search_station = driver.find_element_by_id("search")
search_station.send_keys(user_input)
# send_keys()함수는 값을 보내라는 것으로 콘솔창에 입력하면 셀레늄 창에서도 입력이 됩니다.


# 역명 입력, 엔터치고 다음 셀을 실행합시다.

#%%
# 역명이 입력되었으니 이제 클릭을 명합니다.
driver.find_element_by_id('searchIcon').click()

# 이제 원하는 값을 가져옵시다.
# 두가지 경우가 있습니다.
# 역이 하나만 검색되는 경우와
# 역이 둘 이상 검색되는 경우
# class명 stnm은 역 둘 이상인 경우를 나타냅니다.
# class명 title은 역이 하나만 검색되는 경우입니다.
# 만약 stnm이 [] 빈 리스트라면
# 역이 둘 이상 검색된 것이 아니라는 뜻이고
# 그러므로 class명이 title인 것의 텍스트만 추출되어 search_results라는 결과에 저장합니다.
# 만약 stnm이 [] 빈 리스트가 아니라면
# 역이 둘 이상 검색되었다는 뜻이겠지요?
# 그러므로 class명이 stnm인 값들의 텍스트만 추출되어 search_results라는 결과에 저장합니다.
stations_lists = driver.find_elements_by_class_name('stnm')

if stations_lists == []:    
    stations_lists = driver.find_elements_by_class_name('title')
    search_results=stations_lists[1].text


else:
    search_results=[]
    for i in stations_lists:
        search_results.append(i.text)
    

