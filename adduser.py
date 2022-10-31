import mysql.connector
from mysql.connector import Error
import os

adduser = str
info_user = str
USER = str
PASSWORD = str
EMAIL = str
DOMINIO = str
primero = str
segundo = str
tercero = str
lista_char = ["(", "'", ")", ","]


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='database_name',
                                         user='database_user',
                                         password='database_pass')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor(buffered=True)

        lead = ("SELECT lead_id FROM wp_vxcf_leads_detail "
         "WHERE value='0'")
        cursor.execute(lead)
        result = len(cursor.fetchall())
        numides = result
        print(result)
        print(numides)

        while numides >= 1:

            cursor.execute(lead)

            
            form = str(cursor.fetchone()[0])
            formulario = int(form)
            print(formulario)
            numides = numides - 1

            user_dominio = (formulario * 5) - 1
            temp_pass = int(user_dominio) - 1
            user_mail = int(temp_pass) - 1
            user_name = int(user_mail) - 1

            leadid = formulario * 5

            print(leadid)
            print(user_name, user_mail, temp_pass)

            query1 = "SELECT value FROM `wp_vxcf_leads_detail` WHERE (lead_id='" + str(formulario) + "') AND (id='" + str(user_name) + "');"
            query2 = "SELECT value FROM `wp_vxcf_leads_detail` WHERE (lead_id='" + str(formulario) + "') AND (id='" + str(user_mail) + "');"
            query3 = "SELECT value FROM `wp_vxcf_leads_detail` WHERE (lead_id='" + str(formulario) + "') AND (id='" + str(temp_pass) + "');"

            cursor.execute(query1)
            result = str(cursor.fetchall()[0])
            print(result)
            USER = result
            for character in lista_char:
                USER = USER.replace(character, "")

            cursor.execute(query2)
            result = str(cursor.fetchall()[0])
            print(result)
            EMAIL = result
            for character in lista_char:
                EMAIL = EMAIL.replace(character, "")

            cursor.execute(query3)
            result = str(cursor.fetchall()[0])
            print(result)
            PASSWORD = result
            for character in lista_char:
                PASSWORD = PASSWORD.replace(character, "")
            

#SSH alta ----------------------------------------------------------------------------------------------------------------------------------------------------
            
            info_user = USER + ' ' + PASSWORD + ' ' + EMAIL
            adduser = 'sudo v-add-user ' + info_user

            os.system(adduser)
            print('Nuevo usuario añadido: ',adduser)

#SSH alta ----------------------------------------------------------------------------------------------------------------------------------------------------

            delete_query = "UPDATE wp_vxcf_leads_detail SET value = '1' WHERE (id='" + str(leadid) + "');"
            cursor.execute(delete_query)

#Alta dominio ------------------------------------------------------------------------------------------------------------------------------------------------
            
            domain = "SELECT value FROM `wp_vxcf_leads_detail` WHERE (lead_id='" + str(formulario) + "') AND (id='" + str(user_dominio) + "');"
            cursor.execute(domain)
            result = str(cursor.fetchall()[0])
            print(result)
            DOMINIO = result
            for character in lista_char:
                DOMINIO = DOMINIO.replace(character, "")
                if DOMINIO == '' :
                    print('mamatis')

                else :
                    info_domain = USER + ' ' + DOMINIO
                    adddomain = 'sudo v-add-domain ' + info_domain
                    os.system(adddomain)
                    print(DOMINIO + ' AÑADIDO!!')


#Alta dominio ------------------------------------------------------------------------------------------------------------------------------------------------


except Error as e:
    print("Error al conectar con MySQL :(", e)




finally:
    if connection.is_connected():
        cursor.close()
        connection.commit()
        connection.close()
        print("Conexión con MySQL cerrada :)")
