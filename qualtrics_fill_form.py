from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import time
import random

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# 創建一個新的 Selenium 瀏覽器實例
driver = webdriver.Edge(
    executable_path='/Users/young/python_projects/fill_form_bot/msedgedriver',
    options=options
)

# 打開你想要填寫的網頁表單
driver.get('https://qfreeaccountssjc1.az1.qualtrics.com/jfe/form/SV_7VA5FzxUFVOmfae')

# 使用 BeautifulSoup 解析網頁
soup = BeautifulSoup(driver.page_source, 'html.parser')
# 首先找到並點擊 'NextButton' 按鈕
next_button = driver.find_element(By.ID, 'NextButton')
next_button.click()
# 等待網頁加載完畢
time.sleep(2)

# 找到所有的問題區塊
question_blocks = driver.find_elements(By.CSS_SELECTOR, 'div.QuestionOuter.BorderColor')

# 迭代每個問題區塊
for question_block in question_blocks:
    # 找到問題區塊中的 ul.ChoiceStructure 元素
    choice_structure_element = question_block.find_element(By.CSS_SELECTOR, 'ul.ChoiceStructure')
    # 找到 ul.ChoiceStructure 元素下的所有 li.Selection.reg 元素
    selection_elements = choice_structure_element.find_elements(By.CSS_SELECTOR, 'li.Selection.reg')

    if len(selection_elements) > 0:
        # 隨機選擇一個 li.Selection.reg 元素
        selected_element = random.choice(selection_elements)

        # 找到選擇的 li.Selection.reg 元素中的 <input> 元素
        input_element = selected_element.find_element(By.CSS_SELECTOR, 'input')

        # 找到 input 元素的父元素並執行點擊操作
        parent_element = input_element.find_element(By.XPATH, './..')
        parent_element.click()
        # time.sleep(0.5)
    else:
        print("No options found in ul.ChoiceStructure")

# 若網頁有多頁，找到下一頁按鈕並點擊
next_button = driver.find_element(By.ID, 'NextButton')
next_button.click()
# 等待網頁加載完畢
time.sleep(1)

while True:
    # 解析網頁
    question_rows = driver.find_elements(By.CSS_SELECTOR, 'tr.ChoiceRow')
    print("question_rows:", len(question_rows))
    # 判斷是否已經遍歷完所有問題區塊
    if not question_rows:
        break
    # 迭代每個題目
    for question_row in question_rows:
        # 找到題目中的所有選項
        td_elements = question_row.find_elements(By.CSS_SELECTOR, 'td[class^="c"]')
        if len(td_elements) > 0:
            # 隨機選擇一個選項
            selected_td = random.choice(td_elements)
            # 找到選擇的 td 元素中的 <input> 元素
            input_element = selected_td.find_element(By.CSS_SELECTOR, 'input[type="radio"]')
            # 使用 ActionChains 对象执行点击操作
            actions = ActionChains(driver)
            actions.move_to_element(input_element).click().perform()
        else:
            print("No options found in question row")

    # 若網頁有多頁，找到下一頁按鈕並點擊
    next_button = driver.find_element(By.ID, 'NextButton')
    next_button.click()
    # 等待網頁加載完畢
    time.sleep(2)
    # 關閉瀏覽器
    # driver.quit()
