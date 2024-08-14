# inicio del diccionario

import tkinter as tk#se ingresa la biblioteca
from tkinter import messagebox

# Diccionario de palabras y significados
diccionario = {
    
    "python": "lenguaje de programación",
    "tkinter": "biblioteca de interfaz gráfica",
    "Red Lan" :" red de área local o LAN es una red de computadoras que permite la comunicación y el intercambio de datos entre diferentes dispositivos a nivel local, ya que está limitada a distancias cortas",
    "ALGORITMO" : " Conjunto de pasos para una determinada tarea",
    "CODIGO": "conjunto de palabras o simbolos que contienen instrucciones para la computadora",
    "c#": "lenguaje de programacion orientado a objetos desarrollados por microsoft y que forma parte de la plataforma",
   "LINUX": "sistema operativo gratuito para computadoras personales derivado de Unix.",
    "JAVA" : "va es un lenguaje de programación multiplataforma orientado a objetos que se ejecuta en miles de millones de dispositivos de todo el mundo. ",
    "HTML" : "Se utiliza en documentos y en el mantenimiento de sitios web. En esencia, es un lenguaje de marcado que permite dar formato a la apariencia de la información en un sitio web.",
    "JAVASCRIPT" : "JavaScript, que se utiliza en desarrollo web, desarrollo de videojuegos, aplicaciones móviles y construcción de servidores web, sigue siendo entonces el lenguaje de programación más utilizado en la actualidad, en todo el mundo.",
    "NoSQL" : "Si bien no es un lenguaje de programación, NoSQL se refiere a una amplia clase de sistemas de gestión de bases de datos que se diferencian de los modelos relacionales tradicionales.",
    "Rust" : "Rust es un lenguaje de programación compilado, de propósito general y multiparadigma, desarrollado por la Fundación Mozilla. ",
    "APLICACIÓN WEB": "Programa que se ejecuta en un servidor web y se accede a través de un navegador",
    "ARQUITECTURA DE SOFTWARE": "Diseño y estructura de un sistema de software",
    "BASE DE DATOS": "Colección de datos organizados para facilitar su acceso y manipulación",
    "BÚSQUEDA DE DATOS": "Proceso de encontrar y recuperar información en una base de datos",
    "CLOUD COMPUTING": "Modelo de entrega de servicios de computación a través de Internet",
    "COMPUTACIÓN EN LA NUBE": "Modelo de entrega de servicios de computación a través de Internet",
    "virtualizacion" : "La virtualización es una tecnología que se puede usar para crear representaciones virtuales de servidores, almacenamiento, redes y otras máquinas físicas. ",
    "DESARROLLO WEB" : "Creación de sitios web y aplicaciones web",
    "DISEÑO DE INTERFAZ": "Creación de interfaces de usuario para sistemas de software",
    "DISEÑO DE SOFTWARE": "Proceso de crear y mejorar la estructura y el funcionamiento de un sistema de software",
    "CSS": "Lenguaje de hoja de estilos en cascada, utilizado para dar formato a documentos HTML",  
    "VIRTUAL BOX" : "Oracle VM VirtualBox es un software de virtualización para arquitecturas x86/amd64. Actualmente es desarrollado por Oracle Corporation como parte de su familia de productos de virtualización.",
    "VPS" : "Un servidor virtual privado, término que proviene del inglés virtual private server, es un sistema de alojamiento web. Su uso es cada vez más popular y, debido a su estructura de funcionamiento, es un servicio IaaS",
    "VPN" : "Una VPN o red privada virtual crea una conexión de red privada entre dispositivos a través de Internet",
    "CABLE COAXIAL " : " es el tipo de cable usado por las compañías de televisión por cable para establecer la conexión entre la central emisora y el usuario.",
    "REBOOT":"rebutear.",
    "SERVER": "servidor.",
    "VIRUS": "pequeño programa que infecta una computadora; puede causar efectos indeseables y hasta daños irreparables.",
    "ZIP": "formato de los archivos comprimidos."
   "UNIX" "sistema operativo multiusuario, fue muy importante en el desarrollo de Internet",
   "SOSTWARE": "término general que designa los diversos tipos de programas usados en computación",
   "TCP/IP": "Transfer Control Protocol / Internet Protocol. Es el protocolo que se utiliza en Internet.",
   "ROUTER" : "ruteador Sistema constituido por hardware y software para la transmisión de datos en Internet."
   "PUERTO SERIAL" "conexión por medio de la cual se envían datos a través de un solo conducto Por ejemplo, el mouse se conecta a un puerto serial.",
   "PROTOCOLO": "lenguaje que utilizan dos computadoras para comunicarse entre sí",
   "PROCESADOR": "conjunto de circuitos lógicos que procesa las instrucciones básicas de una computadora",
   "ONLINE": "en línea, conectado. Estado en que se encuentra una computadora cuando se conecta directamente con la red a través de un dispositivo",
   "NANOSEGUNDO": "una milmillonésima de segundo. Es una medida común del tiempo de acceso a la memoria RAM.",
   "NAVEGADOR": "programa para recorrer la World Wide Web. Algunos de los más conocidos son Netscape Navigator, Microsoft Explorer, Opera y Neoplanet.",
   "MODEM": "modulador-demodulador. Dispositivo periférico que conecta la computadora a la línea telefónica.",
   "MEMORIA CACHE": "pequeña cantidad de memoria de alta velocidad que incrementa el rendimiento de la computadora almacenando datos temporariamente.",
   "LATECIA": "lapso necesario para que un paquete de información viaje desde la fuente hasta su destino. La latencia y el ancho de banda, juntos, definen la capacidad y la velocidad de una red.",
   "LAN MANAGER": "sistema operativo de red",
   "IP":"Protocolo de Internet.",
   "ISP": "Internet ServiceProvider. Proveedor de servicios de Internet.",
   "HARD DISK": "disco rígido",
   "FIBRA OPTICA": "tecnología para transmitir información como pulsos luminosos a través de un conducto de fibra de vidrio.",
    "EMULACION":"emulation. Proceso de compatibilización entre computadoras mediante un software",
    "DOWNLOAD": "descargar, bajar. Transferencia de información desde Internet a una computadora.",
   "DATA": "datos información.",
   "COOKIE": "pequeño archivo de texto que un sitio web coloca en el disco rígido de una computadora que lo visita.",
   "BASE DE DATOS": "conjunto de datos organizados de modo tal que resulte fácil acceder a ellos gestionarlos y actualizarlos",
   "AUTOCAD": "programa de dibujo técnico.",
   "ANTIVIRUS": "programa que busca y eventualmente elimina los virus informáticos que pueden haber infectado un disco rígido o disquete.",
   "ANCHO DE BANDA" : "expresa la cantidad de datos que pueden ser transmitidos en determinado lapso En las redes se expresa en bps.",
   "ACCESO DIRECTO": "es un ícono que permite abrir más fácilmente un determinado programa o archivo.",
   "Hosting": "alojamiento. Servicio ofrecido por algunos proveedores, que brindan a sus clientes ",
   "HARWARE": "todos los componentes físicos de la computadora y sus periféricos",
   "Firewall": "mecanismo de seguridad que impide el acceso a una red.",
    "Ethernet": "tecnología para red de área local. Fue desarrollada originalmente por Xerox y posteriormente por Xerox, DEC e Intel. Ha sido aceptada como estándar por la ",
    "HTTP": "Hypertext Transfer Protocol Protocolo de transferencia de hipertextos Es un protocolo que permite transferir información en archivos de texto gráficos de video de audio y otros recursos multimedia.",
   "Jpg": "extensión de ciertos archivos gráficos. Véase JPEG.",
   "USB": "es una interfase de tipo plug  play entre una computadora y ciertos dispositivos por ejemplo teclados teléfonos escáneres e impresoras.",
   "Troyano" : "programa que contiene un código dañino dentro de datos aparentemente inofensivos.",
   "Toolbar": "barra de herramientas.",
   "Screen": "pantalla.", 
   
     
   #
}

diccionario = {k.lower(): v for k, v in diccionario.items()} #una función de cadena en Python que convierte todos los caracteres de una cadena a minúsculas.
"""
Convierte todas las claves del diccionario a minúsculas.

Esto se hace para que en la búsqueda no interfiera si es mayuscula o minuscula y permita acceder a la palabra (no distingue entre mayúsculas y minúsculas).
"""
root = tk.Tk()
root.title("Diccionario")
root.geometry("300x200")#Establece el tamaño de la ventana 

""" TK ES LA RAIZ DE TKINTER Y ES LA QUE NOS PERMITE ACCEDER"""
menu = tk.Menu(root)#se crean las variables para cada una de las pestñas usando la variable tk que llama a la binblioteca y permite acceder a ella
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_command(label="eddi el inge")

file_menu = tk.Menu(menu)
menu.add_command(label="Acerca de", command=lambda: Acerca_de ())


file_menu = tk.Menu(menu)
menu.add_cascade(label="opciones", menu=file_menu)
file_menu.add_command(label="salir", command=root.quit)

search_menu = tk.Menu(menu)
menu.add_cascade(label="Buscar", menu=search_menu)


search_entry = tk.Entry(root, width=20)
search_entry.pack(pady=10)


buscador = tk.Button(root, text="Buscar")
buscador.pack(pady=10)


resultado_text = tk.Text(root, width=35, height=10)
resultado_text.pack(pady=15)


def buscar_palabra():
    """
    Busca el significado de una palabra en el diccionario.

    Obtiene el texto ingresado en la entrada de búsqueda, lo convierte a minúsculas y busca su significado en el diccionario.
    Si la palabra existe, muestra su significado en el área de texto. Si no existe, muestra "No encontrado".
    """
    palabra = search_entry.get().lower()
    significado = diccionario.get(palabra, "No encontrado")
    resultado_text.delete(1.0, tk.END)
    resultado_text.insert(tk.END, f"Significado: {significado}")

buscador.config(command=buscar_palabra)#se crea la variable 
def Acerca_de():
    """se crea la funcion de acerca de donde muestra informacion sobre el diccionario porquien fue creado se llama a la variable acerca de donde cada 
    que se presione el boton salga una pantalla emergente y aparezca la funcion
    """
    messagebox.showinfo("Acerca de", "Diccionario creado por Junior  Chan")
    
    messagebox.showinfo("Acerca de","En este diccionario se encuentran las palabras y el significado de las plas palabras mas comunes en la informatica cuenta con mas de 70 palabras de la informatica")


root.mainloop()# reinicio de menu