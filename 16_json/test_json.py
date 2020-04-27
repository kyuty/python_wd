import demjson
import json

# From Python to JSON
a = demjson.encode(['one', 42, True, None])
print("a =", a)
# a = "asdfasd" # 不是json格式的也ok, 所以可以理解为这个 demjson 简单理解为可以储存读取文件

json = json.dumps(a)
print("json =", json)


# From JSON to Python
b = demjson.decode('["one",42,true,null]')
print("b =", b)

# 将a对象，写到 a.json 文件中
demjson.encode_to_file("a.json", a, overwrite=True)

# 从 b.json 文件中 读取数据
decode_b = demjson.decode_file("a.json")
print("decode_b =", decode_b)
