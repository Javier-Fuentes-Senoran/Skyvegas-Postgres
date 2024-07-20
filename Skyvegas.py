def Skyvegas():
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait #(html is slow)
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service
    
    
    from selenium.webdriver.support.ui import Select
    import time
    
    
    from selenium import webdriver

    ##OPTIONS#
    options =  webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    ##DRIVER
    
    driver_path="F:\chromedriver.exe"
    
    #### Route of the website ####
    
    try:
    
        driver=webdriver.Chrome(executable_path=driver_path,chrome_options=options)
        driver.get("https://www.skyvegas.com/must-go-jackpots")
        time.sleep(10)
    
    
    ##########CLOSE COOKIES###### 
    
        WebDriverWait(driver, 5)\
            .until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-accept-btn-handler']")))\
            .click()
        time.sleep(3) 
        
        
    except Exception as e:
    
        print(f"An error occurred: {e}")
        print("Skyvegas route has changed, it should be reviewed")
        driver.quit()  ###Closing Web ####
       
    
    ######### Current Value and Pool Jackpot ########
    
    
    try:
    
        elements_value='//*[@id="__next"]/main//div[2]/ul/li/div'    
   
        elements_data = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, elements_value)))
            
        values_data = [elements_data.text for elements_data in elements_data]  
    
        #print(values_data)
     
    
    ######### Extracting Current Value ########
    
        import re
    
        def extracting_current_value(STRING):
            
            ### Fixing Values
            
            match = re.search(r'£([\d,\.]+) Current value', STRING)
            if match:
                return match.group(1)
            return None

        ##Taking all Current values #######
    
        values_current_value = [extracting_current_value(STRING) for STRING in values_data]

        #print(values_current_value)
    
    
    ######### Extracting Pool Jackpots ########
    
        Pool_List=[]
    
        for pool in values_data:
            
            ### Fixing Pools
        
            match = re.search(r'£([\d,]+\.\d{2}) Must go value', pool)
            if match:
        ### Removing commas from the number and converting to float
                valor = match.group(1).replace(',', '')
                Pool_List.append(valor)
            
        #print(Pool_List) 
    
    except Exception as e:
    
        print(f"An error occurred: {e}")
        print("Skyvegas's path to get DATA VALUE (JACKPOTS AND POOLS) has changed or the data format has changed. It should be reviewed")
        driver.quit()  ###Closing Web ####
    
    

    ######### Names ########
    
    try:
        elements_name = driver.find_elements(By.XPATH, '//*[@id="__next"]/main//div[2]/ul/li/div[@data-analytics-context]')

        names = [element.get_attribute('data-analytics-context') for element in elements_name]

    ##Name List
    
        Name_list=[]

        for name in names:
            #print(name)
            Name_list.append(name)
            #print(Name_list)
    
    except Exception as e:
    
        print(f"An error occurred: {e}")
        print("Skyvegas's path to get DATA NAMES has changed or the data format has changed. It should be reviewed")
        driver.quit()  ###Closing Web ####
        
    time.sleep(15)  #####Time to close website, if we have an error in the main it will stop running.####
    
    driver.quit()  ###Closing Web ####
    
        
    ####Pandas-Data collection    
    
    try:
        import pandas as pd
    
        df = pd.DataFrame({"Name": Name_list, "Pool_Value": Pool_List ,"Current_Value": values_current_value})
    
        print(df)
    
        return df
    
    except Exception as e:
    
        print(f"An error occurred: {e}")
        print("There has a mistake. Pandas, Names, Jacpot or Pools should be reviewed")
       
#Skyvegas()      
  
    

    
    

        
        
