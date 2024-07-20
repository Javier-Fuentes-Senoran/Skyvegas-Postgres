######Calling function Skybevas and Data Collection


i=0

while True: ###at 
       
    try:
        from Skyvegas import Skyvegas
        df=Skyvegas()
    
        print(df) ###Visualizing Data Frame
        
    except Exception as e:        
        print(f"An error occurred: {e}")
        print("Skyvegas.py has a mistake, this file should be reviewed")
        
    try:    
    
    #####Times for Data###

        from datetime import datetime
        from datetime import date
        import time

        Day=time.strftime("%d/%m/%y")

        print(type(Day))

        Hour=time.strftime("%H:%M:%S")

        print(Hour)

####Connection Postgres and Data Compilation###

        import psycopg2
   
        connection=psycopg2.connect(
            host="localhost",
            user="postgres",  ###User
            password="JaviPost",  ###Password
            database="Skyvegas",
            port="5432"    
        )

        connection.autocommit=True

#####Dragons Luck 1k####

        filtered_df_DL_1k = df.loc[(df['Name'] == 'Aurum Codex') & (df['Pool_Value'] == '1000.00'),'Current_Value'].values[0]

        filtered_df_DL_1k=float(filtered_df_DL_1k.replace(',', ''))

        print(filtered_df_DL_1k)

        filtered_df_DL_1k=float(filtered_df_DL_1k)


        query_DL_1k="INSERT INTO dragon_luck_1k   VALUES('{}', '{}', '{}')".format(Day,Hour,filtered_df_DL_1k) 

        cursor=connection.cursor()

        cursor.execute(query_DL_1k)


#####Dragons Luck 3k####

        filtered_df_DL_3k = df.loc[(df['Name'] == 'Aurum Codex') & (df['Pool_Value'] == '3000.00'),'Current_Value'].values[0]

        filtered_df_DL_3k=float(filtered_df_DL_3k.replace(',', ''))

        print(filtered_df_DL_3k)

        filtered_df_DL_3k=float(filtered_df_DL_3k)
    

    ### Insterting data into Postgress
    
        query_DL_3k="INSERT INTO dragon_luck_3k   VALUES('{}', '{}', '{}')".format(Day,Hour,filtered_df_DL_3k) 

        cursor=connection.cursor()

        cursor.execute(query_DL_3k)



#####Dragons Luck 5k####

        filtered_df_DL_5k = df.loc[(df['Name'] == 'Aurum Codex') & (df['Pool_Value'] == '5000.00'),'Current_Value'].values[0]

        filtered_df_DL_5k=float(filtered_df_DL_5k.replace(',', ''))

        print(filtered_df_DL_5k)

        filtered_df_DL_5k=float(filtered_df_DL_5k)


    ### Insterting data into Postgress  

        query_DL_5k="INSERT INTO dragon_luck_5k   VALUES('{}', '{}', '{}')".format(Day,Hour,filtered_df_DL_5k) 

        cursor=connection.cursor()

        cursor.execute(query_DL_5k)


####Extraction Data. Reviewing data

        connection.autocommit=True

        cursor=connection.cursor()

        query="SELECT * FROM dragon_luck_1k LIMIT 100"

        cursor.execute(query)

        rows=cursor.fetchall()

        for row in rows:
            print(row)     
       
    
###Loop-Break
    
    except Exception as e:
    
        print(f"An error occurred: {e}")
        
        #####Skyvegas.py, there is a time sleep, if we have an error in the main it will stop running.####
       
        break 
    
        import time
    
        time.sleep(60)###  TIME REQUESTING   #####    
    
    

    
 