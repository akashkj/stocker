from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from service.data_util import get_stock_info
import json
from nsetools import Nse

import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks2.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Stock(db.Model):
   id = db.Column(db.Integer, primary_key=True, autoincrement=True)
   name = db.Column(db.String(75))
   symbol = db.Column(db.String(20), unique=True)
   sector = db.Column(db.String(75))
   industry = db.Column(db.String(100)) 
   

   def __init__(self, name, symbol, sector, industry):
      self.name = name
      self.symbol = symbol
      self.sector = sector
      self.industry = industry

@app.route('/')
def show_all():
   #data = Stock.query.all()
   #print("7777777777777 - {}".format(data))
   #return render_template('chart.html', stocks = Stock.query.all() )
   return ""

@app.route("/stocks")
def all_stocks():
   nse = Nse()
   return json.dumps(nse.get_stock_codes())


@app.route('/new', methods = ['GET', 'POST'])
def new():
   return "NI"
   # if request.method == 'POST':
   #    if not request.form['name'] or not request.form['city'] or not request.form['addr']:
   #       flash('Please enter all the fields', 'error')
   #    else:
   #       student = students(request.form['name'], request.form['city'],
   #          request.form['addr'], request.form['pin'])
         
   #       db.session.add(student)
   #       db.session.commit()
   #       flash('Record was successfully added')
   #       return redirect(url_for('show_all'))
   # return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   symbols = ["PIDILITIND.NS", "RELIANCE.NS", "ASTRAL.NS", "BRITANNIA.NS"]
   #symbols = []
   for symbol in symbols:
      logging.info("symbol {}".format(symbol))
      #existing_data = Stock.query.filter(Stock.symbol == symbol)
      existing_data = True
      if not existing_data:
         data = get_stock_info(symbol)
         db.session.add(Stock(data.get("longName"), symbol, data.get("sector"), data.get("industry")))
         db.session.commit()
   app.run(debug = True)
   