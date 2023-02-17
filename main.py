import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.app:app", port=8081, reload=True)

# @app.get('/get_users')
# def get_users():
#     return "MyRoot"z

# @app.post('/create_users/')
# def create_user(user: User):
#     return None
