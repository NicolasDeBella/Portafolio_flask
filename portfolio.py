from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for
)
from app.confiDB import connectionDB

bp = Blueprint("portfolio", __name__, url_prefix="/")

@bp.route("/",methods=["GET"])
def index():
    return render_template("portfolio/index.html")

@bp.route("/mail",methods=["GET","POST"])
def mail(): 
    if request.method == "POST":
        name = request.form.get("username")
        correo = request.form.get("email")
        message = request.form.get("message")
        mydb = connectionDB()
        if mydb:
            cursor = mydb.cursor()
            sql = "INSERT INTO formulario (username, email, message) VALUES (%s, %s, %s)"
            val = (name, correo, message)
            cursor.execute(sql, val)
            mydb.commit()
            cursor.close()
            mydb.close()
            return render_template("portfolio/sent_mail.html")
        else:
            return print("Error en la conexión a la base de datos")
    else:
        return redirect(url_for('portfolio.index'))




