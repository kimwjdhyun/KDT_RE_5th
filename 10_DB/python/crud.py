import mysql.connector
from mysql.connector import Error


# conn = mysql.connector.connect(
#     host='localhost',
#     user='user',       # your_username
#     password='1234',   # your_password
#     database='codingon' # your_database_name
# )

# cursor = conn.cursor()

# 사용자 정보 입력 받기
# username = input("사용자 ID를 입력하세요 : ")
# password = input("비밀번호를 입력하세요 : ")
# name = input("이름을 입력하세요 : ")
# email = input("이메일을 입력하세요 : ")

# # INSERT
# sql = "INSERT INTO users (username, password, name, email) VALUES (%s, %s, %s, %s)"
# user_data = (username, password, name, email)

# cursor.execute(sql, user_data)
# conn.commit()

# print("사용자 등록이 완료되었습니다.")

# # SELECT

# username = input("ID: ")
# password = input("PW: ")

# cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
# user = cursor.fetchone()

# if user:
#     print(user)
#     print(f"로그인 성공! 환영합니다. {user[3]}님")
# else:
#     print("로그인 실패! 아이디 또는 비밀번호가 잘못되었습니다.")


# # UPDATE
# user_id = input("수정할 사용자 ID : ")
# new_name = input("새 이름 : ")
# new_email = input("새 이메일 : ")

# sql = "UPDATE users SET name = %s, email = %s WHERE user_id = %s"
# cursor.execute(sql, (new_name, new_email, user_id))
# conn.commit()
# print("사용자 정보가 수정되었습니다.")


# DELETE
# user_id = input("삭제할 사용자 id : ")
# sql = "DELETE FROM users WHERE user_id = %s"
# cursor.execute(sql, (user_id,))
# conn.commit()
# print("사용자가 삭제되었습니다.")

# CRUD 실습

conn = mysql.connector.connect(
    host='localhost',
    user='user',       # your_username
    password='1234',   # your_password
    database='codingon' # your_database_name
)

cursor = conn.cursor()

# 1. CREATE
sql = "INSERT INTO posts (author, content) VALUES (%s, %s)"
value = ("김정현", "안녕하세요 반갑습니다.")
cursor.execute(sql, value)
conn.commit()
print("실습 1. CREATE", value)

# 2. SELECT
# 1)
read = "SELECT * FROM posts ORDER BY created_at DESC"
cursor.execute(read)
for row in cursor.fetchall():
    print("실습 2-1. READ 최신순", row[1])

# 2)
cursor.execute("SELECT * FROM posts WHERE author = %s", ("김정현",))
for row in cursor.fetchall():
    print("실습 2-2. READ 특정 작성자", row[1])

# 3. UPDATE
sql = "UPDATE posts SET content = %s WHERE id = %s"
update = ("다들 행복한 하루 되세요!", 1)
cursor.execute(sql, update)
conn.commit()
print("실습 3. UPDATE : 수정되었습니다.")

# 4. DELETE
sql = "DELETE FROM posts WHERE id = %s"
delete = (1,)
cursor.execute(sql, delete)
conn.commit()
print("실습 4. DELETE : 삭제되었습니다.")

# 연결 종료
conn.close()