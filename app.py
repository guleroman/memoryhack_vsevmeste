import flask
from flask import render_template, request, send_file, jsonify, make_response, json,redirect
from functions import generationPage
app = flask.Flask(__name__)

@app.route("/<name_page>/",methods=['POST','OPTIONS','GET'])
#@cross_origin(origins="*", methods=['POST','OPTIONS','GET'], allow_headers="*")
# @flask_login.login_required
def getDocuments(name_page):
    return render_template(f'{name_page}.html')

@app.route("/api/v1/generatepage/",methods=['POST','OPTIONS'])
def generatePage():
    try:
        Name = json.loads(request.data.decode('utf-8'))['name']
        Foto = json.loads(request.data.decode('utf-8'))['foto']
    except:
        return make_response(jsonify({"_status_code":422,"error":{"info":"incorrect POST-request"}}),422)

    try:
        Date_1 = json.loads(request.data.decode('utf-8'))['date_1']
    except:
        Date_1 = "..."

    try:
        Date_2 = json.loads(request.data.decode('utf-8'))['date_2']
    except:
        Date_2 = "..."

    try:
        City = json.loads(request.data.decode('utf-8'))['city']
    except:
        City = "..."
    
    try:
        Units = json.loads(request.data.decode('utf-8'))['units']
    except:
        Units = "..."

    try:
        Description = json.loads(request.data.decode('utf-8'))['description']
    except:
        Description = ""

    all_entity = {
        "Name":Name,
        "Foto":Foto,
        "Date_1":Date_1,
        "Date_2":Date_2,
        "City":City,
        "Units":Units,
        "Description":Description
    }
    answer = generationPage(all_entity)
    if answer['status_code'] != 200:
        # logger.error({"error": "Twits not found"})
        return make_response(jsonify({"_status_code":404,"error":"Bad"}),404)
    else:
        return make_response(jsonify({"status_code":200,"url":f"http://194.67.91.175/{answer['key']}/"}),200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80,debug=True)
