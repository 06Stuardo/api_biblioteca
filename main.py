from fastapi import FastAPI
from routers import users_router, auth_router, meta_router, query_router, reports_router, upload_router, etl_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router.router)
app.include_router(auth_router.router)
app.include_router(meta_router.router)
app.include_router(query_router.router)
app.include_router(reports_router.router)
app.include_router(upload_router.router)
app.include_router(etl_router.router)


