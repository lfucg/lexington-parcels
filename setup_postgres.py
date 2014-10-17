from collections import OrderedDict
import os

from postgres import Postgres

db = Postgres(os.environ.get('DATABASE_URL'))

columns = OrderedDict()
columns['x'] = 'float8'
columns['y'] = 'float8'
columns['address'] = 'varchar(255)'
columns['parcel_id'] = 'int'

columns_sql = ['%s %s' % (key, value) for key, value in columns.items()]
create_table_sql = 'CREATE TABLE parcels(%s)' % ', '.join(columns_sql)
db.run('DROP TABLE IF EXISTS parcels')
db.run(create_table_sql)
