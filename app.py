from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/scan?pwd')
def scan(pwd):
      if pwd =="iqbal": 
         return render_template('scan.html')
      else:
         return render_template('index.html')
      
@app.route('/cover')
def cover():
   return render_template('cover.html')


if __name__ == '__main__':
   app.run()
