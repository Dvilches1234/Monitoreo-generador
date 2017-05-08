load 'data_classes.rb'

def read_wind_speed()
  arr_wind = []
  File.open("info/wind_speed.txt").each do |line|
    parameters = line.split
    data_wind = UnicData.new(parameters[0], parameters[1], parameters[2] )
    arr_wind.insert(arr_wind.length, data_wind)
  end
  final_speed = WindSpeed.new(arr_wind, 90)
  return final_speed
end
#Esta funcion lee el archivo y creo un objeto WindSpeed
#
#
#

def read_wind_direction()
  arr_wind = []
  File.open("info/wind_direction.txt").each do |line|
    parameters = line.split
    data_wind = UnicData.new(parameters[0], parameters[1], parameters[2] )
    arr_wind.insert(arr_wind.length, data_wind)
  end
  final_direcion = WindDirection.new(arr_wind)
  return final_direcion
end
#
#
#
#
#
def read_flow()
  arr_flow = []
  File.open("info/amps.txt").each do |line|
    parameters = line.split
    data_flow = UnicData.new(parameters[0], parameters[1], parameters[2] )
    arr_flow.insert(arr_flow.length, data_flow)
  end
  final_flow = Flow.new(arr_flow, 4, 15)
  return final_flow
end
#
#
#
#
#
def read_rpm()
  arr_wind = []
  File.open("info/wind_speed.txt").each do |line|
    parameters = line.split
    data_wind = UnicData.new(parameters[0], parameters[1], parameters[2] )
    arr_wind.insert(arr_wind.length, data_wind)
  end
  final_speed = WindSpeed.new(arr_wind, 90)
  arr_rpm = []
  File.open("info/rpm.txt").each do |line|
    parameters = line.split
    data_rpm = UnicData.new(parameters[0], parameters[1], parameters[2] )
    arr_rpm.insert(arr_rpm.length, data_rpm)
  end
  final_rpm = Rpm.new(arr_rpm, final_speed)
  return final_rpm
end
