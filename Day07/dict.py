# [], {}, {}

# dict: key[str,int] and 중복안됨 - value: anyType
lecture = {
    "java": 1,
    "python": 2,
    "c": 3,
    "javascript":4,
}
print(lecture["python"])

coffeShopMenu= {
    "starbucks":[{"name":"아메리카노"},{"name":"라떼"}],
    "megacoffe":[{"name":"메가리카노","price":2000},{"name":"메가라떼","price":3000}],
}
print(coffeShopMenu["megacoffe"])