### ¿Te encontraste este test por casualidad?
### No te preocupes, realiza la prueba y envíanos tu cv a dharwin@urbvan.com

# Introducción
Hola *aspirante*,

Bienvenido a la prueba técnica para la vacante de **backend developer** en urbvan. El objetivo de esta prueba es analizar tus habilidades para solucionar problemas y la forma en como te desenvuelves a la hora de **tirar código**.

# Objetivos
- Crea un CRUD para cada modelo.
- Agregar un sistema de permisos por servicio y 3 categorias de usuarios.
- Documenta el código.
- Crea pruebas unitarias.
- Hay errores y warnings puestos en el código, encuéntralos y crea un fix.
- Crea commits descriptivos.
- Crear un archivo Dockerfile para correr el proyecto con nginx y wsgi.
- Crear un router para separar la base de datos de lectura y escritura. 


La prueba tiene un tiempo para desarrollarse de 3 días, si tienes alguna duda por favor, házmela saber.


Recuerda, en **URBVAN** queremos a los mejores y sabemos que tú puedes ser uno de ellos.

# Running the app
To run the app execute the following commands:
```  
$ docker-compose up --build -d
$ docker-compose run web python manage.py makemigrations
$ docker-compose run web python manage.py migrate 
$ docker-compose run web python manage.py collectstatic --no-input --clear 

```

###For logs:  
Nginx  
docker-compose logs nginx  
Web  
docker-compose logs web  
DB  
docker-compose logs db  

###For shell accessing: 
Nginx  
docker exec -ti nginx bash  
Web  
docker exec -ti web bash  
Database  
docker exec -ti db bash  

