from fastapi import APIRouter
from app.db import get_connection, create_connection
from fastapi import HTTPException
from app.schemas.user import UserCreate, UserUpdate
from app.schemas.user import PostCreate, Post, PostUpdate

router = APIRouter()

@router.get("/users")
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()
    conn.close()
    return result

    # users = []
    # for row in result:
    #     users.append([
    #         "user_id" : row[0],
    #         "username" : row[1],
    #         "name" : row[2],
    #         "email" ; row[3],
    #         "created_at" : row[4].strftime("%y-%m-%d %H:%M:%S")
    #     ])

@router.post("/users")
def create_user(user : UserCreate):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "INSERT INTO users (username, password, name, email) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (user.username, user.password, user.name, user.email))
        conn.commit()
        return{"message" : "User created successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@router.put("/users/{user_id}")
def update_user(user_id : int, user : UserUpdate):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "UPDATE users SET name = %s, email = %s WHERE user_id = %s"
        cursor.execute(sql, (user.name, user.email, user_id))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="user not found")
    
        return {"message" : "user updated successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@router.delete("/users/{user_id}")
def delete_user(user_id : int):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "DELETE FROM users WHERE user_id = %s"
        cursor.execute(sql, (user_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="user not found")
    
        return {"message" : "user deleted successfully"}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# 실습 CRUD
# Create
@router.post("/posts")
def create_post(post : PostCreate):
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)

        sql = "INSERT INTO posts (author, content) VALUES (%s,%s)"
        cursor.execute(sql, (post.author, post.content))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=400, detail="failed")
        return {"message" : "Post created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# Read
# 최신순으로 불러오기
@router.get("/posts")
def read_posts():
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, author, content, created_at From posts ORDER BY created_at DESC")
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# 특정 작성자의 글만 불러오기
@router.get("/posts/author/{author_name}")
def read_posts_by_author(author_name: str):
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM posts WHERE author = %s ORDER BY created_at DESC", (author_name,))
        results = cursor.fetchall()
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# UPDATE
@router.put("/posts/{post_id}")
def update_post(post_id: int, post: PostUpdate):
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "UPDATE posts SET content = %s WHERE id = %s"
        cursor.execute(sql, (post.content, post_id))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Post not found")
        else:
            return {"message": f"Post {post_id} updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# DELETE
@router.delete("/posts/{post_id}")
def delete_post(post_id: int):
    try:
        conn = create_connection()
        cursor = conn.cursor(dictionary=True)
        sql = "DELETE FROM posts WHERE id = %s"
        cursor.execute(sql, (post_id,))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Post not found")
        else:
            return {"message": f"Post {post_id} deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            