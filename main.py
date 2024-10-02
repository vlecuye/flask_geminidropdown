# Required Imports
import os
from flask import Flask, request, jsonify,render_template
from google.cloud import firestore
import json
# Initialize Flask App
app = Flask(__name__)
db = firestore.Client(project="pc-smart-persona")

@app.route('/', methods=['GET','POST'])
def main():
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents
    """
    db_ref = db.collection('personas')
    docs = db_ref.stream()
    personas = []
    for doc in docs :
        personas.append(doc.to_dict())
    if request.method == "POST":
        print(request.form.get('personas'))
        persona = personas[int(request.form.get('personas')) - 1]
    else:
        persona = personas[0]
    return render_template('persona.html', personas=personas,persona=persona)

port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=port)