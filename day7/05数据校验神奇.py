from pydantic import  BaseModel,Field,ValidationError

class User(BaseModel):
    id : int
    name: str = Field(...,min_length=3,max_length=8,description="设置长度3-8的字符")
    age : int = Field(...,ge=0,le=116,description="填写年龄0-116岁")

if __name__ == "__main__":
    try:
        user = User(id=1, name="aldjkl", age=22)
        usr_json = user.model_dump_json()
        print("返回json格式：{usr_json}")
    except ValidationError as e:
        print(f"校验失败原因是：{e}")
    else:
        print("ok")
    finally:
        print("神器体验完毕")

