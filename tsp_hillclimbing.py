import sys
from copy import copy
from math import radians, cos, sin, atan2, sqrt
import random as rnd

class City():
        
        EARTH_EQUATORIAL_RADIUS = 6378.1370
        CONVERT_KM_TO_MILES = 0.621371
        def __init__(self, name, latitude, longtitude):
            self._name = name
            self._latitude = radians(latitude)
            self._longtitude = radians(longtitude)
        def measure_distance(self, city):
            deltaLongtitude = city._longtitude - self._longtitude
            deltaLatitude = city._latitude - self._latitude
            a = sin(deltaLatitude / 2) ** 2 + cos(self._latitude) * cos(city._latitude) * sin(deltaLongtitude / 2) ** 2
            return City.CONVERT_KM_TO_MILES * City.EARTH_EQUATORIAL_RADIUS * 2 * atan2(sqrt(a), sqrt(1 - a))
        def get_name(self): return self._name
        def get_latitude(self): return self._latitude
        def get_longtitude(self): return self._longtitude
        def __repr__(self): return self._name
        def __str__(self): return self._name
        def __eq__(self, o: object): 
            returnFlag = False
            if isinstance(o, City):
                if o._name == self._name and o._longtitude == self._latitude and o._longtitude == self._longtitude:
                     returnFlag = True
                return returnFlag
        def __hash__(self): return hash((self._name, self._latitude, self._longtitude))
class Route():
     def __init__(self, cities):
          self._cities = copy(cities)
     def calculate_total_distance(self):
          totalDistance = 0
          for i in range(0, len(self._cities)-1):
               totalDistance = self._cities[i].measure_distance(self._cities[i+1]) + totalDistance
          totalDistance = self._cities[0].measure_distance(self._cities[len(self._cities)-1]) + totalDistance
          return totalDistance
     def get_cities(self): return self._cities
     def __repr__(self): return str(self._cities)
     def __str__(self): return str(self._cities)
class HillClimbing():
     ITERATIONS_BEFORE_MAXIMA = 100
     def find_shortest_route(Self, currentRoute:Route):
         adjacentRoute: Route
         iterToMaximaCounter = 0
         compareRoutes = None
         while (iterToMaximaCounter < HillClimbing.ITERATIONS_BEFORE_MAXIMA):
             adjacentRoute = self.obtain_adjacent_route(Route(currentRoute.get_cities()))
             if (round(adjacentRoute.calculate_total_distance()) <= round(currentRoute.calculate_total_distance())):
                compareRoutes = "<= (proceed)"
                iterToMaximaCounter = 0
                currentRoute =Route(adjacentRoute.get_cities())
             else:
                compareRoutes = "> (stay) - iteration # " + str(iterToMaximaCounter)
                iterToMaximaCounter = iterToMaximaCounter + 1
             print("           | "+ compareRoutes)
             sys.stdout.write(str(currentRoute.get_cities()) +"  |      "+str("{:14.5f}".format(currentRoute.calculate_total_distance())))
         if  (iterToMaximaCounter == 100): print("      | potential maxima")
         else: print("            | " + compareRoutes)
         return currentRoute
     def obtain_adjacent_route(self, route):
          x1 = 0; x2 = 0
          while (x1 == x2):
               x1 = (int) (len(route.get_cities()) * rnd.random())
               x2 = (int) (len(route.get_cities()) * rnd.random())
          city1 = route.get_cities()[x1]
          city2 = route.get_cities()[x2]
          route.get_cities()[x1] = city2
          route.get_cities()[x2] = city1               
class Data():
    USCities = [
        City("Boston", 42.3601, -71.0589),
        City("San Francisco", 37.7749, -122.4194),
        City("New York", 40.7128, -74.0059),
        City("Houston", 29.7604, -95.3698),
        City("Denver", 39.7392, -104.9903),
        City("Los Angeles", 34.0522, -118.2437),
        City("Chicago", 41.8781, -87.6298),
        City("Austin", 30.2672, -97.7431)],
        City("Dallas", 32.7767, -96.7970),
        City("Seattle", 47.6062, -122.3321)]

    
   
    
    
    
    
  
    
    
        

   
        





               
def find_tsp_solution(data): 
    route = Route(data)
    formatedRouteStr = "{:^" + str(len(str(data))) + "}"
    print(str(formatedRouteStr.format("Route")) + "  | distance (in miles)  | compare adjacent to current route")
    print("--------------------------------------------------------------------------------------------------------")       
    sys.stdout.write(str(route.get_cities()) + "  |      " + str("{:14.5f}".format(route.calculate_total_distance())))
    HillClimbing().find_shortest_route(route)
find_tsp_solution(Data.USCities)
       


      
            


