from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session

from .models import model_loader
from .dependencies.database import get_db

from .controllers import orders as orders_controller
from .controllers import order_details as order_details_controller
from .controllers import customers as customers_controller
from .controllers import menu_items as menu_items_controller
from .controllers import payments as payments_controller
from .controllers import reviews as reviews_controller
from .controllers import resources as resources_controller
from .controllers import promotions as promotions_controller

from .schemas import orders as orders_schema
from .schemas import order_details as order_details_schema
from .schemas import customers as customers_schema
from .schemas import menu_items as menu_items_schema
from .schemas import payments as payments_schema
from .schemas import reviews as reviews_schema
from .schemas import resources as resources_schema
from .schemas import promotions as promotions_schema

app = FastAPI()

model_loader.index()

# Orders
@app.post("/orders/", response_model=orders_schema.Order, tags=["Orders"], status_code=status.HTTP_201_CREATED)
def create_order(request: orders_schema.OrderCreate, db: Session = Depends(get_db)):
    return orders_controller.create(db, request)

@app.get("/orders/", response_model=list[orders_schema.Order], tags=["Orders"])
def read_orders(db: Session = Depends(get_db)):
    return orders_controller.read_all(db)

@app.get("/orders/{item_id}", response_model=orders_schema.Order, tags=["Orders"])
def read_one_order(item_id: int, db: Session = Depends(get_db)):
    return orders_controller.read_one(db, item_id)

@app.put("/orders/{item_id}", response_model=orders_schema.Order, tags=["Orders"])
def update_order(item_id: int, request: orders_schema.OrderUpdate, db: Session = Depends(get_db)):
    return orders_controller.update(db, item_id, request)

@app.delete("/orders/{item_id}", tags=["Orders"], status_code=status.HTTP_204_NO_CONTENT)
def delete_order(item_id: int, db: Session = Depends(get_db)):
    return orders_controller.delete(db, item_id)

# Order Details
@app.post("/orderdetails/", response_model=order_details_schema.OrderDetail, tags=["Order Details"], status_code=status.HTTP_201_CREATED)
def create_order_detail(request: order_details_schema.OrderDetailCreate, db: Session = Depends(get_db)):
    return order_details_controller.create(db, request)

@app.get("/orderdetails/", response_model=list[order_details_schema.OrderDetail], tags=["Order Details"])
def read_order_details(db: Session = Depends(get_db)):
    return order_details_controller.read_all(db)

@app.get("/orderdetails/{item_id}", response_model=order_details_schema.OrderDetail, tags=["Order Details"])
def read_one_order_detail(item_id: int, db: Session = Depends(get_db)):
    return order_details_controller.read_one(db, item_id)

@app.put("/orderdetails/{item_id}", response_model=order_details_schema.OrderDetail, tags=["Order Details"])
def update_order_detail(item_id: int, request: order_details_schema.OrderDetailUpdate, db: Session = Depends(get_db)):
    return order_details_controller.update(db, item_id, request)

@app.delete("/orderdetails/{item_id}", tags=["Order Details"], status_code=status.HTTP_204_NO_CONTENT)
def delete_order_detail(item_id: int, db: Session = Depends(get_db)):
    return order_details_controller.delete(db, item_id)

# Customers
@app.post("/customers/", response_model=customers_schema.Customer, tags=["Customers"], status_code=status.HTTP_201_CREATED)
def create_customer(request: customers_schema.CustomerCreate, db: Session = Depends(get_db)):
    return customers_controller.create(db, request)

@app.get("/customers/", response_model=list[customers_schema.Customer], tags=["Customers"])
def read_customers(db: Session = Depends(get_db)):
    return customers_controller.read_all(db)

@app.get("/customers/{item_id}", response_model=customers_schema.Customer, tags=["Customers"])
def read_one_customer(item_id: int, db: Session = Depends(get_db)):
    return customers_controller.read_one(db, item_id)

@app.put("/customers/{item_id}", response_model=customers_schema.Customer, tags=["Customers"])
def update_customer(item_id: int, request: customers_schema.CustomerCreate, db: Session = Depends(get_db)):
    return customers_controller.update(db, item_id, request)

@app.delete("/customers/{item_id}", tags=["Customers"], status_code=status.HTTP_204_NO_CONTENT)
def delete_customer(item_id: int, db: Session = Depends(get_db)):
    return customers_controller.delete(db, item_id)

# Menu Items
@app.post("/menuitems/", response_model=menu_items_schema.MenuItem, tags=["Menu Items"], status_code=status.HTTP_201_CREATED)
def create_menu_item(request: menu_items_schema.MenuItemCreate, db: Session = Depends(get_db)):
    return menu_items_controller.create(db, request)

@app.get("/menuitems/", response_model=list[menu_items_schema.MenuItem], tags=["Menu Items"])
def read_menu_items(db: Session = Depends(get_db)):
    return menu_items_controller.read_all(db)

@app.get("/menuitems/{item_id}", response_model=menu_items_schema.MenuItem, tags=["Menu Items"])
def read_one_menu_item(item_id: int, db: Session = Depends(get_db)):
    return menu_items_controller.read_one(db, item_id)

@app.put("/menuitems/{item_id}", response_model=menu_items_schema.MenuItem, tags=["Menu Items"])
def update_menu_item(item_id: int, request: menu_items_schema.MenuItemCreate, db: Session = Depends(get_db)):
    return menu_items_controller.update(db, item_id, request)

@app.delete("/menuitems/{item_id}", tags=["Menu Items"], status_code=status.HTTP_204_NO_CONTENT)
def delete_menu_item(item_id: int, db: Session = Depends(get_db)):
    return menu_items_controller.delete(db, item_id)

# Payments
@app.post("/payments/", response_model=payments_schema.Payment, tags=["Payments"], status_code=status.HTTP_201_CREATED)
def create_payment(request: payments_schema.PaymentCreate, db: Session = Depends(get_db)):
    return payments_controller.create(db, request)

@app.get("/payments/", response_model=list[payments_schema.Payment], tags=["Payments"])
def read_payments(db: Session = Depends(get_db)):
    return payments_controller.read_all(db)

@app.get("/payments/{item_id}", response_model=payments_schema.Payment, tags=["Payments"])
def read_one_payment(item_id: int, db: Session = Depends(get_db)):
    return payments_controller.read_one(db, item_id)

@app.put("/payments/{item_id}", response_model=payments_schema.Payment, tags=["Payments"])
def update_payment(item_id: int, request: payments_schema.PaymentCreate, db: Session = Depends(get_db)):
    return payments_controller.update(db, item_id, request)

@app.delete("/payments/{item_id}", tags=["Payments"], status_code=status.HTTP_204_NO_CONTENT)
def delete_payment(item_id: int, db: Session = Depends(get_db)):
    return payments_controller.delete(db, item_id)

# Reviews
@app.post("/reviews/", response_model=reviews_schema.Review, tags=["Reviews"], status_code=status.HTTP_201_CREATED)
def create_review(request: reviews_schema.ReviewCreate, db: Session = Depends(get_db)):
    return reviews_controller.create(db, request)

@app.get("/reviews/", response_model=list[reviews_schema.Review], tags=["Reviews"])
def read_reviews(db: Session = Depends(get_db)):
    return reviews_controller.read_all(db)

@app.get("/reviews/{item_id}", response_model=reviews_schema.Review, tags=["Reviews"])
def read_one_review(item_id: int, db: Session = Depends(get_db)):
    return reviews_controller.read_one(db, item_id)

@app.put("/reviews/{item_id}", response_model=reviews_schema.Review, tags=["Reviews"])
def update_review(item_id: int, request: reviews_schema.ReviewCreate, db: Session = Depends(get_db)):
    return reviews_controller.update(db, item_id, request)

@app.delete("/reviews/{item_id}", tags=["Reviews"], status_code=status.HTTP_204_NO_CONTENT)
def delete_review(item_id: int, db: Session = Depends(get_db)):
    return reviews_controller.delete(db, item_id)

# Resources
@app.post("/resources/", response_model=resources_schema.Resource, tags=["Resources"], status_code=status.HTTP_201_CREATED)
def create_resource(request: resources_schema.ResourceCreate, db: Session = Depends(get_db)):
    return resources_controller.create(db, request)

@app.get("/resources/", response_model=list[resources_schema.Resource], tags=["Resources"])
def read_resources(db: Session = Depends(get_db)):
    return resources_controller.read_all(db)

@app.get("/resources/{item_id}", response_model=resources_schema.Resource, tags=["Resources"])
def read_one_resource(item_id: int, db: Session = Depends(get_db)):
    return resources_controller.read_one(db, item_id)

@app.put("/resources/{item_id}", response_model=resources_schema.Resource, tags=["Resources"])
def update_resource(item_id: int, request: resources_schema.ResourceCreate, db: Session = Depends(get_db)):
    return resources_controller.update(db, item_id, request)

@app.delete("/resources/{item_id}", tags=["Resources"], status_code=status.HTTP_204_NO_CONTENT)
def delete_resource(item_id: int, db: Session = Depends(get_db)):
    return resources_controller.delete(db, item_id)

# Promotions
@app.post("/promotions/", response_model=promotions_schema.Promotion, tags=["Promotions"], status_code=status.HTTP_201_CREATED)
def create_promotion(request: promotions_schema.PromotionCreate, db: Session = Depends(get_db)):
    return promotions_controller.create(db, request)

@app.get("/promotions/", response_model=list[promotions_schema.Promotion], tags=["Promotions"])
def read_promotions(db: Session = Depends(get_db)):
    return promotions_controller.read_all(db)

@app.get("/promotions/{item_id}", response_model=promotions_schema.Promotion, tags=["Promotions"])
def read_one_promotion(item_id: int, db: Session = Depends(get_db)):
    return promotions_controller.read_one(db, item_id)

@app.put("/promotions/{item_id}", response_model=promotions_schema.Promotion, tags=["Promotions"])
def update_promotion(item_id: int, request: promotions_schema.PromotionCreate, db: Session = Depends(get_db)):
    return promotions_controller.update(db, item_id, request)

@app.delete("/promotions/{item_id}", tags=["Promotions"], status_code=status.HTTP_204_NO_CONTENT)
def delete_promotion(item_id: int, db: Session = Depends(get_db)):
    return promotions_controller.delete(db, item_id)