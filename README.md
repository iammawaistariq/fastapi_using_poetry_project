# FastAPI using Poetry Project

1. Run command in terminal in a folder where you want to create poetry folder `poetry new fastapi_using_poetry_project`
2. Jump to newly created poetry folder by `cd fastapi_using_poetry_project`
3. Open Project in VS Code
4. Git init - Create Github repository to upload code
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
8. Run `poetry run uvicorn fastapi_using_poetry_project.main:app --relaod` command in CMD to run uvicorn server
9. Write `test_main.py` file to test your code.
10. Run `poetry run pytest -v` on your VS Code terminal or new CMD terminal
