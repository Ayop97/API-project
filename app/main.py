from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post , user ,auth ,vote
from .config import settings



models.Base.metadata.create_all(bind=engine)
app= FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='FastAPI', user='postgres', password='Hero1997!', cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print("Database connection was successfull!")
#         break
        
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World my name is ayop"}


# @app.get("/posts")
# def get_posts(db:Session =Depends(get_db)):
#     # cursor.execute(""" SELECT * FROM posts """)
#     # posts= cursor.fetchall()
#     posts=db.query(models.Post).all()
#     return posts

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_post(post:schemas.PostCreate ,db:Session =Depends(get_db)):
#     # cursor.execute(""" INSERT INTO posts (title, content, Published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
#     # new_post =cursor.fetchone()
#     # conn.commit()
#     # new_post =models.Post(title=post.title,content=post.content,published=post.published)
#     new_post = models.Post(**post.dict())
#     db.add(new_post)
#     db.commit()
#     db.refresh(new_post)
#     return new_post


# @app.get("/posts/{id}")
# def get_post(id:int, db:Session =Depends(get_db)):
#     # cursor.execute("""  SELECT * FROM posts where id = %s """, str(id))
#     # post= cursor.fetchone()
#     post=db.query(models.Post).filter(models.Post.id == id).first()
#     print(post)
#     if not post:
#         #response.status_code = status.HTTP_404_NOT_FOUND
#         #return {"message:" f"post with id {id} not found"}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
#     return post

# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int , db:Session =Depends(get_db)):
#     # cursor.execute("""  DELETE FROM posts where id = %s RETURNING *""", str(id))
#     # delete_post=cursor.fetchone()
#     # conn.commit()
#     post=db.query(models.Post).filter(models.Post.id == id)
    
#     if post.first() ==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
#     post.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.put("/posts/{id}")
# def update_post(id: int , udpated_post:schemas.PostCreate, db:Session =Depends(get_db) ):
#     # cursor.execute("""  Update posts set title =%s, content =%s, published =%s where id = %s RETURNING *""", (post.title,post.content,post.published,str(id)))
#     # updated_post=cursor.fetchone()
#     # conn.commit()
#     post_query=db.query(models.Post).filter(models.Post.id == id)
#     post=post_query.first()

#     if post ==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} not found")
#     post_query.update(udpated_post.dict(), synchronize_session=False)
#     db.commit()

#     return post_query.first()


    




# @app.post("/users", status_code=status.HTTP_201_CREATED)
# def create_post(user:schemas.UserCreate ,db:Session =Depends(get_db)):
#     # cursor.execute(""" INSERT INTO posts (title, content, Published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
#     # new_post =cursor.fetchone()
#     # conn.commit()
#     # new_post =models.Post(title=post.title,content=post.content,published=post.published)
#     hashed_password= utils.hash(user.password)
#     user.password=hashed_password
#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user