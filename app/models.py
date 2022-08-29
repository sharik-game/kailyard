from pydantic import BaseModel, Field

class UserReg(BaseModel):
    email: str
    password: str
    tomatoes: bool = Field(default=False)
    cucumbers: bool = Field(default=False)
    raspberries: bool = Field(default=False)
    strawberries: bool = Field(default=False)
    potatoes: bool = Field(default=False)
    sweet_cherry: bool = Field(default=False)
    plums: bool = Field(default=False)
    cherry: bool = Field(default=False)
    apple_tree: bool = Field(default=False)
    pepper: bool = Field(default=False)
    dill: bool = Field(default=False)
    parsley: bool = Field(default=False)
    watermelon: bool = Field(default=False)
    melon: bool = Field(default=False)


class UserIn(BaseModel):
    email: str    
    password: str
class AdviceVeg(BaseModel):
    veg_name: str = Field(title="Название растения")
    when_pinch: str = Field(title="Когда сажать")
    how_feed: str = Field(title="Чем кормить")
    where_pinch: str = Field(title="Где сажать")
    how_handle: str = Field(title="Чем обрабатывать")
    when_feed: str = Field(title="Когда кормить")
    when_handle: str = Field(title="Когда обрабатывать")
    when_take: str = Field(title="Когда собирать")
    common_illness: str = Field(title="Распространённые болезни")