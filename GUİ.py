import sys

import customtkinter
import time
import os
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options

# options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
options=Options()
# options.add_argument("--headless=new")

service=Service("chromedriver.exe")
driver=webdriver.Chrome(service=service,options=options)
driver.implicitly_wait(20)

driver.get("https://tr.tradingview.com/")
# WebDriverWait(driver,30).until(ec.url_to_be("https://tr.tradingview.com/"))
# searchbar=driver.find_element(By.XPATH,value="//*[@id='tv-content']/div[1]/div[1]/div/div[1]/button")

# driver.execute_script("arguments[0].click();", searchbar)

# input=driver.find_element(By.NAME,value="query")
# input.send_keys("sahol")
# input.send_keys(Keys.ENTER)
# WebDriverWait(driver,30).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")))
# stockprice=driver.find_element(By.XPATH,value="/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")
# print(stockprice.text)
# driver.back()
# searchbar = driver.find_element(By.XPATH, value="//*[@id='tv-content']/div[1]/div[1]/div/div[1]/button")
# driver.execute_script("arguments[0].click();", searchbar)
# input = driver.find_element(By.NAME, value="query")
# input.send_keys("BTCUSD")
# input.send_keys(Keys.ENTER)
def getstockpricefromtradingview(sharename):
    if "symbol" in driver.current_url:
        driver.back()
        WebDriverWait(driver, 30).until(ec.url_to_be("https://tr.tradingview.com/"))
        searchbar = driver.find_element(By.XPATH, value="//*[@id='tv-content']/div[1]/div[1]/div/div[1]/button")
        driver.execute_script("arguments[0].click();", searchbar)
        input = driver.find_element(By.NAME, value="query")
        input.send_keys(sharename)
        input.send_keys(Keys.ENTER)
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")))
        stockprice = driver.find_element(By.XPATH,value="/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")
        print(stockprice.text)
    else:
        WebDriverWait(driver, 30).until(ec.url_to_be("https://tr.tradingview.com/"))
        searchbar = driver.find_element(By.XPATH, value="//*[@id='tv-content']/div[1]/div[1]/div/div[1]/button")
        driver.execute_script("arguments[0].click();", searchbar)
        input = driver.find_element(By.NAME, value="query")
        input.send_keys(sharename)
        input.send_keys(Keys.ENTER)
        WebDriverWait(driver, 30).until(ec.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")))
        stockprice = driver.find_element(By.XPATH,value="/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")
        print(stockprice.text)
getstockpricefromtradingview("BTCUSD")
#
# while True:
#     stockprice = driver.find_element(By.XPATH,value="/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")
#     print(stockprice.text)
#     time.sleep(3)

image_path_1=os.path.join(os.getcwd(),"koc--600.png")
image_path_2=os.path.join(os.getcwd(),"sabanci-holding--600.png")
image_path_3=os.path.join(os.getcwd(),"ulker-biskuvi--600.png")
image_pathrisingarrow=os.path.join(os.getcwd(), "risingarrow.png")
image_pathfallingarrow=os.path.join(os.getcwd(),"down-arrow.png")

customtkinter.set_appearance_mode("light")
app=customtkinter.CTk()
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry("800x600")

app.title("Bist")

# value = [21, 53, 12, 54, 23, 65, 75]
def returnfunc(root):
    root.destroy()
    ...

def printforvalue():
    app_forvalue = customtkinter.CTkToplevel()
    # app_forvalue.overrideredirect(True)
    app_forvalue.attributes("-topmost",True)
    app_forvalue.title("STAKE VALUE")
    app_forvalue.geometry('800x600')
    label_1 = customtkinter.CTkLabel(master=app_forvalue, text="Stake Value: ")
    label_1.pack(padx=12, pady=10)
    imagex = customtkinter.CTkImage(light_image=Image.open(image_pathrisingarrow), dark_image=Image.open(image_pathrisingarrow), size=(22, 22))
    image_label = customtkinter.CTkLabel(master=app_forvalue,text="",image=imagex)
    image_label.pack(padx=18, pady=20)
    imagey = customtkinter.CTkImage(light_image=Image.open(image_pathfallingarrow),dark_image=Image.open(image_pathfallingarrow),size=(22,22))

    button_return=customtkinter.CTkButton(master=app_forvalue,text="Return",command=lambda:returnfunc(app_forvalue),
                                 width=120,height=40,fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 hover_color="white",
                                 corner_radius=8,
                                 text_color="orange",)
    button_return.place(relx=0.5,rely=0.5,anchor=customtkinter.CENTER)
    comparisonlist=[]

    def update_label(index=0):
        if index<100:
            stockprice = driver.find_element(By.XPATH,value="/html/body/div[2]/div[6]/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/div[2]/span[1]/span[1]")
            comparisonlist.append(int(stockprice.text))
            label_1.configure(text=f"Stake Value: {stockprice.text}")
            print(index)
            if len(comparisonlist) > index:
                if int(stockprice.text) > comparisonlist[index-1]:
                    label_1.configure(text_color="green")
                    image_label.configure(image=imagex)
                elif int(stockprice.text) == comparisonlist[index-1]:
                    label_1.configure(text_color="blue")
                elif int(stockprice.text)< comparisonlist[index-1]:
                    label_1.configure(text_color="red")
                    image_label.configure(image=imagey)
                else:
                    print("Error Occured!!!")
            app_forvalue.after(1000, update_label, index + 1)
    update_label()
    app_forvalue.mainloop()

# def redirectionsection():
#     app_forvalue = customtkinter.CTk()
#     app_forvalue.title("STAKE VALUE")
#     app_forvalue.geometry('800x600')
#     label_1 = customtkinter.CTkLabel(master=app_forvalue, text="Stake Value: ")
#     label_1.pack(padx=12, pady=10)
#     # Label'i güncelleyen fonksiyon
#     def update_label(index=0):
#         if index < len(value):
#             # Index'ten değeri al
#             current_value = value[index]
#             # Etiketi güncelle
#             label_1.configure(text=f"Stake Value: {current_value}")
#             # Bir sonraki değeri almak için after() metoduyla fonksiyonu kendine çağır
#             app_forvalue.after(1000, update_label, index + 1)
#             if index+1<len(value):
#                 if value[index+1]>value[index]:
#                     label_1.configure(text_color="green")
#                 elif value[index+1]==value[index]:
#                     label_1.configure(text_color="blue")
#                 else:
#                     label_1.configure(text_color="red")
#     # İlk güncellemeyi tetikle
#     update_label()
#     app_forvalue.mainloop()

image_1=customtkinter.CTkImage(light_image=Image.open(image_path_1),size=(25, 25))
image_2=customtkinter.CTkImage(light_image=Image.open(image_path_2),size=(25, 25))
image_3=customtkinter.CTkImage(light_image=Image.open(image_path_3),size=(25, 25))
button_1=customtkinter.CTkButton(master=app,
                               text="SAHOL",#command=printforvalue,
                               image=image_2,

                               width=120,
                               height=40,
                               corner_radius=8,
                                 fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 hover_color="white",
                                 text_color="orange"
                                 )
button_2=customtkinter.CTkButton(master=app,text="KCHOL",
                                 image=image_1,
                                 compound="left",
                                 height=40,
                                 width=120,
                                 corner_radius=8,
                                 fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 hover_color="white",
                                 text_color="orange"
                                 )
button_3=customtkinter.CTkButton(master=app,text="ULKER",
                                 image=image_3,command=printforvalue,
                                 height=40,
                                 width=120,
                                 corner_radius=8,
                                 fg_color="transparent",
                                 border_color="white",
                                 border_width=2,
                                 hover_color="white",
                                 text_color="orange"
                                 )
button_1.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)
button_2.place(relx=0.5, rely=0.2, anchor=customtkinter.CENTER)
button_3.place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

label=customtkinter.CTkLabel(master=app,text="BIST MARKET")
#label.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)
label.pack(padx=12,pady=10)
app.mainloop()
driver.quit()