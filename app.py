from flask import Flask

from v1.routes import api as api_v1
from v1_1.routes import api as api_v1_1
from v2.routes import api as api_v2

app = Flask(__name__)

app.register_blueprint(api_v1, name="v1", url_prefix="/v1")
app.register_blueprint(api_v1_1, name="v1.1", url_prefix="/v1.1")
app.register_blueprint(api_v2, name="v2", url_prefix="/v2")

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)