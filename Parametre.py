
hostname="127.0.0.1"
username="root" 
password="root"
database="testdb"

# create Param table 
def Create_Table_Param():
    try:
        db = MySQLdb.connect(host=hostname,user=username, passwd=password, db=database)
        curs=db.cursor()
        # curs.execute("DROP TABLE `rpi`.`Parametre`;")
        curs.execute("""CREATE TABLE IF NOT EXISTS Parametre(
        id INT NOT NULL AUTO_INCREMENT,
        Param_Nom varchar(40) NOT NULL,
        Param_Valeur varchar(100) NOT NULL,
        PRIMARY KEY (id))
        """)
        db.commit()  # accept the changes
        print("Table Parametre, if not exists, created")
        db.close()
    except Exception as e:
        db.close()
        print(e)
#********************************************************

#********************************************************
# Insert Param table
def Insert_Update_Param():
    try:
        db = MySQLdb.connect(host=hostname,user=username, passwd=password, db=database)
        curs=db.cursor()
        # curs.execute("""Truncate Table Parametre""")
        # La syntaxe REPLACE permet de créer ou de mettre à jour un paramètre existant
        curs.execute("""REPLACE INTO `Parametre` (`id`, `Param_Nom`, `Param_Valeur`) VALUES
        ( 1, 'Version',      'NOT USED'),
        ( 2, 'Url_WS',       'NOT USED'),
        ( 3, 'timeout',      '2'),
        ( 4, 'idreader',     'TBD-01'),
        ( 5, 'Url_ping',     'NOT USED'),
        ( 6, 'timeout_ping', '2'),
        ( 7, 'lcd_addr',     '0x27'),
        ( 8, 'url_WS_HELLO_L', 'NOT USED')
        ;""")
        db.commit()  # accept the changes
        print("Table Parametre Updated")
        db.close()
    except Exception as e:
        print(e)
        db.close()
        pass
#********************************************************
    
#********************************************************
def Update_Param_lcd(lcd_addr):
# Ces paramètres seront insérés que la première fois, les autres fois, comme ils sont déjà présents, il seront ignorés
    try:
        db = MySQLdb.connect(host=hostname,user=username, passwd=password, db=database)
        curs=db.cursor()
        curs.execute("UPDATE Parametre SET Param_Valeur='%s' WHERE Param_Nom='lcd_addr'"%(lcd_addr))
        db.commit()  # accept the changes
        print("lcd_addr Updated",lcd_addr)
        db.close()
    except Exception as e:
        # print(e)
        db.close()

#******************************************************
#********************************************************
# Update Param table
def UPDATE_Param(Param_Valeur,Param_Nom):
    try:
        db = MySQLdb.connect(host=hostname,user=username, passwd=password, db=database)
        curs=db.cursor()
        # RPI Name (pour information)
        curs.execute("UPDATE Parametre SET Param_Valeur='%s' WHERE Param_Nom='%s'"%(Param_Valeur,Param_Nom))
        print("Parametre "+str(Param_Nom)+" Updated: ",Param_Valeur)
        db.commit()
        db.close()
    except Exception as ex:
        print(ex)
        db.close()
#********************************************************
def i2cdetect():
    bus = smbus.SMBus(1) # 1 indicates /dev/i2c-1
    for device in range(128):
        try:
             bus.read_byte(device)
             Update_Param_lcd(hex(device))
             return hex(device)
        except: # exception if read_byte fails
             pass
