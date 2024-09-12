from faker import Faker

fake = Faker('zh_CN')
print(fake.name())#随机生成姓名
print(fake.address())#随机生成地址
print(fake.phone_number())#随机生成电话号码
print(fake.pystr())#随机生成字符串
print(fake.email())#随机生成邮箱地址