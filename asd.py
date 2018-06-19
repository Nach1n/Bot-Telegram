import telebot
import MySQLdb
import random 
from telebot import types
"""from telegram.ext import *"""
#https://geopet.ga/phpmyadmin/
bot = telebot.TeleBot("615474990:AAHf8YDN5IwslwUx0ZYGHWXaV2NTAlX8aZg")

conn = MySQLdb.connect (host = "138.197.200.124", user = "root", passwd = "$%880unab.toor880A", db = "geopet")
cur = conn.cursor()
car = conn.cursor()
cir = conn.cursor()
#cur.execute("SELECT * FROM users")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        print(message)
        chatid = message.chat.id
        nombreUsuario = str(message.chat.first_name) + " " + str(message.chat.last_name)
        lista_direcciones = ['Antonio Varas, Providencia','Pasaje Tabancura, Maipu','EL apero, PuenteAlto','Cuatro norte, Peñalolen']
        random.shuffle(lista_direcciones)

        saludo = "Hola {nombre}, Bienvenido al bot de Geopet si eres nuestro cliente porfavor ingresa el comando /client si eres administrador porfavor ingresa /admin, para ver la localizacion de tu mascota utiliza el comando /location"
        bot.send_message(chatid, saludo.format(nombre = nombreUsuario))


@bot.message_handler(commands=['client'])
def enviarOpciones_cliente(message):
        chatid = message.chat.id
        lista = []
        markup = types.ReplyKeyboardMarkup(row_width=2)

        itembtn2 = types.KeyboardButton('Mis mascotas')
        itembtn4 = types.KeyboardButton('Iniciar sesion')

        markup.add(itembtn2, itembtn4)
        bot.send_message(chatid, "Elige una opcion:", reply_markup=markup)


@bot.message_handler(commands=['admin'])
def enviarOpciones_admin(message):
        chatid = message.chat.id
        lista = []
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('SOS PET')
        itembtn2 = types.KeyboardButton('Mostrar clientes')
        itembtn3 = types.KeyboardButton('Mostrar Dispositivos')
        
        markup.add(itembtn1, itembtn2, itembtn3)
        
        bot.send_message(chatid, "Elige una opcion:", reply_markup=markup)


@bot.message_handler(commands=['location'])
def enviarOpciones_pelao(message):
    cur.execute("SELECT * FROM users")
    car.execute("SELECT * FROM pets")
    chatid = message.chat.id
    user_name = str(message.chat.username)
    markup = types.ReplyKeyboardMarkup(row_width=2)
    lista_pelao = []
    lista_direcciones = ['Antonio Varas, Providencia','Pasaje Tabancura, Maipu','EL apero, PuenteAlto','Cuatro norte, Peñalolen']
    """for row in cur:
                for rop in row:
                        if row[2] == user_name:
                                if rop[10] == row[0]:
                                        lista_pelao.append(rop[2] + "-" +rop[4])"""
    
    itembtn1 = types.KeyboardButton('Mia')
    itembtn2 = types.KeyboardButton('Zack')
    itembtn3 = types.KeyboardButton('Sol')
        
    markup.add(itembtn1,itembtn2,itembtn3)
    bot.send_message(chatid, "Elige una mascota:", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Mis mascotas' and message.content_type == 'text')
def mostrarMascotas(message):

        cur.execute("SELECT * FROM users")
        car.execute("SELECT * FROM pets")
        lista_pets = []
        chatid = message.chat.id
        user_name = str(message.chat.username)

        for row in cur:
                for rop in car:
                        if row[2] == user_name:
                                if rop[10] == row[0]: 
                                        lista_pets.append(rop[2] + "-" +rop[4])
                                        #print(rop)

        bot.send_message(chatid, str(lista_pets))
        

@bot.message_handler(func=lambda message: message.text == 'Iniciar sesion' and message.content_type == 'text')
def mostrarIniciar_sesion(message):

        chatid = message.chat.id
        info = "Ingresa a nuestra aplicacion web para iniciar sesion https://geopet.ga/login"
        bot.send_message(chatid, info)


@bot.message_handler(func=lambda message: message.text == 'SOS PET' and message.content_type == 'text')
def enviarImagen(message):
        cur.execute("SELECT * FROM users")
        chatid = message.chat.id
        user_name = str(message.chat.username)
        mensaje_perdida = "Mascota perdida"
        for row in cur:
                if row[2] == user_name:
                        if row[8] == 1:
                                sti = open('perros.jpg', 'rb')
                                bot.send_sticker(chatid, sti)
                                bot.send_message(chatid, mensaje_perdida)
                                #bot.send_sticker(chatid, "FILEID")
                        else:
                                salu3 = "No eres un administrador"
                                bot.send_message(chatid, salu3)
                                

@bot.message_handler(func=lambda message: message.text == 'Mostrar clientes' and message.content_type == 'text')
def mostrarClientes(message):
        cur.execute("SELECT * FROM users")
        

        chatid = message.chat.id
        lista = []
        user_name = str(message.chat.username)
        for row in cur:
                if row[8] == 2:
                        #for row in cur:
                #if row[2] == user_name:
                        #if row[8] == 2:
                        lista.append(row[3] + "" + row[4])
                                #print(row)
        bot.send_message(chatid, str(lista))

        
@bot.message_handler(func=lambda message: message.text == 'Mostrar Dispositivos' and message.content_type == 'text')
def enviarImagen(message):
        cur.execute("SELECT * FROM users")
        cir.execute("SELECT * FROM products")
        chatid = message.chat.id
        user_name = str(message.chat.username)
        lista_dispositivos = []
        for row in cur:
                for rop in cir:
                        if row[2] == user_name and row[8] == 1: 
                                lista_dispositivos.append(rop[2] + "-" + rop[3])
                        """else:
                                salu3 = "No eres un administrador"
                                bot.send_message(chatid, salu3)"""
                                                 
        bot.send_message(chatid, str(lista_dispositivos))


@bot.message_handler(func=lambda message: message.text == 'Mia' and message.content_type == 'text')
def enviarImagen(message):
        cur.execute("SELECT * FROM users")
        lista_direcciones = ['Antonio Varas, Providencia','Pasaje Tabancura, Maipu','EL apero, PuenteAlto','Cuatro norte, Peñalolen']
        chatid = message.chat.id
        lista_one = []
        mensaje = "Su mascota se encuentra en: " + random.choice(lista_direcciones)
        bot.send_message(chatid, mensaje)
        

@bot.message_handler(func=lambda message: message.text == 'Zack' and message.content_type == 'text')
def enviarImagen(message):
        cur.execute("SELECT * FROM users")
        lista_direcciones = ['Antonio Varas, Providencia','Pasaje Tabancura, Maipu','EL apero, PuenteAlto','Cuatro norte, Peñalolen']
        chatid = message.chat.id
        lista_one = []
        mensaje = "Su mascota se encuentra en: " + random.choice(lista_direcciones)
        
        bot.send_message(chatid, mensaje)

@bot.message_handler(func=lambda message: message.text == 'Sol' and message.content_type == 'text')
def enviarImagen(message):
        cur.execute("SELECT * FROM users")
        lista_direcciones = ['Antonio Varas, Providencia','Pasaje Tabancura, Maipu','EL apero, PuenteAlto','Cuatro norte, Peñalolen']
        chatid = message.chat.id
        lista_one = []
        mensaje = "Su mascota se encuentra en: " + random.choice(lista_direcciones)
        bot.send_message(chatid, mensaje)

        
#Validacion Mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        chatid = message.chat.id
        bot.send_message(chatid,"No existe este comando solo existen /start y /help")
    
   
print("El bot se esta ejecutando")
bot.polling()
cir.close()
cur.close()
car.close()
conn.close()


