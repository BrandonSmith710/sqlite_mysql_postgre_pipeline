import psycopg2
import mysql.connector
from sqlite_to_mysql import connect_mysql, get_curs

DB_NAME = '********'
USER = '********'
PASSWD = '********************************'
HOST = '****************************'

def connect_pg(dbname, user, password, host):
	return psycopg2.connect(dbname = dbname, user = user,
		                    password = password, host = host)

def create_pg_armory_item():
	pg_curs.execute('''CREATE TABLE IF NOT EXISTS armory_item (
		  			   item_id SERIAL PRIMARY KEY,
					   name VARCHAR(255) NOT NULL,
					   value INT NOT NULL,
					   weight INT NOT NULL);''')
	pg_conn.commit()

def create_pg_armory_weapon():
	pg_curs.execute('''CREATE TABLE IF NOT EXISTS armory_weapon (
		  			   item_ptr_id SERIAL PRIMARY KEY,
					   power INT NOT NULL);''')
	pg_conn.commit()

def create_pg_character():
	pg_curs.execute('''CREATE TABLE IF NOT EXISTS character (
		  			   character_id SERIAL PRIMARY KEY,
					   name VARCHAR(255) NOT NULL,
					   level INT NOT NULL,
					   exp INT NOT NULL,
					   hp INT NOT NULL,
					   strength INT NOT NULL,
					   intelligence INT NOT NULL,
					   dexterity INT NOT NULL);''')
	pg_conn.commit()

def create_pg_character_inv():
	pg_curs.execute('''CREATE TABLE IF NOT EXISTS character_inv (
					   id SERIAL PRIMARY KEY,
		  			   character_id INT NOT NULL,
					   item_id INT NOT NULL);''')
	pg_conn.commit()

def create_pg_cleric():
	pg_curs.execute('''CREATE TABLE IF NOT EXISTS cleric (
		               character_ptr_id SERIAL PRIMARY KEY,
		               using_shield BOOL NOT NULL,
		               mana INT NOT NULL);''')
	pg_conn.commit()

def create_pg_mage():
	pg_curs.execute('''CREATE TABLE IF NOT EXISTS mage (
		               character_ptr_id SERIAL PRIMARY KEY,
		               has_pet BOOL NOT NULL,
		               mana INT NOT NULL);''')
	pg_conn.commit()

def insert_pg_armory_item(curs, item_id, name, value, weight):
	query = '''INSERT INTO armory_item (item_id, name, value, weight) 
		       VALUES (%s, %s, %s, %s);'''
	values = (item_id, name, value, weight)
	curs.execute(query, values)

def insert_pg_armory_weapon(curs, item_ptr_id, power):
	query = '''INSERT INTO armory_weapon (item_ptr_id, power)
	           VALUES (%s, %s);'''
	values = (item_ptr_id, power)
	curs.execute(query, values)

def insert_pg_character(curs, character_id, name, level, exp, hp, strength,
	                    intelligence, dexterity):
	query = '''INSERT INTO character (character_id, name, level, exp,
	           hp, strength, intelligence, dexterity) VALUES
	           (%s, %s, %s, %s, %s, %s, %s, %s);'''
	values = (character_id, name, level, exp, hp, strength, intelligence,
		      dexterity)
	curs.execute(query, values)

def insert_pg_character_inv(curs, inv_id, character_id, item_id):
	query = '''INSERT INTO character_inv (id, character_id, item_id)
	           VALUES (%s, %s, %s);'''
	values = (inv_id, character_id, item_id)
	curs.execute(query, values)

def insert_pg_cleric(curs, c_id, using_shield, mana):
	query = '''INSERT INTO cleric (character_ptr_id, using_shield, mana)
	           VALUES (%s, %s, %s);'''
	values = (c_id, using_shield, mana)
	curs.execute(query, values)

def insert_pg_mage(curs, c_id, has_pet, mana):
	query = '''INSERT INTO mage (character_ptr_id, has_pet, mana)
	           VALUES (%s, %s, %s);'''
	values = (c_id, has_pet, mana)
	curs.execute(query, values)

def load_pg_armory_item():
	my_curs.execute('SELECT * FROM armory_item;')
	for item_id, name, value, weight in my_curs.fetchall():
		insert_pg_armory_item(pg_curs, item_id, name, value, weight)
	pg_conn.commit()

def load_pg_armory_weapon():
	my_curs.execute('SELECT * FROM `armory_weapon`;')
	for item_ptr_id, power in my_curs.fetchall():
		insert_pg_armory_weapon(pg_curs, item_ptr_id, power)
	pg_conn.commit()

def load_pg_character():
	my_curs.execute('SELECT * FROM `character`;')
	lst = my_curs.fetchall()
	for char_id, name, lvl, exp, hp, strength, intl, dex in lst:
		insert_pg_character(pg_curs, char_id, name, lvl, exp,
			                hp, strength, intl, dex)
	pg_conn.commit()

def load_pg_character_inv():
	my_curs.execute('SELECT * FROM `character_inv`;')
	for inv_id, character_id, item_id in my_curs.fetchall():
		insert_pg_character_inv(pg_curs, inv_id, character_id, item_id)
	pg_conn.commit()

def load_pg_cleric():
	my_curs.execute('SELECT * FROM `cleric`;')
	for c_id, using_shield, mana in my_curs.fetchall():
		insert_pg_cleric(pg_curs, c_id, using_shield, mana)
	pg_conn.commit()

def load_pg_mage():
	my_curs.execute('SELECT * FROM `mage`;')
	for c_id, has_pet, mana in my_curs.fetchall():
		insert_pg_mage(pg_curs, c_id, has_pet, mana)
	pg_conn.commit()

def query_pg_armory_item():
	pg_curs.execute('SELECT * FROM armory_item;')
	res = pg_curs.fetchall()
	return res

def query_pg_armory_weapon():
	pg_curs.execute('SELECT * FROM armory_weapon;')
	res = pg_curs.fetchall()
	return res

def query_pg_character(char_id):
	pg_curs.execute('SELECT hp, strength, intelligence FROM character ' +
		            'WHERE character_id = {};'.format(char_id))
	res = pg_curs.fetchall()
	return res

def query_pg_character_inv():
	pg_curs.execute('SELECT * FROM character_inv;')
	res = pg_curs.fetchall()
	return res

def query_pg_cleric():
	pg_curs.execute('SELECT * FROM cleric;')
	res = pg_curs.fetchall()
	return res

def query_pg_mage():
	pg_curs.execute('SELECT * FROM mage;')
	res = pg_curs.fetchall()
	return res

def query_pg_char_weapon_inv():
	pg_curs.execute('''SELECT * FROM armory_weapon as aw
		               INNER JOIN armory_item as ai ON aw.item_ptr_id = ai.item_id
		               INNER JOIN character_inv as ci ON ci.item_id = ai.item_id
		               GROUP BY ci.character_id;''')
	res = pg_curs.fetchall()
	return res

def pg_gain_hp(char_id, hp_gain):
	q = ('UPDATE character SET hp = hp + {} '.format(hp_gain) + 
		 'WHERE character_id = {}'.format(char_id))
	pg_curs.execute(q)
	pg_conn.commit()
	pg_curs.execute('SELECT * FROM character WHERE character_id = {}'.
		format(char_id))
	res = pg_curs.fetchall()
	return res

def pg_gain_strength(char_id, str_gain):
	q = ('UPDATE character SET strength = strength + {} '.format(str_gain) + 
		 'WHERE character_id = {}'.format(char_id))
	pg_curs.execute(q)
	pg_conn.commit()
	pg_curs.execute('SELECT * FROM character WHERE character_id = {}'.
		format(char_id))
	res = pg_curs.fetchall()
	return res

def pg_gain_intelligence(char_id, int_gain):
	q = ('UPDATE character SET intelligence = intelligence + {} '.format(
		int_gain) + 'WHERE character_id = {}'.format(char_id))
	pg_curs.execute(q)
	pg_conn.commit()
	pg_curs.execute('SELECT * FROM character WHERE character_id = {}'.
		format(char_id))
	res = pg_curs.fetchall()
	return res

def drop_pg_table(table_name):
	pg_curs.execute('DROP TABLE IF EXISTS {}'.format(table_name))
	pg_conn.commit()

my_conn = connect_mysql(host = 'localhost', user = '****',
	                passwd = '***********', database = '*******')
my_curs = get_curs(my_conn)
pg_conn = connect_pg(dbname = DB_NAME, user = USER,
	                 password = PASSWD, host = HOST)
pg_curs = get_curs(pg_conn)
