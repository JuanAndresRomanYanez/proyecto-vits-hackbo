from bottle import get, post, request, run, route, redirect, template, response, static_file
import os


Administrador = {'id':[1], 'nom':['Juan Andres'], 'app':['Roman'], 'apm':['Yañez'], 'usu':['adm'], 'contra':['adm'], 'img':[]}

Profesor = {'id':[1], 'nom':['Brayan'], 'app':['Torrez'], 'apm':['Navia'], 'materia':['Fisica-Quimica'], 'usu':['Enigma'], 'contra':['Enigma_eaw'], 'img':[]}

Padre = {'id':[1], 'nom':['Angel'], 'app':['Vargas'], 'apm':['Landivar'], 'usu':['pad'], 'contra':['pad'], 'img':[]}

Estudiante  = {'id':[1], 'nom':['Alexis'], 'app':['Lozano'], 'apm':['Teran'], 'curso':['1°'], 'paralelo':['B'], 'nompm':['Hugo'], 'appmp':['Lozano'], 'apmmp':['Barba'], 'usupm':['hlozano'], 'contramp':['hl123']}

def nwId():
    mayor = -1
    for x in datos['id']:
        if x > mayor:
            mayor = x
    mayor += 1
    return mayor

@route('/')
def inicio():
    return template('Index')

@route('/archivoimg/<nombrearchivo>')
def servirarchivos(nombrearchivo):
    app = os.getcwd()  # get current Windows Directory
    return static_file(nombrearchivo, root=app + "/IMAGENES")

@route('/archivocss/<nombrearchivo>')
def servirarchivos(nombrearchivo):
    app = os.getcwd()  # get current Windows Directory
    return static_file(nombrearchivo, root=app + "/CSS")

@route('/archivocssform/<nombrearchivo>')
def servirarchivos(nombrearchivo):
    app = os.getcwd()  # get current Windows Directory
    return static_file(nombrearchivo, root=app + "/CSS")

@route('/archivocssmenu/<nombrearchivo>')
def servirarchivos(nombrearchivo):
    app = os.getcwd()  # get current Windows Directory
    return static_file(nombrearchivo, root=app + "/CSS")

@route('/Iniciar')
def Login():
      return template('LOGIN')

@route('/login', method='post')
def Ingresar_Sistema():
      login = request.forms.get('log')
      password = request.forms.get('pas')
      selection = request.forms.get('select')
      if login in Administrador['usu'] and selection == '2':
              pos = Administrador['usu'].index(login)
              if password == Administrador['contra'][pos]:
                  # return "ingresaste " + usr['nom'][pos]
                  response.set_cookie("id", str(Administrador['id'][pos]))
                  return template('ADMINISTRADOR')

      elif login in Profesor['usu'] and selection == '3':
              pos = Profesor['usu'].index(login)
              if password == Profesor['contra'][pos]:
                  # return "ingresaste " + usr['nom'][pos]
                  response.set_cookie("id", str(Profesor['id'][pos]))
                  return template('PROFESOR')

      elif login in Padre['usu'] and selection == '4':
              pos = Padre['usu'].index(login)
              if password == Padre['contra'][pos]:
                  # return "ingresaste " + usr['nom'][pos]
                  response.set_cookie("id", str(Padre['id'][pos]))
                  return template('PADRES')

      print (selection)
      return redirect('/')

@route('/logout')
def salir():
    response.set_cookie("id", "-1")
    return redirect('/')


run(host='0.0.0.0', port = 8003)
