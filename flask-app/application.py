from flask import Flask
app = Flask(__name__)

##region routing
@app.route('/')
def index():
  return '122 flaask appp'
##endregion routing

if __name__ == "__main__":
  app.run()
