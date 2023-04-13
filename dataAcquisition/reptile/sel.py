from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# 获取详细信息


def getInfo(id:int):
    option = webdriver.ChromeOptions()
    option.add_argument('-headless')  # 设置option
    driver = webdriver.Chrome()  # 调用带参数的谷歌浏览器

    # driver = webdriver.Chrome()
    # 超时时间
    driver.set_page_load_timeout(30)
    try:
        driver.get('https://www.themoviedb.org/movie/{}'.format(id))
    except:
        return 0
    # time.sleep(2)
    # driver.implicitly_wait(20)  # 隐性等待，最长等30秒
    d = {}
    # 标题
    d['title'] = driver.title.split(' ')[0]
    # 发行时间，类型，时长
    facts = driver.find_element(By.CSS_SELECTOR, '.facts')
    d['release_date'] = facts.find_element(By.CSS_SELECTOR, '.release').text.split('(')[0].strip()
    d['types'] = facts.find_element(By.CSS_SELECTOR, '.genres').text
    d['runtime'] = facts.find_element(By.CSS_SELECTOR, '.runtime').text
    # 名言
    try:
        d['lines'] = driver.find_element(By.CSS_SELECTOR, '.tagline').text
    except:
        d['lines'] = ''
    # 评分
    d['grade'] = float(driver.find_element(By.CSS_SELECTOR, '.percent span').get_attribute('class').split('icon-r')[-1])
    # 简介
    d['desc'] = driver.find_element(By.CSS_SELECTOR, '.overview').text
    # 预算与票房
    total = driver.find_elements(By.CSS_SELECTOR, '.left_column p')
    try:
        d['budget'] = float(total[3].text.replace('预算\n$', '').replace(',', ''))
        d['boxoffice'] = float(total[4].text.replace('票房\n$', '').replace(',', ''))
    except:
        if not 'budeget' in d:
            d['budget'] = 0
        if not 'boxoffice' in d:
            d['boxoffice'] = 0
    # 背景与封面
    try :
        d['background'] = driver.find_element(
        By.CSS_SELECTOR, '.backdrop img.backdrop').get_attribute('src')
    except:
        d['background'] = ''
    try:
        d['cover'] = driver.find_element(
        By.CSS_SELECTOR, 'img.poster').get_attribute('src')
    except:
        d['cover'] = ''
    driver.quit()
    return d
# print(getInfo(38288))