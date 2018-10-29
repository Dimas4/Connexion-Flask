import connexion
import pathlib


def create():
    path = pathlib.Path(__file__).parent.parent.parent / 'swagger'
    app = connexion.FlaskApp(__name__, port=8000, specification_dir=str(path))
    app.add_api('api.yaml', arguments={'title': 'Hello World Example'})
    return app
