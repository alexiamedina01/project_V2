# TODO document
from final_project.city import City
area_rates = {
    0: (100,200),
    1: (50, 250),
    2: (250,350),
    3: (150,450),
}
city = City(size = 10, area_rates = area_rates)
city.initialize()
# TODO iterations
# TODO requested graph
# plt.savefig('reports/graph1.png')
# TODO proposed graph

# plt.savefig('reports/graph2.png')

print('current iteration:', city.step)
# exploring a place in the city
my_place = city.places[25]
my_place.place_id
my_place.host_id
my_place.neighbours
my_place.area
# exploring a host of the city
my_host = city.hosts[25]
my_host.profits
my_host.area
my_host.assets
