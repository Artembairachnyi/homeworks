random_string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
no_equals = random_string.replace('=', ":").replace('sssss', "" ).replace('&', " ").replace('Amanda:', ' Amanda,').replace('32',' 32,').replace('1500','1500,')


print(no_equals)
print ("name: Amanda, age: 32, salary: 1500, currency: quro")

