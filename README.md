# Qualtrics Survey Automatic Form Filling Bot

## Quickstart

### 1. Install webdriver

記得先安裝對應自己瀏覽器的 webdriver，然後把 `webdriver` 的路徑填入 `driver = webdriver.Chrome(executable_path='your webdriver path')`

```python
driver = webdriver.Edge(
    executable_path='your webdriver path',
    options=options
)
```

### 2. Fill in your Form URL

```python
driver.get('your-form-url')
```

## Intro

**面對那些久違的友人蓦然來訊 ：可以幫我填我的論文問卷表單嗎？**

面對這種窘境。我們可以告訴他們：

>「*當互不相識的相逢如夢初醒，風華絕代的詩句在心中迴繞。這突如其來的噓寒問暖，似乎意味著一種交流的復興，然而一直沒有想到，卻是一張問卷表單的填寫。這般瑣碎的事務，我們是否可以共同破繭而出，尋找更有意義的交談*？」

對於那些不懈追求時間節省的人，或許我們可以巧妙地以成語來回敬：

> 「*物換星移，光陰似箭，自古以來，時光如水，從未停止奔流。在這浩瀚的宇宙中，人們都渴望尋找自由，追求與心靈對話的樂趣。讓我們以自動填單機器人的力量，融入這無窮的宇宙之中，為自己保留寶貴的時光，讓彼此的關懷與真誠得以延續*。」

不要再浪費自己時間，趕緊用自動填單機器人回敬

> 目前此專案只針對 [Qualtrics Survey](https://qfreeaccountssjc1.az1.qualtrics.com/jfe/form/SV_5o2C7kKPPPJGSMK) 去進行自動填單
> 未來會持續針對各種表單平台開發高速自動填單 BOT

## Demo

https://github.com/youngOman/qualtrics-auto-form-filler/assets/85870590/d4671a05-fd43-4767-8359-745f8d4463b6

## Upcoming Features

- [x] [Qualtrics Survey](https://qfreeaccountssjc1.az1.qualtrics.com/jfe/form/SV_5o2C7kKPPPJGSMK)
- [ ] [Google Form](https://docs.google.com/forms/u/0/?tgif=d)