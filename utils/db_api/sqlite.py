import sqlite3
import logging

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            fullname varchar(255) NOT NULL,
            yosh integer NOT NULL,
            jinsi varchar(10) NOT NULL,
            doimi varchar(100) NOT NULL,
            vaqtinchalik varchar(100) NOT NULL,
            ota varchar(20) NOT NULL,
            ona varchar(20) NOT NULL,
            talim varchar(30) NOT NULL,
            PRIMARY KEY (id)
            )
        """
        self.execute(sql, commit=True)

    def create_table_tests(self):
        # 2 5 7 9  13 15 16 17 18 19
        sql = """
        CREATE TABLE Tests(
        id int NOT NULL,
        test_1 varchar(5) NOT NULL,
        test_2 varchar(5) NOT NULL,
        test_3 varchar(5) NOT NULL,
        test_4 varchar(5) NOT NULL,
        test_5 varchar(5) NOT NULL,
        test_6 varchar(5) NOT NULL,
        test_7 varchar(5) NOT NULL,
        test_8 varchar(5) NOT NULL,
        test_9 varchar(5) NOT NULL,
        test_10 varchar(5) NOT NULL,
        test_11 varchar(5) NOT NULL,
        test_12 varchar(5) NOT NULL,
        test_13 varchar(5) NOT NULL,
        test_14 varchar(5) NOT NULL,
        test_15 varchar(5) NOT NULL,
        test_16 varchar(5) NOT NULL,        
        test_17 varchar(5) NOT NULL,       
        test_18 varchar(5) NOT NULL,
        test_19 varchar(5) NOT NULL,
        fikr_2 varchar(255) DEFAULT (NULL),
        fikr_5 varchar(255) DEFAULT (NULL),
        fikr_7 varchar(2555) DEFAULT (NULL),
        fikr_9 varchar(255) DEFAULT (NULL),
        fikr_13 varchar(5) DEFAULT (NULL),
        fikr_15 varchar(5) DEFAULT (NULL),
        fikr_16 varchar(255) DEFAULT (NULL),
        fikr_17 varchar(255) DEFAULT (NULL),
        fikr_18 varchar(255) DEFAULT (NULL),
        fikr_19 varchar(255) DEFAULT (NULL),
        PRIMARY KEY (id)
        )
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())
#--------------------------------------------Test-----------------------------------------------------------------------
    # 2 5 7 9  13 15 16 17 18 19
    def add_test(self, id: int,
                 test_1 : str,
                 test_2 : str,
                 test_3 : str,
                 test_4 : str,
                 test_5 : str,
                 test_6 : str,
                 test_7 : str,
                 test_8 : str,
                 test_9 : str,
                 test_10 : str,
                 test_11 : str,
                 test_12 : str,
                 test_13 : str,
                 test_14 : str,
                 test_15 : str,
                 test_16 : str,
                 test_17 : str,
                 test_18 : str,
                 test_19 : str,
                 fikr_2: str = None,
                 fikr_5: str = None,
                 fikr_7: str = None,
                 fikr_9: str = None,
                 fikr_13: str = None,
                 fikr_15: str = None,
                 fikr_16: str = None,
                 fikr_17: str = None,
                 fikr_18: str = None,
                 fikr_19 : str = None ):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Tests (id, test_1, test_2, test_3, test_4, test_5, test_6, test_7,  test_8, test_9,  test_10, test_11, test_12, test_13,  test_14, test_15, test_16,  test_17,  test_18,  test_19, fikr_2,  fikr_5, fikr_7, fikr_9, fikr_13, fikr_15, fikr_16, fikr_17, fikr_18 , fikr_19) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?)
        """
        self.execute(sql, parameters=(id, test_1, test_2, test_3, test_4, test_5, test_6, test_7,  test_8, test_9,  test_10, test_11, test_12, test_13,  test_14, test_15, test_16,  test_17,  test_18,  test_19, fikr_2,  fikr_5, fikr_7,fikr_9, fikr_13, fikr_15, fikr_16, fikr_17, fikr_18 , fikr_19), commit=True)

    # def get_test_id(self, idlist):
    #     idlist = tuple(idlist)
    #     sql = f"SELECT * FROM Tests WHERE id IN " + str(idlist)
    #     data = self.execute(sql, fetchall=True)
    #
    #     test_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    #     for i in data:
    #         for j in range(29):
    #             if j <= 18:
    #                 test_list[j] += " " + str(i[j + 1]) + " "
    #             else:
    #                 test_list[j] += str(i[j + 1]) + "\n"
    #
    #     return test_list

    def get_test(self, idlist):
        sql = f"SELECT * FROM Tests WHERE id IN ({str(idlist).replace('[', '').replace(']','')})"
        data = self.execute(sql, fetchall=1)
        test_list = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]
        for i in data:
            for j in range(29):
                if j <= 18:
                    test_list[j] += " " + str(i[j + 1]) + " "
                else:
                    test_list[j] += str(i[j + 1]) + "\n"

        return test_list

    def get_all_test(self):
        sql = f"SELECT * FROM Tests"
        data = self.execute(sql, fetchall=1)
        return data


    def get_statistic(self, test_list):
        qaytar = ""
        qaytar += f"1. Savol\nA. {test_list[0].count('A')}\nB. {test_list[0].count('B')}\nC. {test_list[0].count('C')}\nD. {test_list[0].count('D')}\nE. {test_list[0].count('E')}\n"
        qaytar += f"2. Savol\nA. {test_list[1].count('A')}\nB. {test_list[1].count('B')}\nC. {test_list[1].count('C')}\nD. {test_list[1].count('D')}\nE. {test_list[1].count('E')}\nF. {test_list[1].count('F')}\n"
        qaytar += f"3. Savol\nA. {test_list[2].count('A')}\nB. {test_list[2].count('B')}\nC. {test_list[2].count('C')}\nD. {test_list[2].count('D')}\nE. {test_list[2].count('E')}\n"
        qaytar += f"4. Savol\nA. {test_list[3].count('A')}\nB. {test_list[3].count('B')}\nC. {test_list[3].count('C')}\nD. {test_list[3].count('D')}\nE. {test_list[3].count('E')}\n"
        qaytar += f"5. Savol\nA. {test_list[4].count('A')}\nB. {test_list[4].count('B')}\nC. {test_list[4].count('C')}\nD. {test_list[4].count('D')}\n"
        qaytar += f"6. Savol\nA. {test_list[5].count('A')}\nB. {test_list[5].count('B')}\nC. {test_list[5].count('C')}\nD. {test_list[5].count('D')}\n"
        qaytar += f"7. Savol\nA. {test_list[6].count('6')}\nB. {test_list[6].count('6')}\nC. {test_list[6].count('C')}\nD. {test_list[6].count('D')}\nE. {test_list[6].count('E')}\n"
        qaytar += f"8. Savol\nA. {test_list[7].count('A')}\nB. {test_list[7].count('B')}\nC. {test_list[7].count('C')}\nD. {test_list[7].count('D')}\n"
        qaytar += f"9. Savol\nA. {test_list[8].count('A')}\nB. {test_list[8].count('B')}\nC. {test_list[8].count('C')}\nD. {test_list[8].count('D')}\nE. {test_list[8].count('E')}\n"
        qaytar += f"10. Savol\n1. {test_list[9].count(' 1 ')}\n2. {test_list[9].count('2')}\n3. {test_list[9].count('3')}\n4. {test_list[9].count('4')}\n5. {test_list[9].count('5')}\n6. {test_list[9].count('6')}\n7. {test_list[9].count('7')}\n8. {test_list[9].count('8')}\n9. {test_list[9].count('9')}\n10. {test_list[9].count('10')}\n"
        qaytar += f"11. Savol\n1. {test_list[10].count(' 1 ')}\n2. {test_list[10].count(' 2 ')}\n3. {test_list[10].count(' 3 ')}\n4. {test_list[10].count(' 4 ')}\n5. {test_list[10].count(' 5 ')}\n6. {test_list[10].count(' 6 ')}\n7. {test_list[10].count(' 7 ')}\n8. {test_list[10].count(' 8 ')}\n9. {test_list[10].count(' 9 ')}\n10. {test_list[10].count('10')}\n"
        qaytar += f"11. {test_list[10].count('11')}\n12. {test_list[10].count('12')}\n13. {test_list[10].count('13')}\n14. {test_list[10].count('14')}\n15. {test_list[10].count('15')}\n16. {test_list[10].count('16')}\n17. {test_list[10].count('17')}\n18. {test_list[10].count('18')}\n"
        qaytar += f"12. Savol\nA. {test_list[11].count('A')}\nB. {test_list[11].count('B')}\nC. {test_list[11].count('C')}\nD. {test_list[11].count('D')}\n"
        qaytar += f"13. Savol\nA. {test_list[12].count('A')}\nB. {test_list[12].count('B')}\nC. {test_list[12].count('C')}\nD. {test_list[12].count('D')}\nE. {test_list[12].count('E')}\nF. {test_list[12].count('F')}\nG. {test_list[12].count('G')}\n"
        qaytar += f"14. Savol\nA. {test_list[13].count('A')}\nB. {test_list[13].count('B')}\nC. {test_list[13].count('C')}\nD. {test_list[13].count('D')}\nE. {test_list[13].count('E')}\nF. {test_list[13].count('F')}\nG. {test_list[13].count('G')}\nH. {test_list[13].count('H')}\nI. {test_list[13].count('I')}\nJ. {test_list[13].count('J')}\n"
        qaytar += f"15. Savol\nA. {test_list[14].count('A')}\nB. {test_list[14].count('B')}\nC. {test_list[14].count('C')}\nD. {test_list[14].count('D')}\nE. {test_list[14].count('E')}\nF. {test_list[14].count('F')}\nG. {test_list[14].count('G')}\nH. {test_list[14].count('H')}\nI. {test_list[14].count('I')}\n"
        qaytar += f"16. Savol\nA. {test_list[15].count('A')}\nB. {test_list[15].count('B')}\nC. {test_list[15].count('C')}\n"
        qaytar += f"17. Savol\nA. {test_list[16].count('A')}\nB. {test_list[16].count('B')}\nC. {test_list[16].count('C')}\nD. {test_list[16].count('D')}\nE. {test_list[16].count('E')}\n"
        qaytar += f"18. Savol\nA. {test_list[17].count('A')}\nB. {test_list[17].count('B')}\nC. {test_list[17].count('C')}\nD. {test_list[17].count('D')}\nE. {test_list[17].count('E')}\nG. {test_list[17].count('G')}\n"
        qaytar += f"19. Savol\nA. {test_list[18].count('A')}\nB. {test_list[18].count('B')}\nC. {test_list[18].count('C')}\nD. {test_list[18].count('D')}\nE. {test_list[18].count('E')}\n"
        qaytar += f"2. Savol fikrlar:\n{test_list[19]}"
        qaytar += f"5. Savol fikrlar:\n{test_list[20]}"
        qaytar += f"7. Savol fikrlar:\n{test_list[21]}"
        qaytar += f"9. Savol fikrlar:\n{test_list[22]}"
        qaytar += f"13. Savol fikrlar:\n{test_list[23]}"
        qaytar += f"15. Savol fikrlar:\n{test_list[24]}"
        qaytar += f"16. Savol fikrlar:\n{test_list[25]}"
        qaytar += f"17. Savol fikrlar:\n{test_list[26]}"
        qaytar += f"18. Savol fikrlar:\n{test_list[27]}"
        qaytar += f"19. Savol fikrlar:\n{test_list[28]}"
        qaytar = qaytar.replace("None\n", "")

        return qaytar






# --------------------------------------------Users----------------------------------------------------------------------
    def add_user(self, id: int, fullname: str, yosh: int,jinsi: str, doimi: str, vaqtinchalik: str,ota: str, ona: str, talim:str):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Users(id, fullname, yosh, jinsi, doimi, vaqtinchalik, ota, ona,talim) VALUES(?, ?, ?, ?, ?, ?, ?, ?,?)
        """
        self.execute(sql, parameters=(id, fullname, yosh, jinsi, doimi, vaqtinchalik, ota, ona, talim), commit=True)

    def get_allUser(self):
        sql = "SELECT * FROM Users"
        data =self.execute(sql, fetchall=True)
        return data

    def get_all_users(self):
        sql = """
        SELECT id FROM Users
        """
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])

        return id_list

    # yosh
    # jinsi
    # doimi
    # vaqtinchalik
    # ota
    # ona
    # talim

    def select_yosh(self, yosh):
        yosh =str(yosh)
        sql = f"SELECT id FROM Users WHERE yosh = {yosh}"
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])

        return id_list

    # yosh
    # jinsi
    # doimi
    # vaqtinchalik
    # ota
    # ona
    # talim

    def select_all(self, yosh = None, jins = None, doimi = None, vaqtinchalik = None, ota = None, ona = None, talim = None):
        sql = f"SELECT id FROM Users WHERE "
        if yosh != None:
            sql += f"yosh = {yosh} "
        if jins != None:
            sql += f" jinsi = {jins} "
        if doimi!=None:
            sql += f"AND doimi = {doimi} "
        if vaqtinchalik != None:
            sql += f"AND vaqtinchalik = {vaqtinchalik} "
        if ota != None:
            sql += f"AND ota = {ota} "
        if ona != None:
            sql +=  f" AND ona = {ona} "
        if talim != None:
            sql += f" AND talim = {talim}"
        id_list = list()
        
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])

        return id_list

    def select_yosh_oraligi(self, yosh1, yosh2):

        sql = f"SELECT id FROM Users WHERE yosh >= {yosh1} AND yosh <= {yosh2}"
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])

        return id_list

    def select_jinsi(self, jins):
        sql = f"SELECT id FROM Users WHERE jinsi = '{jins}'"
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])
        return id_list

    def select_doimi(self, doimi):
        sql = f"SELECT id FROM Users WHERE doimi = '{doimi}'"
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])
        return id_list

    def select_vaqtinchalik(self, vaqtinchalik):
        sql = f"SELECT id FROM Users WHERE vaqtinchalik = '{vaqtinchalik}'"
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])
        return id_list

    def select_ota(self, ota):
        sql = f"SELECT id FROM Users WHERE ota = " + str("\""+ota+"\"")
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])
        return id_list

    def select_ona(self, ona):
        sql = f"SELECT id FROM Users WHERE ona = " + str("\""+ona+"\"")
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])
        return id_list

    def select_talim(self, talim):
        sql = f"SELECT id FROM Users WHERE talim = '{talim}'"
        id_list = list()
        data = self.execute(sql, fetchall=True)
        for i in data:
            id_list.append(i[0])
        return id_list

    def get_user_id(self):
        sql = """
        SELECT id FROM Users WHERE yosh=20
        """
        return self.execute(sql, fetchall=True)


    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Tests;", fetchone=True)


    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)
        
    def delete_tests(self):
        self.execute("DELETE FROM Tests WHERE TRUE", commit=True)
#---------------------------------EndUsers------------------------------------------------------------------------------


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")