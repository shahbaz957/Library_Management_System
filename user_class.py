from database import connect_db

class user :
    def add_user(self,name):
        conn = connect_db()
        c = conn.cursor()
        c.execute("INSERT INTO user (name) VALUES(?)",(name,))
        conn.commit()
        conn.close()
        print(f"User of name {name} has been added")
    def list_user(self):
        conn=connect_db()
        c = conn.cursor()
        c.execute("SELECT * FROM user")
        data = c.fetchall()
        conn.commit()
        conn.close()
        if data:
            print("Following are the registered users:\n")
            for d in data:
                
                print(f"{d[0]} : {d[1]} --> issued book of ID {d[2]} ")
        else:
            print("No user is registered yet")
