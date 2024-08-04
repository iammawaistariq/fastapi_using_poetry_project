# FastAPI using Poetry Project

1. `poetry new fastapi_using_poetry_project`
2. `cd fastapi_using_poetry_project`
3. Open Project in VS Code
4. Git init
5. Open file "pyproject.toml"
6. Install new packages in poetry project
    `poetry add fastapi "uviorn[standard]`
    ```
    [tool.poetry.dependencies]
    python = "^3.12"
    fastapi = "^0.112.0"
    uvicorn = {extras = ["standard"], version = "^0.30.5"}
    ```
7. Create `main.py` file in `fastapi_using_poetry_project`