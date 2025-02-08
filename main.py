from fastapi import FastAPI
from routes.NmapRoute import nmap_scanning_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["http://localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nmap_scanning_router)
