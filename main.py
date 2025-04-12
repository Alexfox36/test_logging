from fastapi import FastAPI
import uvicorn
import logging

log = logging.getLogger(__name__)
fh = logging.FileHandler("app.log")
fh.setLevel(logging.DEBUG)
fh.setFormatter(
    logging.Formatter(
        "[%(asctime)s.%(msecs)03d] %(module)5s:%(lineno)3d %(levelname)-7s - %(message)s"
    )
)
log.addHandler(fh)
log.setLevel(logging.DEBUG)


app = FastAPI()


admin = [
    {"id": 1, "title": "Админ панель", "decsription": "какое-то описание"},
]

log.debug("get_admin")


@app.get("/admin/dashboard")
def get_admin():
    return admin


log.info("get_auth")


@app.get("/api/v1/auth/login")
def get_auth():
    return None


log.warning("get_orders")


@app.get("/api/v1/orders")
def get_orders():
    return None


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
