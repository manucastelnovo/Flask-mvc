from controllers.user_controller import login
from flask import Blueprint

blueprint= Blueprint('blueprint', __name__)


blueprint.route('/login', methods=['GET', 'POST'])(login)


