from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

import models
import schemas
import auth

from database import engine, get_db
from models import User, Order

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Order Management System")

oauth2_scheme = HTTPBearer()


@app.get("/")
def root():
    return {"message": "API працює"}


def get_current_user(
    credentials = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    token = credentials.credentials
    username = auth.decode_token(token)

    if username is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user = db.query(User).filter(
        User.username == username
    ).first()

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


@app.post("/users/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    hashed_password = auth.hash_password(
        user.password
    )

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role="user"
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "User created"
    }


@app.post(
    "/users/login",
    response_model=schemas.Token
)
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db)
):
    db_user = db.query(User).filter(
        User.username == user.username
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if not auth.verify_password(
        user.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = auth.create_access_token(
        data={"sub": db_user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@app.post("/orders")
def create_order(
    order: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_order = Order(
        title=order.title,
        description=order.description,
        user_id=current_user.id
    )

    db.add(new_order)

    db.commit()

    db.refresh(new_order)

    return new_order


@app.get("/orders/{order_id}")
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):
    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@app.put("/orders/{order_id}")
def update_order(
    order_id: int,
    updated_data: schemas.OrderUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    # тільки owner або admin

    if (
        order.user_id != current_user.id
        and current_user.role != "admin"
    ):
        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    if updated_data.title:
        order.title = updated_data.title

    if updated_data.description:
        order.description = updated_data.description

    if updated_data.status:
        order.status = updated_data.status

    db.commit()

    db.refresh(order)

    return order


@app.delete("/orders/{order_id}")
def delete_order(
    order_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # тільки адміністратор

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Only admin can delete orders"
        )

    order = db.query(Order).filter(
        Order.id == order_id
    ).first()

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    db.delete(order)

    db.commit()

    return {
        "message": "Order deleted"
    }
