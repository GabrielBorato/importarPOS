##########Importar POS_FIN######################
###########Bibliotecas##############
from botcity.core import DesktopBot
from datetime import datetime, timedelta
import pandas as pd
from botcity.web import WebBot, Browser, By
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui 
import cx_Oracle
import os
#####################Configs###################
bot = DesktopBot()
def not_found(label):
    print(f"Element not found: {label}")
#################Conexão-banco##################
dados_conexao = {
    "user": "###########Secret-value###########################",
    "password": "###########Secret-value###########################",
    "dsn": "###########Secret-value############################"  }
try:
    conexao = cx_Oracle.connect(**dados_conexao)
    cursor = conexao.cursor()
    query = """
SELECT A.NROEMPRESA 
FROM GE_EMPRESA A
WHERE 1=1
AND A.STATUS = 'A'
AND A.NROEMPRESA NOT IN (95,96,97,98,800,900)
ORDER BY 1 """
    
    cursor.execute(query)
    resultados = cursor.fetchall()
    lista_loja_de_inteiros = [int(resultado[0]) for resultado in resultados]
    print (lista_loja_de_inteiros)
except cx_Oracle.DatabaseError as ex:
    print(f"Falha na conexão: {ex}")
if conexao:
     conexao.close()
    
################Open-Sitef######################
def operar_robo(data_recebida):
    try:
        data_formatada = datetime.strptime(data_recebida, "%d-%m-%Y")
        #campo_insert_data_formatada = f"K:\\Financeiro\\FECHAMENTO DE CAIXAS\\10 Conciliação de cartão POS\\Pasta Insert Arquivo Robô\\det_diversos_{data_formatada.csv}"
        #path2=f"K:\\Financeiro\\FECHAMENTO DE CAIXAS\\10 Conciliação de cartão POS\\Pasta Insert Arquivo Robô\\det_diversos_{data_formatada.csv}"
        print(data_formatada)
        operar_robo = True
        if operar_robo:
            return "Processamento concluído com sucesso."
    except Exception as e:
            return f"Erro durante o processamento"    
        if os.path.exists(path2):
            os.remove(path2)
        else:
            bot.click_at(x=1900, y=8)
            path = r'C:\\Users\\gabriel.borato\\Desktop\\sitefwebjws.jnlp'
            bot.execute(path)
            bot.wait(10000)
            bot.tab()
            bot.tab()
            bot.space()
            bot.enter()
            bot.wait(2000)
            bot.kb_type("Automate")
            bot.tab()
            bot.kb_type("4N-1W#8Y")
            bot.tab()
            bot.enter()
            bot.wait(3000)
        ###############Extração-Arquivo-Sitef#############
            bot.click_at(x=504, y=136)
            bot.wait(1000)
            bot.click_at(x=550, y=158)
            bot.wait(8000)
            bot.click_at(x=32, y=208)
            bot.type_keys(data_formatada)
            bot.tab()
            bot.type_keys(data_formatada)
            bot.click_at(x=935, y=209)
            bot.type_down()
            bot.type_down()
            bot.enter()
            bot.click_at(x=1698, y=950)
            bot.wait(1000)
            bot.click_at(x=905, y=231)
            bot.wait(1000)
            bot.click_at(x=920, y=775)
            bot.wait(1000)       
            bot.tab()
            bot.tab()
            for _ in range(3):
                bot.type_down()
                bot.enter()
                bot.click_at(x=960, y=828)
                bot.click_at(x=1696, y=882)
                bot.wait(20000)
                bot.type_keys(campo_insert_data_formatada)      
                bot.enter()
                bot.wait(10000)
                bot.enter()
                bot.click_at(x=1900, y=8)
                bot.wait(5000)
        #############Input-Arquivo-Consinco#############
            bot.click_at(x=1900, y=8)
            bot.type_windows()
            bot.wait(5000)
            bot.type_keys(r"C:\C5Client\Tesouraria\tesouraria.exe")
            bot.enter()
            bot.wait(7000)
            bot.type_keys("automate")
            bot.wait(1000)  
            bot.tab()  
            bot.type_keys("889911")
            bot.tab()           
            bot.tab()   
            bot.enter()
            bot.wait(5000)
            bot.click_at(x=165, y=37)
            bot.wait(1000)
            bot.click_at(x=230, y=362)
            bot.wait(1000) 
            bot.click_at(x=160, y=144)
            for _ in range(10):
                bot.backspace()
                bot.type_keys(data_formatada)
                bot.click_at(x=218, y=93)
                bot.wait(1000)
                bot.click_at(x=464, y=165)
                bot.wait(1000)
                bot.type_keys(campo_insert_data_formatada)
                bot.enter()
                bot.wait(10000)
                bot.click_at(x=122, y=107)
                bot.enter()
                bot.click_at(x=472, y=74)
                bot.wait(20000)    
        ################ insert loja #############
                def processar_loja(loja_str):
                    pyautogui.hotkey('ctrl', 'shift', 't')
                    bot.wait(1000)
                for _ in range(3):
                    bot.tab()
                    bot.type_keys(loja_str)
                    bot.enter()
                    bot.wait(5000)
                    bot.click_at(x=105, y=95)
                    bot.wait(5000)   
                print(f"Processando loja: {loja}")
                for loja in lista_loja_de_inteiros:
                    loja_str = str(loja)  
                    processar_loja(loja_str)
                    bot.click_at(x=1005, y=67)
                    bot.click_at(x=1894, y=8)          
    













   
















  



                     
                   

