
#Aquí están todas las clases relacionadas con almacenar datos

class NormalData                                 #clase madre de los datos
  attr_reader :date, :value
  def initialize(date, value)
    @date = date
    @value = value
  end
end

class UnicData < NormalData           #clase para datos
  attr_reader :hour             #de una medición única
  def initialize(date, value, hour)
    super(date, value)
    @hour = hour
  end
end

class DailyData < NormalData                                        #clase para guardar datos
  attr_reader :amount, :min_value, :avg_value, :max_value     #de las mediciones de un día
  def initialize(date, amount, min_value, avg_value, max_value )
    super(date)
    @amount = amount
    @min_value = min_value
    @avg_value = avg_value
    @max_value = max_value
  end
end
###############

class DayMed                  #clase madre para guardar datos
  attr_reader :day_data
  def initialize(day_data = [])
    @day_data = day_data
  end
end

class WindSpeed < DayMed          #clase para guardar velocidades del viento
  attr_reader :limit              #en un día
  def initialize(day_data, limit)
    super(day_data)
    @limit = limit
  end
  def show()
    puts "Day     | Hour   | Wind speed(km/h)  | Limit"
    puts "----------------------------"
    for i in 0...@day_data.length
      puts "#{@day_data[i].date}    | #{@day_data[i].hour}    | #{@day_data[i].value}      | #{@limit}"
    end
  end
  def graph()
      ###función para graficar
  end
end

class Rpm < DayMed
  attr_reader :wind, :rpm_spect
  def initialize(day_data, wind)
    super(day_data)
    @wind = wind
    @rpm_spect = []
    for i in 0...@day_data.length
      @rpm_spect.insert(i, wind[i].value/10)
    end
  end
  def show()
        puts "Day     | Hour   | RPM  | RPM spected"
        for i in 0...@day_data.length
          puts "#{@day_data[i].date} | #{@day_data[i].hour}   | #{@day_data[i].value}   | #{@rpm_spect[i]}"
        end
  end
  def graph()
  end
end

class WindDirection < DayMed
  def initialize(day_data)
    super
  end
  def show()
    puts "Day     | Hour   |  Wind direction"
    for i in 0...@day_data.length
      puts "#{@day_data[i].date} | #{@day_data[i].hour}   | #{@day_data[i].value} "
    end
  end
end

class Flow < DayMed
  attr_reader :low, :high
  def initialize(day_data,low, high)
    super(day_data)
    @low = low
    @high = high
  end
  def show()
    puts "Day     | Hour   |  Flow(amps)  | Minimun flow(amps)   |  Maximun flow(amps)"
    for i in 0...@day_data.length
      puts "#{@day_data[i].date}  |   #{@day_data[i].hour}   | #{@day_data[i].value}  | #{@low}   | #{@high} "
    end
  end
  def graph ()
  end
end


####

class GroupMed                        #clase para guardar datos de últimos x días
  attr_reader :group_data, :days
  def initialize (group_data = [], days)
    @group_data = group_data
    @days = days
  end
end
