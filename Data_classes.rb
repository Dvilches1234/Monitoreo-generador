
#Aquí están todas las clases relacionadas con almacenar datos

class Data                                 #clase madre de los datos
  attr_reader :date, :value
  def initialize(date, value)
    @date = date
    @value = value
  end
end

class UnicData < Data           #clase para datos
  attr_reader :hour             #de una medición única
  def initialize(hour)
    @hour = hour
  end
end

class DailyData < Data                                        #clase para guardar datos
  attr_reader :amount, :min_value, :avg_value, :max_value     #de las mediciones de un día
  def initialize(amount, min_value, avg_value, max_value )
    @amount = amount
    @min_value = min_value
    @avg_value = avg_value
    @max_value = max_value
  end
end
###############

class DayMed                  #clase madre para guardar datos
  attr_reader :day_data
  def initialize(day_data)
    @day_data = day_data[]
  end
end

class WindSpeed < DayMed          #clase para guardar velocidades del viento
  attr_reader :limit              #en un día
  def initialize(limit)
    @limit = limit
  end

  def graph()
      ###función para graficar
  end
end

class Rpm < DayMed
  attr_reader :wind, :rpm_spect
  def initialize(wind, rpm_spect)
    @wind = wind
    @rpm_spect = rpm_spect []
  end

  def graph()
  end

end

class WindDirection < DayMed
  def show()
    #muestra las direcciones según las mediciones
  end
end

class Flow < DayMed
  attr_reader :low, :high
  def initialize(low, high)
    @low = low
    @high = high
  end

  def graph ()
  end
end
####

class GroupMed                        #clase para guardar datos de últimos x días
  attr_reader :group_data, :days
  def initialize (group_data, days)
    @group_data = group_data
    @days = days
  end
end
