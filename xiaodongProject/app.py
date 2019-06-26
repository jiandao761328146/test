from flask import Flask


def create_application() -> (Flask):
    """
    #     创建应用实例
    #     Returns:
    #         Flask: 一个Flask应用的实例
    #     """

    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False

    from webapi import home_api
    app.register_blueprint(home_api)

    return app


app = create_application()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", post=8000)
