"""
成绩小助手（列表+字典+排序+分组）
需求：
● 保存学生成绩
● 修改成绩
● 统计：平均分、及格名单、Top3、分组（及格/不及格）
"""

# 学生列表：每个元素是一个字典，保存 name / score
students = [
    {"name": "Tom", "score": 80},
    {"name": "Jerry", "score": 59},
    {"name": "Spike", "score": 100},
]

# 新增一条学生数据（列表是可变对象，函数内修改会影响外部）
def add_student(name:str,score:int):
    students.append({"name":name,"score":score})
    print(students)

 # 按姓名遍历查找，找到后修改分数并返回 True；找不到返回 False
def find_student(name:str,new_score:int):
    for student in students:
        if student["name"] == name:
            student["score"] = new_score
            print(students)
            return True

        return False
find_student("Tom",60)


# 平均分：sum + 生成器表达式

def adv_student():
    sum_score = 0.00
    for s in students:
        sum_score += s["score"]
        adv = sum_score / len(students)
    return adv


print(adv_student())

# 及格名单：列表推导式
pass_names = [s["name"] for s in students if s["score"] >= 60]
print(pass_names)

# 分组：字典的setdefault 经典用法
group = {}
for s in students:
    key = "pass" if s["score"] >= 60 else "fail"
    group.setdefault(key, []).append(s["name"])

print(group)

