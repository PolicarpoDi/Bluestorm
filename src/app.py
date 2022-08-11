from fastapi import FastAPI, status
from routers import pharmacies_routers, user_routers

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {'Mensagem': 'Bem vindo a API Bluestorm'}


# Router User
app.include_router(user_routers.router, prefix='/user')


# Router Pharmacies
app.include_router(pharmacies_routers.router)








