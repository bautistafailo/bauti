Mi Proyecto Django
Este es un proyecto Django que incluye una aplicación web llamada "SanLuis". La aplicación proporciona información sobre servicios y permite a los usuarios realizar pedidos.

Requisitos
Python 3.x
Django 3.x

Base de datos
Este proyecto utiliza una base de datos SQLite por defecto.

Funcionalidades:

Modalidades: Muestra las diferentes modalidades de servicios disponibles.

Servicios: Permite buscar servicios por nombre.

Contacto: Proporciona un formulario para ponerse en contacto. (El msimo es una simulacion, ya que agregar el codigo que hacia que los mismos comentarios lleguen a mi mail escapaba de mis conocimietos).

Inscribirme: Permite registrar nuevos clientes.

Pago: Permite dejar constancia de un pago.

Nosotros: Brinda informacion especifica acerca de: La web, la institucion y mi persona. (ademas pone en practica el uso de un boton que nos permita saber mas sobre algo en especifico, en este caso, saber mas sobre la institucion).

Editar Perfil: Permite cambiar contraseña, nombre de usuario y avatar.

ModalidadList: Esta vista muestra una lista de modalidades en la página. Utiliza la plantilla modalidad_lista.html para renderizar la lista de modalidades y mostrarlas al usuario.

ModalidadDetalle: Esta vista muestra los detalles de una modalidad específica. Utiliza la plantilla detail.html para renderizar la información de la modalidad y mostrarla al usuario.

ModalidadCreacion: Esta vista muestra un formulario para que el usuario pueda crear una nueva modalidad. El usuario puede ingresar los datos requeridos, como el título, subtítulo, contenido, autor, fecha e imagen de la modalidad. Después de enviar el formulario, se crea la modalidad y se redirige al usuario a la lista de modalidades.

ModalidadUpdate: Esta vista muestra un formulario para que el usuario pueda actualizar una modalidad existente. El usuario puede editar los campos de la modalidad, como el título, subtítulo, contenido, autor, fecha e imagen. Después de enviar el formulario de actualización, se guardan los cambios y se redirige al usuario a la lista de modalidades.

ModalidadDelete: Esta vista muestra una confirmación para que el usuario pueda eliminar una modalidad. Si el usuario confirma la eliminación, se elimina la modalidad de la base de datos y se redirige al usuario a la lista de modalidades.

Log In y Log out:  Permite a los usuarios iniciar sesión y cerrar sesión en la aplicación.



Contribuciones
Las contribuciones son bienvenidas. Si encuentras algún problema o quieres agregar nuevas características, no lo dudes.


Nombre: Juan Bautista Failo
