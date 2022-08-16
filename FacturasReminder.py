# Facturas Reminder Application 

import xlrd # Reading an excel file needs
import smtplib # to send emails
from datetime import datetime # time module is must as reminder  


facturasFile = 'C:/Python/Facturas_Viernes.xlsx'
#facturasDay = datetime.today().strftime('%d-%m-%Y')
facturasDay = '15/11/2019'


## tengo que recorrer primero las columnas y buscar la fecha, 
## si la encuentro, en esa columna recorro las filas de ESA col para sacar la X y el nombre del q tiene q comprar.

# Convertor porque hay problemas a la hora de capturar la fecha la trae como un float ejemplo, 12/10/2019 pone algo asi "48696.0"
def floatHourToTime(fh):
    h, r = divmod(fh, 1)
    m, r = divmod(r*60, 1)
    return (
        int(h),
        int(m),
        int(r*60),
    )

def sendEmail(globerEmail):
    conn = smtplib.SMTP('smtp.gmail.com', 587) ## conecto con el servidor de mails de gmail
    #type(conn)
    conn.ehlo() ## pruebo la conexion
    conn.starttls() # se encripta la conexion para que sea segura
    conn.login('conttijorge@gmail.com', 'my_pass') # logeueo a mi cuenta, tengo que tener activado el "Acceso de apps menos seguras" en gmail
    conn.sendmail('conttijorge@gmail.com', globerEmail, 'Subject: Facturas reminder \n\nSending email from python app')
    conn.quit() # cierro la conexion
  
def checkTodaysFacturas(): 
    # Para abrir el Workbook 
    workbook = xlrd.open_workbook(facturasFile)
    for sheet in workbook.sheets():
        
        for column in range(sheet.ncols) :
            excel_date = sheet.cell(0,column).value

            if excel_date != '' :
                dt = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(excel_date) - 2)
                hour, minute, second = floatHourToTime(excel_date % 1)
                dt = dt.replace(hour=hour, minute=minute, second=second)

                colDay = str(dt.day) + '/' + str(dt.month) + '/' + str(dt.year)
                if colDay == facturasDay : # Busco si es día de facturas
                    print ('We found the day ! ')

                    for row in range(1 ,sheet.nrows): # busco la X en ese día y el nombre
                        if sheet.cell(row,column).value == 'X' :
                            name1 = sheet.cell(row,1).value
                            name2 = sheet.cell(row+1,1).value
                            
                            #globerEmail = sheet.cell(row,0).value  # mail
                            #sendEmail(globerEmail) # Envio mail a los seleccionados

                            if name2 != '' :
                                print('Compran facturas: ' + name1 + ' y ' + name2) # row donde encontre la x, el 1 es la columna que contiene el name
                                break
                            else:
                                print('Compra facturas: ' ) + name1
                                break

checkTodaysFacturas()
