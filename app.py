import os
from flask import Flask, render_template, jsonify, request, Response
import psycopg2
import psycopg2.extras
import re

app = Flask(__name__)

url = os.environ.get('DATABASE_URL')
conn = psycopg2.connect(url, cursor_factory=psycopg2.extras.DictCursor)
cur = conn.cursor()


@app.route('/parcel')
def parcel():
    query = request.args['parcel_id']

    if re.search('^\d+$', query):
        cur.execute('select * from parcels where parcel_id = (%s)', (query,))
    else:
        return ''

    if cur.rowcount:
        return jsonify(cur.fetchone())
    else:
        return ''

if __name__ == ('__main__'):
  app.run(debug=True)
