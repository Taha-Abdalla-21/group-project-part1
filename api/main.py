from fastapi import FastAPI

from .models import model_loader
from .routers.orders import router as orders_router
from .routers.order_details import router as order_details_router
from .routers.customers import router as customers_router
from .routers.menu_items import router as menu_items_router
from .routers.payments import router as payments_router
from .routers.reviews import router as reviews_router
from .routers.resources import router as resources_router
from .routers.promotions import router as promotions_router

app = FastAPI()

model_loader.index()

app.include_router(orders_router)
app.include_router(order_details_router)
app.include_router(customers_router)
app.include_router(menu_items_router)
app.include_router(payments_router)
app.include_router(reviews_router)
app.include_router(resources_router)
app.include_router(promotions_router)