#作者：Napleon
#创建时间：2023/8/15
#模拟selenium浏览器打开问卷星网址，模拟点击选项，最后提交
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import numpy as np
import config
from selenium.webdriver import ActionChains

#base_url='https://www.wjx.cn/vm/Q2EFnd5.aspx'   #问卷地址
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
    browser = webdriver.Chrome(options=options, executable_path=path)

    return browser

def choose_click(browser,type,num,questions,weights):
    questions= list(range(1, questions+1))
    if type==4:     #不重复选取多选
        t = random.randint(1, len(questions)-1)
        results = np.random.choice(questions, size=t, replace=False, p=weights / np.sum(weights))
        for i in results:
            e=browser.find_element('xpath',f'//*[@id="div{num}"]/div[2]/div[{i}]')
            e.click()
    elif type==3:     #单选
        result = np.random.choice(questions, size=1, replace=False, p=weights / np.sum(weights))
        e = browser.find_element('xpath', f'//*[@id="div{num}"]/div[2]/div[{result[0]}]')
        e.click()
    elif type== 2:
        browser.find_element('xpath', f'//*[@id="q{num}"]').send_keys("无")
def auto_choose():
    browser = create_browser()
    browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
    browser.get(base_url)
    time.sleep(2)
    problems = [
        [3, 1, 4, [3,4,4,3]],
        [3, 2, 2, [5, 5]],
        [3, 3, 3, [3,1,1]],
        [3, 4, 4, [1,2,3,4]],
        [3, 5, 2, [1,2]],
        [3, 6, 3, [1,1,1]],
        [4, 7, 6, [1,1,1,1,1,1]],
        [4, 8, 5, [1,1,1,1,1]],
        [3, 9, 2, [1,1]],
        [3, 10, 2, [1,1]],
        [4,11,4,[1,1,1,1]],
        [4,12,7,[1,1,1,1,1,1,1]],
        [4,13,5,[1,1,1,1,1]],
        [4,14,5,[1,1,1,1,1]],
        [4,15,7,[1,1,1,1,1,1,1]],
    ]
    for p in problems:
        choose_click(browser, p[0],p[1],p[2],p[3])
        # time.sleep(2)
    # 提交按钮
    submit = browser.find_element('xpath', '//*[@id="ctlNext"]')
    submit.click()
    time.sleep(1)
    try:
        comfirm=browser.find_element('xpath','//*[@id="layui-layer1"]/div[3]/a')
        comfirm.click()
        time.sleep(0.5)
    except:
        pass
    try:
        button=browser.find_element('xpath','//*[@id="rectMask"]')
        button.click()
        time.sleep(5)
    except:
        pass
    try:
        slider = browser.find_element('xpath', '//*[@id="nc_1__scale_text"]/span')
        if str(slider.text).startswith("请按住滑块"):
            width = slider.size.get('width')
            ActionChains(browser).drag_and_drop_by_offset(slider, width, 0).perform()
            time.sleep(2)
    except :
        pass
    browser.quit()

if __name__ == '__main__':
    for i in range(1,config.loop_time+1):
        try:
            auto_choose()
            print(f'已提交{i}次问卷')
        except Exception as e:
            print(e)
        # time.sleep(10)



