import pypyodbc
import xml.etree.ElementTree as etree
import xml.dom.minidom
import logging

logger = logging.getLogger("be_Error_logs")
hdlr = logging.FileHandler("./Logs/be_Error.logs")
formater = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formater)
logger.addHandler(hdlr)
logger.setLevel(logging.ERROR)

class connect():
    def __init__(self):
        try:
            # make connection
            self.conn = pypyodbc.connect('Driver={SQL Server}; Server=DESKTOP-9A1HCKG;Database=pubs')

            # create cursor objects
            self.cur = self.conn.cursor()

            # create sql query and store it into variable
            self.cmd = "SELECT a.* ,b.title,b.price,b.advance,b.pubdate,a.qty * b.price as payment FROM (select a.*,b.stor_name,b.stor_address,b.city,b.state,b.zip from dbo.sales as a inner join dbo.stores as b on a.stor_id = b.stor_id) as a inner join dbo.titles as b ON a.title_id = b.title_id FOR XML PATH('SALE'), ROOT('SALES')"
        except Exception as obj:
            print('Error occur while initializing the connection.')
            logger.error(obj)


    def xmlgenerate(self):
        try:
            # execute the sql query and store it into variable
            self.cur.execute(self.cmd)
            rows = self.cur.fetchall()


            nml = '<?xml version="1.0"?>'
            i = 0
            while i < len(rows):
                nml = nml + str(rows[i][0])
                i = i + 1 

            self.dom = xml.dom.minidom.parseString(nml)
            self.dom = self.dom.toprettyxml()

            with open('sales_reports.xml', 'w') as f:
                f.writelines(self.dom)

            self.conn.close()
        except Exception as obj:
            print('Error occur while generating xml.')
            logger.error(obj)