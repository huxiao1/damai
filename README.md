# main
# 调用
def enter_concert()  
def choose_ticket()

# def enter_concert(self)
## 功能
进入到具体抢票页面  
## 调用
get_cookie()  
login()  
## 解析
```options.add_argument("--disable-blink-features=AutomationControlled")``` #这行代码向浏览器添加一个命令行参数 ```--disable-blink-features=AutomationControlled```。该参数的作用是禁用自动化控制功能。某些网站可能会检测自动化工具的使用，通过禁用这个功能可以避免被检测到，提高自动化脚本的稳定性和可靠性。  

capa = DesiredCapabilities.CHROME  
更换等待策略为不等待浏览器加载完全就进行下一步操作 capa["pageLoadStrategy"] = "none"  
页面DOM加载完后，再执行代码 capa["pageLoadStrategy"] = "eager"  

```locator = (By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/a[2]/div")``` 这段代码中的 ```"/html/body/div[1]/div/div[3]/div[1]/a[2]/div"``` 是一个 XPath 表达式，用于定位网页中的元素。  
/html：表示根节点是 ```<html>``` 元素。  
/html/body：表示 ```<body>``` 元素是 ```<html>``` 元素的直接子元素。  
/html/body/div[1]：表示第一个 ```<div>``` 元素是 ```<body>``` 元素的直接子元素。  
/html/body/div[1]/div：表示第一个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素。  
/html/body/div[1]/div/div[3]：表示第一个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素的子元素中的第三个 ```<div>``` 元素。  
/html/body/div[1]/div/div[3]/div[1]：表示第一个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素的子元素中的第三个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素。  
/html/body/div[1]/div/div[3]/div[1]/a[2]：表示第一个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素的子元素中的第三个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素的子元素中的第二个 ```<a>``` 元素。  
/html/body/div[1]/div/div[3]/div[1]/a[2]/div：表示第一个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素的子元素中的第三个 ```<div>``` 元素的子元素中的第一个 ```<div>``` 元素的子元素中的第二个 ```<a>``` 元素的子元素中的第一个 ```<div>``` 元素。  

# def get_cookie(self)
## 功能
获取cookie  
## 调用
## 解析
```dump(self.driver.get_cookies(), open("cookies.pkl", "wb"))``` 这行代码的作用是将当前浏览器的 cookies 保存到一个文件中。  
具体来说，self.driver.get_cookies() 返回一个包含当前浏览器的 cookies 信息的列表。然后，dump() 函数将该列表对象序列化，并使用二进制写入模式打开名为 "cookies.pkl" 的文件。通过这种方式，将浏览器的 Cookies 保存到了一个二进制文件中。  

# def login(self):
## 功能
登录函数，跳转到商品页面  
## 调用
def set_cookie()  
## 解析
```WebDriverWait(self.driver, 10, 0.1).until(EC.title_contains('商品详情'))```待页面的标题包含"商品详情"这个文本，最长等待时间为10秒，轮询间隔时间为0.1秒。如果在等待时间内标题包含了指定文本，程序将继续执行；如果超过最长等待时间仍未满足条件，将抛出超时异常。  
WebDriverWait 是一个等待类，它可以让程序等待某个条件满足后再继续执行。  
self.driver 是 WebDriver 对象，它代表浏览器窗口。  
10 是最长等待时间，单位是秒。这里设置为10秒，表示最长等待10秒。  
0.1 是轮询间隔时间，单位是秒。这里设置为0.1秒，表示每0.1秒检查一次条件是否满足。  
until 方法接受一个条件，表示等待条件满足后再继续执行。  
EC.title_contains('商品详情') 是一个条件，表示等待页面的标题包含"商品详情"这个文本。  

# def set_ticket(self):
## 功能
载入并读取cookie  
## 调用
## 解析
cookie.get('name') 获取Cookie的名称。  
cookie.get('value') 获取Cookie的值。  
self.driver.add_cookie(cookie_dict) 将每个Cookie添加到当前的WebDriver对象中。add_cookie 方法用于添加Cookie到当前会话中的浏览器。  

# def choose_ticket(self):
## 功能
实现购买函数  
## 调用
def set_cookie()  
## 解析

