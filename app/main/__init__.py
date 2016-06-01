from flask import Blueprint

main = Blueprint('main',__name__)

from . import sun, upload, command, index, form_zc

