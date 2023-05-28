import psycopg2
from typing import List
from Secrets import *

class Databases():
    def __init__(self):
        try:
            self.db = psycopg2.connect(host=SECRET_HOST, dbname=SECRET_DBNAME, user=SECRET_USER,password=SECRET_PASSWORD,port=SECRET_PORT, connect_timeout=3)
            self.cursor = self.db.cursor()
        except psycopg2.DatabaseError as db_err:
            print("Not connected")
            print(db_err)

    def __del__(self):
        self.db.close()
        self.cursor.close()

    def execute(self,query,args={}):
        #print("execute :" + query)
        self.cursor.execute(query,args)
        row = self.cursor.fetchall()
        return row

    def commit(self):
        self.cursor.commit()

    def insertDB(self,schema,table,column,data):
        sql = " INSERT INTO {schema}.{table}(news_key, title, content, reporter_id, pub) VALUES (%s, %s, %s, %s, %s) ;".format(schema=schema,table=table)
        try:
            self.cursor.execute(sql, data)
            #self.db.commit()
        except Exception as e :
            print("insert DB  ",e)
            self.db.rollback()
        else:
            print(data[0])
            self.db.commit()

    def insertTistoryBlogLink(self, hostname, url):
        schema = "public"
        table = "tistory_blogs"
        sql = " INSERT INTO {schema}.{table}(hostname, url) VALUES {sql_str_val} ;".format(schema=schema,table=table, sql_str_val=f"('{hostname}', '{url}')")
        try:
            print(sql)
            self.cursor.execute(sql)
            #self.db.commit()
        except Exception as e :
            print("insert DB  ",e)
            print(sql)
            self.db.rollback()
        else:
            print(sql)
            self.db.commit()
    
    def insertTistoryBlogBody(self, hostname, url, body):
        schema = "public"
        table = "tistory"
        # 특수문자 제거
        body = body.replace("%", '')
        sql = " INSERT INTO {table}(hostname, url, body) VALUES {sql_str_val} ;".format(table=table, sql_str_val=f"('{hostname}', '{url}', $YEJIN${body}$YEJIN$)")
        try:
            # print(sql)
            self.cursor.execute(sql, body)
            #self.db.commit()
        except Exception as e :
            print("DB에서 exception발생")
            print("insert DB  ",e)
            print(sql[:200])
            print(sql[-50:])

            self.db.rollback()
        else:
            # print(sql)
            self.db.commit()

    def selectTistoryBlogBody(self, limit, offset):
            schema = "public"
            table = "tistory"
           
            sql = f" SELECT a.body, a.url FROM tistory a ORDER BY url ASC LIMIT {limit} OFFSET {offset};"
            try:
                # print(sql)
                self.cursor.execute(sql)
                result = self.cursor.fetchall()
                return result
                #self.db.commit()
            except Exception as e :
                print("DB에서 exception발생")
                print("insert DB  ",e)
                print(sql[:200])
                print(sql[-50:])

                self.db.rollback()

    # offset: 시작 위치, limit: 개수
    def selectTistoryLink(self, offset:int, limit:int) -> List[tuple]:
        schema = "public"
        table = "tistory"
        sql = f" SELECT DISTINCT ON (HOSTNAME) URL FROM tistory_blogs ORDER BY HOSTNAME, URL DESC LIMIT {limit} OFFSET {offset};"
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            if len(result) == 0 and offset > 6700: # 미안 나중에 고칠게
                return
            else: 
                print(result)
                return result
            #self.db.commit()
        except Exception as e :
            print("insert DB  ",e)
            print(sql)
            self.db.rollback()
        else:
            print(sql)
            self.db.commit()
    
    def updatistoryBlogCleanedBody(self, url, title, body, isParsedByMachine):
        schema = "public"
        table = "tistory"
        # 특수문자 제거
        title = title.replace("%", '')
        body = body.replace("%", '')
        if isParsedByMachine is None:
            _isParsedByMachine = "unknown"
        else:
            if isParsedByMachine:
                _isParsedByMachine = "true"
            else:
                _isParsedByMachine = "false"

        sql = " UPDATE {table} SET cleaned_title = {title}, cleaned_body = {body}, is_parsed_by_machine = {_isParsedByMachine} WHERE url = '{url}';".format(table=table, title = f'$YEJIN${title}$YEJIN$', body = f'$YEJIN${body}$YEJIN$', _isParsedByMachine = _isParsedByMachine, url=url)
        try:
            # print(sql[100:])
            self.cursor.execute(sql)
            #self.db.commit()
        except Exception as e :
            print("DB에서 exception발생")
            print("insert DB  ",e)
            self.db.rollback()
        else:
            # print(sql)
            self.db.commit()
