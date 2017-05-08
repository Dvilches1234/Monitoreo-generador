load 'get_data.rb'

puts "¡Bienvenido al sistema de monitoreo del generador eolico"
puts "Elija una opcion"
puts "1) Ver mediciones existentes    2) Hacer medición de manual   3) Automatizar mediciones"
option = gets.chomp().to_i

if option == 1
  puts "Elija una opcion"
  puts "1) Ver mediciones del dia     2) Ver mediciones de los ultimos dias"
  option = gets.chomp().to_i
  if option == 1
      puts "Elija los datos que desea desplegar"
      puts "1) Direccion del viento    2) Velocidad del viento    3) Revoluciones por minuto    4) Corriente generada"
      option = gets.chomp().to_i
      if option == 1
        direction = read_wind_direction()
        direction.show()
      elsif option == 2
        speed = read_wind_speed()
        speed.show()
      elsif option == 3
        rpm = read_rpm()
        rpm.show()
      elsif option == 4
        flow = read_flow()
        flow.show
      else
        puts "por favor ingrese una opcion valida"
      end
  elsif option == 2
    puts "Estamos trabajando para usted"
  else
    puts "por favor ingrese una opcion valida"
  end
elsif option == 2
  puts "Estamos trabajando para usted"
elsif option == 3
  puts "Estamos trabajando para usted"
else
  puts "Por favor, ingrese una opcion valida"
end
