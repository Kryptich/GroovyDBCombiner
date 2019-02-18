#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  User Database | Select Operations Application (for a personal job screening)
#

import re
import os
import binascii
import pymysql
import unidecode as undec

emailValidation = re.compile(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$")  # Regex matching for valid email entries.

def yesNo(question): # Simple and tolerant mechanism to take yes/no from user
    while True:
        reply = str(input(question + ' (Y/N): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

def inputNumber(prompt): # Function to receive number from user.
    while True:
        try:
            userInput = input(prompt)
            checkNULL = userInput
            if userInput == "":
                userInput = 0
            userInput = int(userInput)
            if checkNULL == '':
                userInput = None
        except ValueError:
            print("Please enter numbers only -- no commas, spaces or currency symbol needed.")
            continue
        else:
            return userInput
            break

def pickDB(db = 42): # Choose from either DB using the new layout
        while db not in (1, 2):
            db = inputNumber('\nCHOOSE DB:    [1]: Original on-site DB (demo_accounts_db)  '+
                                           '[2]: Combined DB (demo_accounts_db_new)  ')
            print('')
            if db == 1:
               return 'demo_accounts_db'
            elif db == 2:
                return 'demo_accounts_db_new'
            else:
                print('Invalid DB choice. Try again: ')

def displayMenu(options, choice = 42): # Global operations user menu
    print("\n:::[MAIN MENU]:::\n")
    for i in range(len(options)):
        print("{:d}. {:s}".format(i + 1, options[i]))
    while choice >= (len(options) + 2):
        choice = inputNumber("\nPlease choose an option: ")
        print('')
        if choice is None:
            choice = 8
    return choice

#####################################################################################################
# The User Class. Follows exactly our desired 'user' structure (deduplicated, heirarchical) to more #
# elegantly organize, generate, and reference users as entities throughout this script. #############
class User:
    def __init__(self,user_id=(bytes.decode(binascii.b2a_hex(os.urandom(10)).upper())), # Default ID hash
                 login=None, email=None, fname=(""), lname=(""), tel1=None, tel2=None,        # Personals
                 ulica=(""), linia2=(""), kodpocz="", miejscowosc=(""), kraj=(""),  # Address information
                 corp={'name': 'Unnamed', 'email': 'None', 'nip': None}):# store corp info as simple dict
        # Initiate attributes
        self.user_id = user_id
        self.login = login
        self.email = email
        self.fname = fname
        self.lname = lname
        self.tel1 = tel1
        self.tel2 = tel2
        self.ulica = ulica
        self.linia2 = linia2
        self.kodpocz = kodpocz
        self.miejscowosc = miejscowosc
        self.kraj = kraj
        self.corp = corp

    @classmethod            # CLI User addition method. Re-declares attributes to skip 'self' prefixing.
    def from_input(cls,user_id=(bytes.decode(binascii.b2a_hex(os.urandom(10)).upper())), # Default ID hash
                 login=None, email=None, fname=(""), lname=(""), tel1=None, tel2=None, # Personals
                 ulica=(""), linia2=(""), kodpocz="", miejscowosc=(""), kraj=(""), # Address information
                 corp={'name': 'Unnamed', 'email': 'None', 'nip': None}):  # Store corp info as simple dict

        ########################## UID LOGIC ###################################################
        sql = "SELECT ID from users where ID ='{}'".format(user_id)
        cur.execute(sql)
        while cur.fetchall():
            user_id = (bytes.decode(binascii.b2a_hex(os.urandom(10)).upper()))
            cur.execute(sql)
        print("UID has been generated automatically:", user_id)
        fname = input("User first name: ").title()                          # Input first name
        lname = input("User last name: ").title()                           # Input last name

        login_buffer = undec.unidecode((fname.lower().replace(
            " ", "") + '.' + lname.lower().replace(" ", "")))

        ########################## USERNAME LOGIC ##############################################
        sql = "SELECT * from users where login ='{}'".format(login_buffer)
        cur.execute(sql)
        results = []
        rcount = 0
        print("Generating username from fname, lname: ", login_buffer)
        while cur.fetchall():
            print("There's a problem, this user already exists. Use ",
                login_buffer, (len(results) + 1),
                '[1], or define custom username [2]?: ', sep="", end="")
            choice = 5
            while True:
                choice = inputNumber("")
                if choice == 1:
                    login_buffer = (login_buffer + (len(results) + 1))
                    print('Suffixing successful.')
                    break
                elif choice == 2:
                    login_buffer = input("Enter custom username:")
                    break
                else:
                    print("\nPlease choose valid option!")
            cur.execute(sql)
        else:
            print("Username ",login_buffer,' was committed.', sep='')
        login = login_buffer

        ########################## ORGANIZATIONAL CHECKS #######################################
        is_corp = yesNo("Is this account associated with a company/organization?")
        if is_corp:                                       # Organizational checks
            corp['nip'] = str(
                inputNumber("NIP (if associated with company): "))
            sql = "SELECT company_name from companies where nip_fk ='{}'".format(
                corp['nip'])
            cur.execute(sql)
            results = cur.fetchall()
            org_found = []
            for row in results:
                org_found.append(row[0])
            if org_found:
                print("User has been successfully linked to the organization '",
                    org_found[0], "'. Please enter remaining information.", sep="")
            else:
                print("Organization not registered with Allegro. Please provide information: ")
                corp['name'] = input(
                    "What is the name of user's organization? ").title()
                corp['email'] = input("Organization contact email, if any: ")

        ########################## EMAIL VALIDATION ############################################
        email = input("User email (required): ")
        if email == '':
            email = None #  <<<< allow empty email as NULL entry in DB
        else:
            while True:
                while not emailValidation.match(email):
                    email = input("User email (required): ")
                    if not emailValidation.match(email):
                        print("Invalid email format. Retry.")
                sql = "SELECT * from users where email ='{}'".format(email)
                cur.execute(sql)
                email_duplicity_check = []
                dup = ''
                for row in cur:
                    email_duplicity_check.append(row[2])
                    dup = str(row[2])
                    print(dup)
                if email == dup:
                    emailreplace = yesNo(
                        "User email'" + email +
                        "' already exists. Disconnect from previous and associate to this account?" +
                        "(WARNING::: EXISTING ACCOUNT MAY NO LONGER RECEIVE EMAIL NOTIFICATIONS)")
                    if emailreplace:
                        sql = "update users set email=REPLACE(email,'{}','{} (DISCONNECTED)')".format(
                            dup, dup)
                        cur.execute(sql)
                        conn.commit()
                        print('SUCCESSFULLY REASSIGNED EMAIL.')
                        break
                    else:
                        break
                break

        ######################## CONTACT AND ADDRESS INFO ######################################
        tel1 = inputNumber("User telephone # 1: ")
        tel2 = inputNumber("User telephone # 2: ")
        ulica = input("User adres ulicy (ex. Wędkarska 29): ")
        linia2 = input("Adres linia 2? (apt, instructions) (else ENTER): ")
        kodpocz = input("User kod pocztowy (tylko cyfry): ")
        miejscowosc = input("User Miejscowość: ")
        kraj = input("Kraj użytkownika: ")

        return cls(user_id, login, email, fname, lname, tel1, tel2, ulica,
                   linia2, kodpocz, miejscowosc, kraj, corp)

    ############################ USER DISPLAY FORMATTING #######################################
    def Display(self):    # Print DB results to console
        print("     LOGIN ID:", self.login, '\n    ', 41 * '_', '\n')
        print("            Name:   |", self.fname.title())
        print("         Surname:   |", self.lname.title())
        print("          e-Mail:   |", self.email)
        if str(self.ulica) != '':
            print("         Address:   |", self.ulica.title(), self.linia2.title())
        if str(self.kodpocz) != '':
            print("                    | ", self.kodpocz, ' ', self.miejscowosc,sep="")
        if str(self.kraj) != '':
            print("                    |", self.kraj)
        if self.corp['nip'] is not None:
            print("     Organization:  | ", self.corp['name'], ' | CONTACT: ',
             self.corp['email'],' (NIP ',self.corp['nip'],')', sep='')
        print("\n          ----------- Other information:  ---------")
        print("          TEL #1:", self.tel1,"   TEL #2:", self.tel2, "   UID:", self.user_id,'\n')


##########################################################################################################
# The User Database Object. Takes 'db' parameter to specify active database. Interacts with MySQL cursor #
# to modify and display the database. ####################################################################

class UserDB(object):
    def __init__(self,db):
        self.db = db

    ############################## USER DISPLAY FORMATTING #######################################
    def insert_or_remove_user(self, user, remove = False):
        # SET ACTIVE DATABASE
        sql = """USE {}""".format(self.db)
        cur.execute(sql)

        ######################################## USER REMOVAL ####################################
        if remove:
            execute = ''
            users_matched = []
            while len(users_matched) != 1:
                user_input = input('\nWhich user would you like to remove? Enter ID, login or corp NIP: ')
                sql = """SELECT `ID`, `login`, `nip` FROM users WHERE `ID` LIKE '%{0}%' OR `login` \
                         LIKE '%{0}%' OR `nip` LIKE '%{0}%'""".format(user_input)
                cur.execute(sql)

                find_user = cur.fetchall()
                users_matched = []             # Clear list for retry
                for row in find_user:
                    users_matched.append([row[0],row[1],row[2]])
                if users_matched:
                    if len(users_matched) == 1:
                        print('User',users_matched[0][1],'was matched, ',end='')
                        if users_matched[0][2]:
                            print('and is part of an organization (NIP ',
                                   users_matched[0][2],'); ',sep='', end='' )
                        print('remove this user?')
                        confirm = yesNo('')
                        if confirm:
                            print('User',users_matched[0][1],'with ID of',
                                   users_matched[0][0],'marked for removal.')
                            execute = str(users_matched[0][1])
                        else: print('\nNo changes will be made to the database.\n')
                    if len(users_matched)>1:
                        print("\nMultiple user match(es) found:")
                        for row in users_matched:
                            print (row[0],row[1],row[2])
                        print("\nYou'll need to be more specific:")
                else: print('\nNo users found. Try again. ')
            if execute != '':
                sql = """DELETE FROM users WHERE `login` = '{}'""".format(execute)
                affected_rows = cur.execute(sql)
                print(affected_rows,'rows affected.\n')
                print('Removing any dangling UIDs ... \n')
                sql = """DELETE FROM unique_id WHERE ID NOT IN (SELECT f.ID FROM users f)"""
                cur.execute(sql)
                conn.commit()  # Commit all changes

        #################################### ADD USER TO DB ####################################
        else:
            sql = """SELECT company_name from companies where nip_fk = '{}' """.format(
                     user.corp['nip'])

            nip_or_hash = user.user_id
            corpticker = 0

            cur.execute(sql)
            conn.commit()
            results = cur.fetchall()
            org_found = []
            for row in results:
                org_found.append(row[0])

            sql = "SELECT * from unique_id where ID =%s OR %s"
            cur.execute(sql, (user.user_id, user.corp['nip']))
            id_exists = False
            for row in cur:
                id_exists = True

            if user.corp['nip'] != None:
                sql = "SELECT * from unique_id where ID =%s "
                print(user.corp['nip'])
                cur.execute(sql, (user.corp['nip']))
                nip_in_UID = False
                for row in cur:
                    nip_in_UID = True

            is_corp_user = False
            if user.corp['nip'] is not None:
                is_corp_user = True

            sql = "SELECT * from users where login = %s"
            cur.execute(sql, (user.login))
            login_exists = False
            for row in cur:
                login_exists = True

            sql = "SELECT * from users where email ='{}'".format(user.email)
            cur.execute(sql)
            if not id_exists and not login_exists: #  <<<< EMAIL EXISTENCE CHECKS
                email_duplicity_check = []
                dup = ''
                for row in cur:
                    email_duplicity_check.append(row[2])
                    dup = str(row[2])
                    print('this is the email match we found:', dup)
                if user.email == dup:
                    print("User email '", user.email,
                          "' already exists. Disconnecting from previous and ",
                          "associating with this account.", sep='')                 # SQL TO DISCONNECT OLD EMAIL
                    sql = "update users set email=REPLACE(email,'{}','{} (DISCONNECTED)')".format(dup, dup)
                    cur.execute(sql)
                    conn.commit()
                    print('SUCCESSFULLY REASSIGNED EMAIL.')

            ######################### CASES WHERE NIP OR ID ALREADY IN DB ######################
            if id_exists:
                print(nip_or_hash)
                if is_corp_user:
                    print('USER IS CORP.')
                    corpticker = 1 # <<< for is_corporate column in unique_id table
                    nip_or_hash = user.corp['nip']
                    if not org_found:
                        print('ORG NOT FOUND.')                                     # Add NIP to unique_id if new org
                        sql = "INSERT INTO unique_id(ID, is_corporate) \
                        VALUES (%s, %s)"
                        try:
                            cur.execute(sql, (nip_or_hash, corpticker))
                            conn.commit()
                            print("SUCCESSFULLY INSERTED UNIQUE ID")
                        except Exception as ex:
                            pass # fine error handling unnecessary for now

                        sql = "INSERT INTO companies(company_name, email, nip_fk) \
                            VALUES (%s, %s, %s)"                                    # Add new Company if required
                        cur.execute(
                            sql, (user.corp['name'], user.corp['email'], user.corp['nip']))
                        conn.commit()
                        print("SUCCESFULLY COMMITTED NEW COMPANY")
                    else:
                        if not nip_in_UID:
                            print('ORG FOUND, BUT HAD NO USERS.')
                            sql = "INSERT INTO unique_id(ID, is_corporate) \
                            VALUES (%s, %s)"
                            cur.execute(sql, (nip_or_hash, corpticker))
                            conn.commit()
                            print("SUCCESSFULLY INSERTED UNIQUE ID")
                        print("There isn't a need to create a new company for this job...")

            ############################### CREATE MAIN USER ENTRY #############################
            if not is_corp_user:
                print("User isn't corporate.")
                sql = """
                    INSERT INTO unique_id(ID, is_corporate)
                    VALUES (%s, %s)
                    """
                try:
                    cur.execute(sql, (nip_or_hash, corpticker))
                    conn.commit()
                    print("SUCCESSFULLY INSERTED UNIQUE ID") ###### ADD UID (NON-CORP) #########
                except Exception as ex:
                    pass # fine error handling unnecessary for now

            if not login_exists:                            ########## ADD USER ENTRY  #########
                sql = """
                    INSERT INTO users(ID, login, email, first_name, last_name, \
                    tel1, tel2, ul, linia_2, kodpocz, miejscowosc, kraj, nip) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """
                try:
                    cur.execute(sql,
                        (nip_or_hash, user.login, user.email, user.fname, user.lname,
                         user.tel1, user.tel2, user.ulica, user.linia2, user.kodpocz,
                         user.miejscowosc, user.kraj, user.corp['nip']))
                    conn.commit()
                    print("\nUser has been successfully added to DB.\n")
                except Exception as ex:
                    pass # fine error handling unnecessary for now
            else:
                print('User "',user.login,'" already exists in target database. Skipping to preserve ',
                      'account integrity.\n\n','='*69,'\n\n',sep='')

    ########################### REMAP OLD (FLAT) USERS TO NEW LAYOUT ###########################
    def remapSchema(self,targetdb):
        check = yesNo(
            "This tool will merge a database which uses the old/flat schema (" + self.db +") with one which "+
            "is already using a deduplication strategy for corporate accounts (" + targetdb +"). Proceed? ")
        if check:
            sql = """USE {}""".format(self.db)
            cur.execute(sql)
            sql = "SELECT * from users"
            cur.execute(sql)
            results = cur.fetchall()
            for row in results:
                print('User to import: (raw data):\n', row)
                user_id = row[0]
                login = row[1]
                fname = row[2]
                lname = row[3]
                email = row[4]
                tel1 = row[5]
                tel2 = row[6]
                ulica = row[7]
                linia2 = row[8]
                kodpocz = row[9]
                miejscowosc = row[10]
                kraj = row[11]
                nip = row[13]
                corp = {'name': 'Unnamed', 'email': 'None', 'nip': None}
                if nip not in ('', None):
                    corp['nip'] = nip
                    corp['name'] = row[12]
                remapped = User(user_id,login,fname,lname,email,tel1,tel2,
                                ulica,linia2,kodpocz,miejscowosc,kraj,corp)
                print('Remap successfull. Forwarding to deduplication mechanism as:\n')
                # Display user remapping results to console
                remapped.Display()
                # Insert remapped user object into new database
                UserDB(targetdb).insert_or_remove_user(remapped)
            choice = yesNo('\nThe combination was successful. Print the combined database ('+ targetdb +') ? ' )
            print ('')
            if choice:
                UserDB(targetdb).display_userdb()
        else:
            print("No worries! Messing with databases isn't for the faint of heart.")

    ########################### DISPLAY THE USER DATABASE ######################################
    def display_userdb(self):
        print('Printing results from DB "',self.db,'".','\n\n','='*69,'\n\n',sep='')
        sql = """USE {}""".format(self.db)
        cur.execute(sql)
        sql = "SELECT * from users"
        cur.execute(sql)
        results = cur.fetchall()

        for row in results:
            user_id = row[0]
            login = row[1]
            fname = row[2]
            lname = row[3]
            email = row[4]
            tel1 = row[5]
            tel2 = row[6]
            ulica = row[7]
            linia2 = row[8]
            kodpocz = row[9]
            miejscowosc = row[10]
            kraj = row[11]
            nip = row[12]
            corp = {'name': 'Unnamed', 'email': 'None', 'nip': None}
            if nip != None:
                sql = "SELECT * from companies where nip_fk ='{}'".format(nip)
                cur.execute(sql)
                results = cur.fetchall()
                for row in results:
                    corp['name'] = row[0]
                    corp['email'] = row[1]
                    corp['nip'] = row[2]
            User(user_id, login, fname, lname, email, tel1, tel2,
                 ulica, linia2, kodpocz, miejscowosc, kraj, corp).Display()


################################## !! MAIN FUNCTION LOOP !! ####################################
def main():
    global conn #   <<<<<<<<<<<<<<<<<<<<<<<< Make the connection accessible to other functions
    conn   = pymysql.connect(host='localhost',           # Connect to the local MySQL server
                             port=3306,                  #     (security not a priority here)
                             user='allegro_db_user',
                             passwd='Default_Passwrd',
                             db='demo_accounts_db',
                             charset='utf8')
    global cur #    <<<<<<<<<<<<<<<<<<<<<<<<<<< Make the cursor accessible to other functions
    cur = conn.cursor()                                  # Open a cursor on active connection


    #####################################| MENU OPTIONS |#######################################
    menuItems = ['View User Database', 'Add / Remove User',
                 'Import Separate DB (w/ old flat schema)', 'Quit']

    print("\n||||||| ALLEGRO USER ACCOUNT MANAGEMENT ||||||")
    print("""
| To to use this program, please first ensure you have these databases available ---
| 'demo_accounts_db', 'demo_accounts_db_new' (an exact copy of 'demo_accounts_db',
| created to preserve original from damage) and demo_accounts_db_old_flat. """
    )
    while True:
        choice = displayMenu(menuItems)

        if choice == 1:
            print("\nVIEW FULL USER DATABASE:\n")
            UserDB(pickDB()).display_userdb()

        elif choice == 2:
            rm_choice = 999
            rm = False
            while rm_choice not in (1,2):
                rm_choice = inputNumber('\n[1]: Add new user to DB  '+
                                 '[2]: Remove user by ID/Allegro Login  ')
                if rm_choice == 1:
                    pass
                elif rm_choice == 2:
                    rm = True
                else:
                    print('Invalid DB choice. Try again: ')
            if rm:
                print("\n====== [USER REMOVAL MODE] ======\n")
                UserDB(pickDB()).insert_or_remove_user(User(),remove=True)
            elif not rm:
                UserDB(pickDB()).insert_or_remove_user(User.from_input())

        elif choice == 3:
            UserDB('demo_accounts_db_old_flat').remapSchema(targetdb = 'demo_accounts_db_new')

        else:
            cur.close()
            conn.close()
            quit()

######################################### END MAIN FUNCTION ####################################

if __name__ == '__main__':
    main()
