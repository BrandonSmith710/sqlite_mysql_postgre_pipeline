import mysql.connector
import sqlite3

def connect_mysql(host, user, passwd, database):
	return mysql.connector.connect(
			host = host,
			user = user,
			passwd = passwd,
			database = database)

def connect_sqlite(database):
    return sqlite3.Connection(database)

def get_curs(conn):
    return conn.cursor()

def create_my_armory_item():
    my_curs.execute('''CREATE TABLE IF NOT EXISTS `armory_item` (
		  			   item_id INT PRIMARY KEY,
					   name VARCHAR(255) NOT NULL,
					   value INT NOT NULL,
					   weight INT NOT NULL);''')
    my_conn.commit()

def create_my_amrmory_weapon():
    my_curs.execute('''CREATE TABLE IF NOT EXISTS `armory_weapon` (
		  			   item_ptr_id INT PRIMARY KEY,
					   power INT NOT NULL);''')
    my_conn.commit()

def create_my_character():
    my_curs.execute('''CREATE TABLE IF NOT EXISTS `character` (
		  			   character_id INT PRIMARY KEY,
					   name VARCHAR(255) NOT NULL,
					   level INT NOT NULL,
					   exp INT NOT NULL,
					   hp INT NOT NULL,
					   strength INT NOT NULL,
					   intelligence INT NOT NULL,
					   dexterity INT NOT NULL);''')
    my_conn.commit()

def create_my_character_inv():
    my_curs.execute('''CREATE TABLE IF NOT EXISTS `character_inv` (
					   id INT PRIMARY KEY,
		  			   character_id INT NOT NULL,
					   item_id INT NOT NULL);''')
    my_conn.commit()

def create_my_cleric():
    my_curs.execute('''CREATE TABLE IF NOT EXISTS `cleric` (
		               character_ptr_id INT PRIMARY KEY,
		               using_shield BOOL NOT NULL,
		               mana INT NOT NULL);''')
    my_conn.commit()

def create_my_mage():
    my_curs.execute('''CREATE TABLE IF NOT EXISTS `mage` (
		               character_ptr_id INT PRIMARY KEY,
		               has_pet BOOL NOT NULL,
		               mana INT NOT NULL);''')
    my_conn.commit()

def insert_my_armory_item(curs, item_id, name, value, weight):
    query = '''INSERT INTO `armory_item` (item_id, name,
	       value, weight) VALUES (%s, %s, %s, %s);'''
    values = (item_id, name, value, weight)
    curs.execute(query, values)

def insert_my_armory_weapon(curs, item_ptr_id, power):
    query = '''INSERT INTO `armory_weapon` (item_ptr_id, power)
	       VALUES (%s, %s);'''
    values = (item_ptr_id, power)
    curs.execute(query, values)

def insert_my_character(curs, character_id, name, level, exp, hp, strength,
	                intelligence, dexterity):
    query = '''INSERT INTO `character` (character_id, name, level, exp,
	       hp, strength, intelligence, dexterity) VALUES
	       (%s, %s, %s, %s, %s, %s, %s, %s);'''
    values = (character_id, name, level, exp, hp, strength, intelligence,
              dexterity)
    curs.execute(query, values)

def insert_my_character_inv(curs, inv_id, character_id, item_id):
    query = '''INSERT INTO `character_inv` (id, character_id, item_id)
	       VALUES (%s, %s, %s);'''
    values = (inv_id, character_id, item_id)
    curs.execute(query, values)

def insert_my_cleric(curs, c_id, using_shield, mana):
    query = '''INSERT INTO `cleric` (character_ptr_id, using_shield, mana)
	       VALUES (%s, %s, %s);'''
    values = (c_id, using_shield, mana)
    curs.execute(query, values)

def insert_my_mage(curs, c_id, has_pet, mana):
    query = '''INSERT INTO `mage` (character_ptr_id, has_pet, mana)
	       VALUES (%s, %s, %s);'''
    values = (c_id, has_pet, mana)
    curs.execute(query, values)

def load_my_armory_item():
    sq3_curs.execute('SELECT * FROM `armory_item`;')
    for item_id, name, value, weight in sq3_curs.fetchall():
	insert_my_armory_item(my_curs, item_id, name, value, weight)
    my_conn.commit()

def load_my_armory_weapon():
    sq3_curs.execute('SELECT * FROM `armory_weapon`;')
    for item_ptr_id, power in sq3_curs.fetchall():
	insert_my_armory_weapon(my_curs, item_ptr_id, power)
    my_conn.commit()

def load_my_character():
    sq3_curs.execute('SELECT * FROM `charactercreator_character`;')
    lst = sq3_curs.fetchall()
    for char_id, name, lvl, exp, hp, strength, intl, dex, wis in lst:
 	insert_my_character(my_curs, char_id, name, lvl, exp,
   	                    hp, strength, intl, dex)
    my_conn.commit()

def load_my_character_inv():
    sq3_curs.execute('SELECT * FROM `charactercreator_character_inventory`;')
    for inv_id, character_id, item_id in sq3_curs.fetchall():
	insert_my_character_inv(my_curs, inv_id, character_id, item_id)
    my_conn.commit()

def load_my_cleric():
    sq3_curs.execute('SELECT * FROM `charactercreator_cleric`;')
    for c_id, using_shield, mana in sq3_curs.fetchall():
	insert_my_cleric(my_curs, c_id, using_shield, mana)
    my_conn.commit()

def load_my_mage():
    sq3_curs.execute('SELECT * FROM `charactercreator_mage`;')
    for c_id, has_pet, mana in sq3_curs.fetchall():
	insert_my_mage(my_curs, c_id, has_pet, mana)
    my_conn.commit()

def query_my_armory_item():
    my_curs.execute('SELECT * FROM `armory_item`;')
    return my_curs.fetchall()

def query_my_armory_weapon():
    my_curs.execute('SELECT * FROM `armory_weapon`;')
    return my_curs.fetchall()

def query_my_character(char_id):
    my_curs.execute('SELECT hp, strength, intelligence FROM `character` ' +
	            'WHERE character_id = {};'.format(char_id))
    return my_curs.fetchall()

def query_my_character_inv():
    my_curs.execute('SELECT * FROM `character_inv`;')
    return my_curs.fetchall()

def query_my_cleric():
    my_curs.execute('SELECT * FROM `cleric`;')
    return my_curs.fetchall()

def query_my_mage():
    my_curs.execute('SELECT * FROM `mage`;')
    return my_curs.fetchall()

def query_my_char_weapon_inv():
    my_curs.execute('''SELECT * FROM `armory_weapon` as aw
	               INNER JOIN `armory_item` as ai ON aw.item_ptr_id = ai.item_id
		       INNER JOIN `character_inv` as ci ON ci.item_id = ai.item_id
		       GROUP BY ci.character_id;''')
    return my_curs.fetchall()

def my_gain_hp(char_id, hp_gain):
    q = ('UPDATE `character` SET hp = hp + {} '.format(hp_gain) + 
	 'WHERE character_id = {}'.format(char_id))
    my_curs.execute(q)
    my_conn.commit()
    my_curs.execute('SELECT * FROM `character` WHERE character_id = {}'.
	format(char_id))
    return my_curs.fetchall()

def my_gain_strength(char_id, str_gain):
    q = ('UPDATE `character` SET strength = strength + {} '.format(str_gain) + 
         'WHERE character_id = {}'.format(char_id))
    my_curs.execute(q)
    my_conn.commit()
    my_curs.execute('SELECT * FROM `character` WHERE character_id = {}'.
	format(char_id))
    return my_curs.fetchall()

def my_gain_intelligence(char_id, int_gain):
    q = ('UPDATE `character` SET intelligence = intelligence + {} '.format(
	 int_gain) + 'WHERE character_id = {}'.format(char_id))
    my_curs.execute(q)
    my_conn.commit()
    my_curs.execute('SELECT * FROM `character` WHERE character_id = {}'.
	format(char_id))
    return my_curs.fetchall()

def drop_my_table(table_name):
    my_curs.execute(f'DROP TABLE IF EXISTS`{table_name}`;')
                                                                            
my_conn = connect_mysql(host = 'localhost', user = 'root',
	                passwd = 'touche5er#', database = 'db_one')
my_curs = get_curs(my_conn)
sq3_conn = connect_sqlite('rpg_db.sqlite3')
sq3_curs = get_curs(sq3_conn)
sq3_conn.close()
my_conn.close()
