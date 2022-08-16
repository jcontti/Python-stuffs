import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587) ## conecto con el servidor de mails de gmail
#type(conn)
conn.ehlo() ## pruebo la conexion
conn.starttls() # se encripta la conexion para que sea segura
conn.login('conttijorge@gmail.com', 'my_pass') # logeueo a mi cuenta, tengo que tener activado el "Acceso de apps menos seguras" en gmail
conn.sendmail('conttijorge@gmail.com', 'conttijorge@hotmail.com', 'Subject: So long...Test \n\nSending email from python app')
conn.quit() # cierro la conexion
