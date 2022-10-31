# AddUser_VestaCP

Script that automates the creation of users in the Vesta control panel from a wordpress form.

Script que automatiza la creación de usuarios en el panel de control de Vesta a partir de un formulario en wordpress.

The script is intended to be scheduled in a system cron every 3 minutes.

El script está pensado para programarlo en un cron del sistema cada 3 minutos.

First you have to configure the access data to the database where the data from the new registration form is temporarily stored.

Primero hay que configurar los datos de acceso a la base de datos donde se almacenan temporalmente los datos del formulario de nuevas altas.

When the script is executed it accesses the database and looks for the new registered users (in this case they are identified with a value = 0 in a database column), then it creates the new users, the domains, the dns, the e-mails…
all based on the form you create previously.

Cuando el script se ejecuta accede a la base de datos y busca los usuarios nuevos registrados (en este caso se identifican con un valor = 0 en una columna de la base de datos), luego crea los usuarios nuevos, los dominios, los dns, los correos electrónicos… 
todo en base al formulario que crees previamente.
