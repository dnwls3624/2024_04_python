# enumerate: 열거하다
coffees = [{'name':'아메리카노','price':2000},{'name':'라떼','price':2000}]

for index, item in enumerate(coffees):
    print(f"{index}. {item['name']} {item['price']}원")


