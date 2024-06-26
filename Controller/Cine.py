
from Models.cineModels import cineModels as CineModel

from flask import Blueprint, render_template

#from ControllerBase import ControllerBase

cine_blue = Blueprint('cine', __name__,template_folder='Controller', url_prefix='/')

cine_model = CineModel()

          
@cine_blue.route("/cine/<int:id_cinema>")
def cine(id_cinema):
    cinema = cine_model.view_cine(id_cinema)
    tarifa = cine_model.get_cineTarifas(id_cinema)
    cinema_film = cine_model.get_cinePeliculas(id_cinema)
    return render_template("cine.html", cinema = dict(cinema),tarifa = dict(tarifa), cinema_film = dict(cinema_film))

@cine_blue.route("/cines")
def cines():
    cinema = cine_model.get_cines()
    return render_template("cines.html", cinema = cinema)

  