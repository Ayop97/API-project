from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']

)

# /users/
# /users

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_post(user:schemas.UserCreate ,db:Session =Depends(get_db)):
    # cursor.execute(""" INSERT INTO posts (title, content, Published) VALUES(%s,%s,%s) RETURNING * """,(post.title,post.content,post.published))
    # new_post =cursor.fetchone()
    # conn.commit()
    # new_post =models.Post(title=post.title,content=post.content,published=post.published)
    hashed_password= utils.hash(user.password)
    user.password=hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}", response_model=schemas.UserOut)
def get_post(id:int, db:Session =Depends(get_db)):
    # cursor.execute("""  SELECT * FROM posts where id = %s """, str(id))
    # post= cursor.fetchone()
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {"message:" f"post with id {id} not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} not found")
    return user