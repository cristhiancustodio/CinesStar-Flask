from flask import Blueprint, render_template, jsonify, request, url_for

#from ControllerBase import ControllerBase

api_blue = Blueprint('api', __name__,template_folder='Controller', url_prefix='/api')

class API:

    def __init__(self):
        pass
    def listaPalabrasClaves() ->dict:
        lista = {
            "precio" : "Para consultar el precio debes de acercarte a nuestra caja",
            "pago" : "Puedes pagar con efectivo, yape o tranferencia",
            "atencion" : "Atendemos de 8 am a 10 pm de L a V",
            "horario" : "Atendemos de 8 am a 10 pm de L a V",
            "compra" : "Las compras los puedes hacer por internet",
            "contacto" : "Para comunicarte con nuestros clientes por favor llamar a 9462655",
            "correo" : "Nuestro correo es cryisthian_06@hotmail.com",
            "gracias" : "Gracias a ti, espero que vuelvas pronto",
            "hola" : "Hola en que puedo ayudarte!",

        }
        return lista
    
    #def listarRutas(self):
    @api_blue.route("/lista-palabras")
    def lista_palabras():
        return "comentario de computadora"
        return API.listaPalabrasClaves()
    
    @api_blue.route("/API/", methods=['POST'])
    def chat():
        # Obtener todos los parámetros de formulario
        form = request.form.to_dict()

        return API.procesarRespuesta(form.get("pregunta") or 'No encontrado')

    def procesarRespuesta(pregunta : str):
        tokens = pregunta.split()
        palabras = API.listaPalabrasClaves()
        
        
        
        claves = list(palabras.keys())
        for letras in tokens:
            if letras in claves:
                return palabras.get(letras)
        return 'No pudimos procesar tu pregunta'
        
