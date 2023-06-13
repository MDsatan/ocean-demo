from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
@app.route('/')
def index():
    print('Request for index page received')
    return render_template('index.html')



# #add debug
# if __name__ == '__main__':
#     app.run(debug=True)
    