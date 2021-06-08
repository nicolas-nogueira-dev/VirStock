from flask import *
from checkLogin import *
from fileCore import *
from utilities import *
from os.path import join
import time

envSettings = getEnvVar()
app = Flask(__name__)
app.secret_key = bytes(envSettings["secret_key"], 'utf-8')
folderPath = envSettings["folderPath"]
app.config['UPLOAD_FOLDER'] = envSettings["folderPath"]

def saveLogs(ip, user, fileName, localTime, logsPath):
    rawtext = str(ip) + "|" + str(user) + "|" + str(fileName) + "|" + str(localTime) + "\n"
    logsPath = "logs/" + str(logsPath)
    with open(logsPath, "a") as logs:
        logs.write(rawtext)

@app.route("/")
def home():
    if "name" in session:
        files = getFilespath(folderPath)
        return render_template("home_login.html", files=files, formateSize=formateSize)
    return render_template("home_logoff.html")

@app.route("/download/<filePath>")
def downloadFile(filePath):
    if "name" in session:
        ip = str(request.remote_addr)
        user = session["name"]
        fileName = filePath
        downloadTime = time.ctime()
        saveLogs(ip, user, fileName, downloadTime, "download.txt")
        path = folderPath + "/" + filePath
        return send_file(path, as_attachment=True)
    return redirect("/")

@app.route("/upload", methods=["GET","POST"])
def uploadFile():
    if "name" in session:
        if request.method == "POST":
            file = request.files["file"]
            ip = str(request.remote_addr)
            user = session["name"]
            fileName = file.filename
            downloadTime = time.ctime()
            saveLogs(ip, user, fileName, downloadTime, "upload.txt")
            saveFile(app, file, file.filename)
            return redirect("/")
        return render_template("sendFile.html")
    return redirect("/")

@app.route("/login", methods=['POST'])
def login():
    if not "name" in session:
        name = request.form["name"]
        password = request.form["password"]
        if checkPassword(name,password):
            session.permanent = False
            session["name"] = name
            return redirect("/")
        else:
            return redirect("/")
    return redirect("/")

@app.route("/logout")
def logout():
    if "name" in session:
        del session["name"]
        return redirect("/")
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
