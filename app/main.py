from fastapi import FastAPI
from app.db import database, User_veg, Advice
from app.models import UserReg, UserIn, AdviceVeg
from app.hashing import Hasher
from typing import List
UserUpdate = User_veg.get_pydantic(exclude={"id", "email", "password"})
app = FastAPI(title="FastAPI, Docker")
@app.post("/user/register/", summary="endpoints(3.2) for User_veg")
async def create_user(user_in: UserReg):
    """
    Здесь перевод всех полей:

    - **email**: почта,
    - **password**: пароль,
    - **tomatoes**: помидоры,
    - **cucumbers**: огурцы,
    - **raspberries**: малина,
    - **strawberries**: клубника,
    - **potatoes**: картошка,
    - **sweet_cherry**: черешня,
    - **plums**: слива,
    - **cherry**: вишня,
    - **apple_tree**: яблоня,
    - **pepper**: перец,
    - **dill**: укроп,
    - **parsley**: петрушка,
    - **watermelon**: арбуз,
    - **melon**: дыня.
    """
    hashed_password = Hasher.get_password_hash(user_in.dict()["password"])
    user_in_db = {}
    for key, value in user_in.dict().items():
        if key == "password":
            user_in_db[key] = str(hashed_password)
        else:
            user_in_db[key] = value
    await User_veg.objects.create(**user_in_db)
    return {"register": True}
@app.get("/user/register/", response_model=List[UserReg], summary="endpoints(3.1) for User_veg")
async def read_all_db():
    """
    This GET request need for register.
    """
    all_db = await User_veg.objects.all()
    return all_db
@app.put("/user/register/{user_id}/", summary="endpoints(3.3) for User_veg")
async def update_user(user_id: int, user_up: UserUpdate):
    user_db = await User_veg.objects.get(pk=user_id)
    await user_db.update(**user_up.dict())
    return {"update": True}
@app.delete("user/register/{user_id}/", summary="endpoints(3.4) for User_veg")
async def delete_user(user_del: UserReg):
    pass
@app.get("user/input/", summary="endpoints(3.5) for input")
async def user_input(user_inp: UserIn):
    pass
@app.post("user/advice/", summary="endpoints(3.8) for Advice")
async def create_advice(vegetable: AdviceVeg):
    pass
@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # create a dummy entry
    # await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


"""
While I choose the third option.
1) frontend - main - endpoints
main: (POST: /user/register/ - {"email": "vova@user.com", "password": "gig8gf7gfubkho", "tomatoes": True, ...}) 
# password = hashed_password # send JSON

endpoints: (GET: /user/register/) # get JSON
endpoints: (POST: /user/register/ - {"register": True}) # send Json and save user
main: (GET: /user/register/) # get JSON


2) frontend - main
main: (GET: /user/register/)
main: (POST: /user/register/)
main: (PUT: /user/register/)
main: (DELETE: /user/register/)


3) frontend - main - endpoints

endpoints for register:
3.1)endpoints: (GET: /user/register/) # get all data from User_veg table.
3.2)endpoints: (POST: /user/register/ - UserReg) # create user in User_veg table.
3.3)endpoints: (PUT: /user/register/{user_id}/ - UserReg) # update table in  User_veg table. 
3.4)endpoints: (DELETE: /user/register/{user_id}/ - UserReg) # delete user from User_veg table {not required}.


endpoints for input:
3.5)endpoints: (GET: /user/input/ - UserIn) # check user to want to input.


endpoints for Advice: # (I won't use these endpoints. These endpoints are needed for me).
3.6)endpoints: (GET: /user/advice/) # get all data from Advice table.
3.7)endpoints: (PUT: /user/advice/{veg_id}) # update table in Advice table.
3.8)endpoints: (POST: /user/advice/ - AdviceVeg) # create object in Advice table.
3.9)endpoints: (DELETE: /user/advice/{veg_id}/ - AdviceVeg) # delete object from Advice table.


Main:
3.10)main: (GET: /?q=true/false) # for frontend input or register. - 3.5 or 3.2
# 3.11)main: (GET: /veg/) # for frondent choose veg. - 3.3
3.11)main: (POST: /veg/ - UserReg{exclude: email, password}) - in frontend
3.12)main: (POST: /user/ - UserReg, AdviceVeg) # compare tables and output list of AdviceVeg models according to said in UserReg - in frontend

Soon I add function which let user download img.
"""