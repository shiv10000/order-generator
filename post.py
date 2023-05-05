from flask import Flask, request,abort

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
 if request.method=="POST":
    print(request.data)
    return "sucess",200
 else:
    abort(400)
     

if __name__ == '__main__':
    app.run(debug=True)
