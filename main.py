#作者：aoyijiaozhu
#创建时间：2023/8/14
#模拟selenium浏览器打开问卷星网址，模拟点击选项，最后提交
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import numpy as np
import config
from selenium.webdriver import ActionChains

#base_url='https://www.wjx.cn/vm/Qkp42ud.aspx'   #问卷地址
#path =  'chromedriver.exe'     # 驱动目录
base_url=config.base_url
path=config.path
max_num=config.max_num

#//*[@id="div题号"]/div[2]/div[选项数字]/div
#max_num=15 #题目数量：15
#题目类型，3是单选，4是多选

def create_browser():      #创建浏览器，返回一个browser对象
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('--headless')
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36"')
    options.add_argument("--proxy-server=http://" + '218.75.102.198:8000')  # 还没想好，待添加
    browser = webdriver.Chrome(service=Service(path))
    return browser

def choose_click(browser,type,num,questions,weights):
    questions= list(range(1, questions+1))
    if type==4:     #不重复选取多选
        t = random.randint(1, len(questions)-1)
        results = np.random.choice(questions, size=t, replace=False, p=weights / np.sum(weights))
        for i in results:
            e=browser.find_element('xpath',f'//*[@id="div{num}"]/div[2]/div[{i}]/div')
            e.click()
    elif type==3:     #单选
        result = np.random.choice(questions, size=1, replace=False, p=weights / np.sum(weights))
        e = browser.find_element('xpath', f'//*[@id="div{num}"]/div[2]/div[{result[0]}]/div')
        e.click()
def auto_choose():
    browser = create_browser()
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    browser.get(base_url)
    time.sleep(1)
    choose_click(browser,3, 1, 2, [5, 5])
    choose_click(browser,3, 2, 5, [1, 28, 5, 1, 0])
    choose_click(browser,3, 3, 5, [1, 2, 9, 21, 5])
    choose_click(browser,3, 4, 3, [4, 7, 5])
    choose_click(browser,3, 5, 2, [9, 1])
    choose_click(browser,3, 6, 2, [13, 1])
    choose_click(browser,3, 7, 2, [8, 1])
    choose_click(browser,4, 8, 5, [5, 1, 2, 9, 7])
    choose_click(browser,4, 9, 7, [5, 9, 2, 1, 1, 6, 8])
    choose_click(browser,3, 10, 4, [5, 8, 12, 3])
    choose_click(browser,3, 11, 4, [5, 14, 9, 1])
    choose_click(browser,3, 12, 4, [2, 7, 15, 5])
    choose_click(browser,3, 13, 4, [7, 5, 4, 2])
    choose_click(browser,3, 14, 3, [15, 7, 5])
    choose_click(browser,4, 15, 8, [5, 6, 4, 6, 3, 5, 7, 9])
    submit = browser.find_element('xpath', '//*[@id="ctlNext"]')
    submit.click()
    time.sleep(1)
    try:
        slider = browser.find_element('xpath', '//*[@id="nc_1__scale_text"]/span')
        if str(slider.text).startswith("请按住滑块"):
            width = slider.size.get('width')
            ActionChains(browser).drag_and_drop_by_offset(slider, width, 0).perform()
    except :
        pass
    browser.quit()

if __name__ == '__main__':
    for i in range(1,config.loop_time+1):
        try:
            auto_choose()
            print(f'已提交{i}次问卷')
        except:
            print(f'第{i}次问卷提交失败')



