import pandas as pd
import mysql.connector as sql
import os, sys
pckg_path = os.path.abspath(os.path.join(__file__,"../../../../.."))
sys.path.append(pckg_path)
#from  crdatabase import crdatabase
MYSQL_HOST = '129.146.85.135'
MYSQL_PORT = '3306'
path = os.path.abspath(__file__)
dir_path = os.path.dirname(path)
db_connection = sql.connect(host='129.146.85.135', database='landing', user='root', password='crmysql**##', auth_plugin='mysql_native_password')
db_cursor = db_connection.cursor()

if __name__ == '__main__':
	print(os.getenv('MYSQL_HOST'))
	if os.getenv('MYSQL_HOST'):
		pass
		#print('1')
		# print('1')
		# rlvnt_menu = pd.read_csv("/webservice/ws/pos/rlvnt_menu.csv")
		# queue = pd.read_csv("/webservice/ws/pos/queue.csv")
		# orig_menu = pd.read_csv("/webservice/ws/pos/orig_menu.csv")
		# MYSQL_HOST = os.getenv('MYSQL_HOST')
		# MYSQL_PORT = os.getenv('MYSQL_PORT')

	else:
		#print(dir_path)
		pos_list = []
		inventoryrules_list = []
		time_list = []
		for file in os.listdir(dir_path):
			filename = os.fsdecode(file)
			if filename.startswith('pos'):
				#print(filename)
				pos = pd.read_csv(filename, index_col = None, header = 0)
				pos_list.append(pos)
			elif filename.startswith('inventory'):
				#print(filename)
				inv = pd.read_csv(filename, index_col = None, header = 0)
				inventoryrules_list.append(inv)
			elif filename.startswith('Time'):
				#print(filename)
				tim = pd.read_csv(filename, index_col = None, header = 0)
				time_list.append(tim)
		#posframe = pd.concat(pos_list, axis = 0, ignore_index = True)
		#invframe = pd.concat(inventoryrules_list, axis = 0, ignore_index = True)
		#timframe = pd.concat(time_list, axis = 0, ignore_index = True)


	#posframe.drop(['Unnamed: 0'], axis = 1, inplace = True)
	#invframe.drop(['Unnamed: 0'], axis = 1, inplace = True)
	#timframe.drop(['Unnamed: 0'], axis = 1, inplace = True)
	#posframe['TCTime'] = posframe['TCTime'].str[7:15]
	#posframe['OrderStored'] = posframe['OrderStored'].str[7:15]
	#posframe['OrderTotaled'] = posframe['OrderTotaled'].str[7:15]
	#posframe['OrderTendered'] = posframe['OrderTendered'].str[7:15]
	#posframe['OrderDrawerClose'] = posframe['OrderDrawerClose'].str[7:15]
	#db = crdatabase('landing', MYSQL_HOST, MYSQL_PORT, 'root', 'crmysql**##')

	#db.dataframetomysql(posframe, 'pos', 'landing', 'append')
	#db.dataframetomysql(invframe, 'inventory_rules', 'landing', 'append')
	#db.dataframetomysql(timframe, 'TimeAggDemandInput', 'landing', 'append')