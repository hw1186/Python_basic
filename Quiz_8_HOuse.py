class House:
    def __init__(self, location, house_type, deal_tyep, price, completion_year):
        self.location = location
        self.house_tyoe = house_type
        self.deal_type = deal_tyep
        self.price = price
        self.completion_year = completion_year


    def show_detail(self):
        print(self.location, self.house_tyoe, self.deal_type, self.price, self.completion_year)

        pass

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("고양", "오피스텔", "전세", "5억", "2002년")
house3 = House("삼송", "아파트", "매매", "7억", "2005년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0} 대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()