VIDEO DE YOUTUBE (Demostración del proyecto) : https://youtu.be/Hq3FT5seH1c 
###Proyecto_final- TAPPERO MARIA LUZ

Este proyecto realizado en python-django; tiene como funciones:
-Acceder a una pagina web.
-Visualizar blogs subidos por todos los usuarios. 
-Visualizar blogs subidos por mi usuario.
-SignIn, LogIn y LogOut.
-Crear, editar y eliminar blogs.
-Crear comentarios sobre blogs de otros usuarios.
-Cear y editar un perfil con información sobre el usuario, con descripcion y avatars.


0- Installar Django con el comando pip install django

----------------------------------------------------------------------------------------------------------

1- Se creo un repositorio de git-hub con el nombare Proyecto_final-main; y dentro de ésta se ejecuto el comando:
    - django-admin startproject ProyectoFinal. (crea un archivo llamado ProyectoFinal, donde se encuentra el archivo de settings general del proyecto)
    Dentro de ésta ultima carpeta se ejecutaron los comandos:
    - python manage.py startapp Home
    - python manage.py startapp Blog

----------------------------------------------------------------------------------------------------------

2- URL
En la app Home se encuentran las siguientes url:
    urlpatterns = [
        path('', views.Home, name='Home'),
        path('about_me/', views.About, name='about_me'),
        path('registro/', views.registro_view, name='registro'), 
        path('login/', views.login_view, name='login'),
        path('logout/', LogoutView.as_view(template_name='Home/logout.html'), name='logout'),
        path ('profile/<id>', views.profile_view, name='profile'), 
        path('profile_create/',views.profile_create, name='profile_create'),
        path('profile_update/', views.profile_update, name= 'profile_update'), # type: ignore
        path('crear_avatar/', views.crear_avatar, name= 'crear_avatar'), # type: ignore
        path('update_avatar/', views.update_avatar, name='update_avatar')
    
        ]
    if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    En la app Blog se encuentran las siguientes url:

    urlpatterns = [
    path ('Blogs/', views.Blogs, name='Blogs'),
    path ('blog_create/', views.BlogCreate.as_view(), name='blog_create'),
    path ('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path ('blog_update/<pk>', views.BlogUpdate.as_view(), name='blog_update'),
    path ('blog_delete/<pk>', views.BlogDelete.as_view(), name='blog_delete'),
    path('mis_blog_list/<id>/', views.MisBlogList, name= 'mis_blog_list'),
    
    path ('comentario_create/<int:blog_pk>', views.ComentarioCreate.as_view(), name='comentario_create')
    ]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

----------------------------------------------------------------------------------------------------------

3-MODELOS
    En la app de Home se encuentra el modelo:
    -Avatar
    En la app de Blog se encuentra el modelo:
    -Perfil
    -Blog
    -Comentario

    Por ultimo, se ejecutaron los comandos para crear las tablas en la base de datos, posteriormente checkeado en DB browser:
    >> python manage.py makemigrations
    >> python manage.py migrate
----------------------------------------------------------------------------------------------------------

4-VISTAS
    En la app Home se encuentran definidas las vistas de:
    Home
    Registro
    Login
    Logout
    Profile Create & Update
    Avatar Create & Update

    En la app de Blog se encuentran definidas las vistas de:
    Blogs
    Mis Blogs 
    Blog Create, UpDate, Detail, & Delete
    Comentario Create

----------------------------------------------------------------------------------------------------------

5-FORMULARIOS
    En la app de Home, hay un archivo llamado forms.py donde se desarrolla los formularios para Creación, Edicion de usuario, para creación de perfil, y creación de Avatar.


    En la app de Blog, hay un archivo llamado forms.py donde se desarrolla el formulario ComentarioForm; 
    el cual luego se lo llama desde la vista para crear comentarios.
----------------------------------------------------------------------------------------------------------

6- CONTENIDO DE HTML(Templates)
    En la app Home, se encuentra una carpeta llamada static, la cual contiene archivos de css, que le dan el estilo a la página; y otra carpeta llamada Templates/Home, la cual tiene el index, navbar, header, footer, y los templates que responden a las vistas de login, signin, logout, profile & Avatar.

    En la app Blog, se encuentra la carpeta llamada Templates/Home, la cual hereda contenido de Home, y ademas responde a las vistas del CRUD de Blog.
----------------------------------------------------------------------------------------------------------

7- En la carpeta media dentro de la carpeta ProyectoFinal se encuentran las carpetas:
    -media/avatares: se guardan las imagenes del avatar de los usuarios.
    -media/blogs: se guardan las imagenes de los blogs.

----------------------------------------------------------------------------------------------------------

8- Con el comando python manage.py runserver se ejecuta la página creada, en la cual se puede Acceder al Home y About; donde hay información sobre la finalidad del proyecto e información sobre mí (LuzTappero), así también; se pueden ver blogs creados por todos los usuarios.
Por otra parte, se puede realizar un registro y login de usuarios; para poder tener acceso a Crear Blogs, interaccionar con otros blogs creando comentarios, general un perfil donde se agrega información sobre el mismo, avatares y link que lleven a una red social u otro link de interes.

----------------------------------------------------------------------------------------------------------
