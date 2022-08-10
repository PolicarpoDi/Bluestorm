from fastapi import FastAPI
from router import router_user, router_other

app = FastAPI()

# Initial Route
@app.get("/")
def rota_root():
    return {"Messagem": "Bem vindo a API da Bruestorm"}


# Routers User
app.include_router(router_user.router)
 
# Routers Patients, Pharmacies and Transactions
app.include_router(router_other.router)

