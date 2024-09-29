from fastapi import FastAPI

app = FastAPI()

@app.get("/factorial/{startnum}")
def factorial(startnum: int):
    if startnum == 0:
        return {"result": False}

    rs = 1
    num = startnum

    while num > 1:
        rs *= num
        num -= 1

    return {"starting_number": startnum, "factorial": rs}