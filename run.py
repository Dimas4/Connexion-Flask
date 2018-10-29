from utils.create_app.create import create as create_app


if __name__ == '__main__':
    app = create_app()
    app.run(port=8000)
