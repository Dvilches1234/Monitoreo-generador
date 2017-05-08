load 'data_classes.rb'

dia_1 = UnicData.new("01/02/2017", 48, "17:45")
dia_2 = UnicData.new("02/02/2017", 46, "17:35")
dia_3 = UnicData.new("03/02/2017", 76, "14:45")
dia_4 = UnicData.new("01/02/2017", 90, "17:45")

dias = Array.new()
dias.insert(0,dia_1)
dias.insert(1,dia_2)
dias.insert(2,dia_3)
dias.insert(3,dia_4)
puts dias.length

vientecito = WindSpeed.new(dias, 90)

vientecito.show
