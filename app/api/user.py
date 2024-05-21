# from fastapi import FastAPI, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app.schemas.user import User, UserCreate
# from app.services.user import create_user, get_user, get_user_by_username
# from app.api.deps import get_db
#
# app = FastAPI()
#
#
# @app.post("/users/", response_model=User)
# def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Username already registered")
#     return create_user(db=db, user=user)
#
#
# @app.get("/users/{user_id}", response_model=User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
