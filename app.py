from flask import Flask

app = Flask(__name__)
#app = Flask(__name__) # Create a Flask WSGI application, an instance of the Flask class.

@app.route('/')
def hello_world():
  return 'Hello World'
  #return 'Hello World!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  #app.run(host='0.0.0.0', debug=True)
