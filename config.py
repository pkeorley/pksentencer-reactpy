from dotenv import dotenv_values


env = dotenv_values("venv/.env")
datas = {
    "MONGO_URL": env["MONGO_URL"]
}
