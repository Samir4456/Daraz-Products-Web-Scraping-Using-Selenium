from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys



urls = [

    'https://www.daraz.com.np/' 
        
        ]
s = Service(r"C:\Program Files\driver\chromedriver.exe")

for url in urls:
    driver = webdriver.Chrome(service=s)
    driver.get(url)


#searching
search_box=driver.find_element(By.ID,"q")

search_box.clear()

search_box.send_keys("Watch")
driver.find_element(By.XPATH,'//*[@id="topActionHeader"]/div/div[2]/div/div[2]/form/div/div[2]/button').click()


watch_name=[]
watch_price=[]
watch_reviews=[]


base_url = 'https://www.daraz.com.np/catalog/?_keyori=ss&from=input&page={page_number}&q=Watch&spm=a2a0e.searchlist.pagination.3.347c433ceRwh0G'


for page_number in range(1,102):  # Adjust the range as needed
    url = base_url.format(page_number=page_number)







    names=driver.find_elements(By.XPATH,'//div[@class="title-wrapper--IaQ0m"]')
    
    for name in names:
        watch_name.append(name.text)
    
    #price
    
    prices=driver.find_elements(By.XPATH,'//span[@class="currency--GVKjl"]')
    
    for price in prices:
        watch_price.append(price.text)
        
        
    #reviews
    
    reviews=driver.find_elements(By.XPATH,'//span[@class="ratig-num--KNake rating--pwPrV"]')
    
    for review in reviews:
        watch_reviews.append(review.text)

print("name===>",len(watch_name))
print("price=====>",len(watch_price))
print("review=====>",len(watch_reviews))

                  

            
import pandas as pd


df=pd.DataFrame(zip(watch_name,watch_price,watch_reviews),columns=['Watch_Name','Watch_Price','Watch_Review'])
df.to_excel(r"C:\Users\acer\Documents\webscrapping\watches_multiple.xlsx",index=False)












