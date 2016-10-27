## CS 2120 Assignment #2 -- Zombie Apocalypse
## Name: PLEASE FILL THIS IN
## Student number: SERIOUSLY
## Worked With:


import numpy


#### This stuff you just have to use, you're not expected to know how it works.
#### You just need to read the plain English function headers.
#### If you want to learn more, by all means follow along (and ask questions if
#### you're curious). But you certainly don't have to.

def make_city(name,neighbours):
    """
    Create a city (implemented as a list).

    :param name: String containing the city name
    :param neighbours: The city's row from an adjacency matrix.

    :return: [name, Infection status (defailt value of False), List of neighbours]
    """

    return [name, False, list(numpy.where(neighbours==1)[0])]


def make_connections(n,density=0.35):
    """
    This function will return a random adjacency matrix of size
    n x n. You read the matrix like this:

    if matrix[2,7] = 1, then cities '2' and '7' are connected.
    if matrix[2,7] = 0, then the cities are _not_ connected.

    :param n: number of cities
    :param density: controls the ratio of 1s to 0s in the matrix

    :returns: an n x n adjacency matrix
    """

    import networkx

    # Generate a random adjacency matrix and use it to build a networkx graph
    a=numpy.int32(numpy.triu((numpy.random.random_sample(size=(n,n))<density)))
    G=networkx.from_numpy_matrix(a)

    # If the network is 'not connected' (i.e., there are isolated nodes)
    # generate a new one. Keep doing this until we get a connected one.
    # Yes, there are more elegant ways to do this, but I'm demonstrating
    # while loops!
    while not networkx.is_connected(G):
        a=numpy.int32(numpy.triu((numpy.random.random_sample(size=(n,n))<density)))
        G=networkx.from_numpy_matrix(a)

    # Cities should be connected to themselves.
    numpy.fill_diagonal(a,1)

    return a + numpy.triu(a,1).T

def set_up_cities(names=['City 0', 'City 1', 'City 2', 'City 3', 'City 4', 'City 5', 'City 6', 'City 7', 'City 8', 'City 9', 'City 10', 'City 11', 'City 12', 'City 13', 'City 14', 'City 15']):
    """
    Set up a collection of cities (world) for our simulator.
    Each city is a 3 element list, and our world will be a list of cities.

    :param names: A list with the names of the cities in the world.

    :return: a list of cities
    """

    # Make an adjacency matrix describing how all the cities are connected.
    con = make_connections(len(names))

    # Add each city to the list
    city_list = []
    for n in enumerate(names):
        """n[0] = 0,1,2,3,4 etc."""
        """n[1] = Name of the city."""
        city_list += [ make_city(n[1],con[n[0]]) ]

    return city_list

def draw_world(world):
    """
    Given a list of cities, produces a nice graph visualization. Infected
    cities are drawn as red nodes, clean cities as blue. Edges are drawn
    between neighbouring cities.

    :param world: a list of cities
    """

    import networkx
    import matplotlib.pyplot as plt

    G = networkx.Graph()

    bluelist=[]
    redlist=[]

    plt.clf()

    # For each city, add a node to the graph and figure out if
    # the node should be red (infected) or blue (not infected)
    for city in enumerate(world):
        if city[1][1] == False:
            G.add_node(city[0])
            bluelist.append(city[0])
        else:
            G.add_node(city[0],node_color='r')
            redlist.append(city[0])

        for neighbour in city[1][2]:
            G.add_edge(city[0],neighbour)

    # Lay out the nodes of the graph
    position = networkx.circular_layout(G)

    # Draw the nodes
    networkx.draw_networkx_nodes(G,position,nodelist=bluelist, node_color="b")
    networkx.draw_networkx_nodes(G,position,nodelist=redlist, node_color="r")

    # Draw the edges and labels
    networkx.draw_networkx_edges(G,position)
    networkx.draw_networkx_labels(G,position)

    # Force Python to display the updated graph
    plt.show()
    plt.draw()

def print_world(world):
    """
    In case the graphics don't work for you, this function will print
    out the current state of the world as text.

    :param world: a list of cities
    """

    import string

    print string.ljust('City',15), 'Zombies?'
    print '------------------------'
    for city in world:
        print string.ljust(city[0],15), city[1]



#### That's the end of the stuff provided for you.
#### Put *your* code after this comment.

def zombify(cities,cityno):
    """
    city[0] = "Name Of the city"
    city[1] = "Is Infected"
    city[2] = "List of the connected cities"

    So if cityno = 2
    Then city = cities[2];
    """
    cities[cityno][1]=True
    return cities

def cure(cities,cityno):
    cities[cityno][1] = False
    return cities

def sim_step(cities,p_spread,p_cure):
    for city in enumerate(cities):
        if city[1][1] == True and numpy.random.rand() < p_spread:
            cities[numpy.random.randint(0,len(cities))][1] = True
        if city[1][1] == True and city[0] !=0 and numpy.random.rand() < p_cure:
            city[1][1] = True
    return cities

def is_end_of_world(cities):
    flag = True
    for city in enumerate(cities):
        if city[1][1] == False:
            flag = False

    return flag

def time_to_end_of_world(p_spread,p_cure):
    my_world = set_up_cities()
    zombify(my_world,0)
    end_of_world_conter = 0
    while(not is_end_of_world(my_world)):
        sim_step(my_world,0.5,0.0)
        end_of_world_conter=end_of_world_conter+1

    return  end_of_world_conter

#def end_world_many_times(n,p_spread,p_cure):


my_world = set_up_cities()
my_world = zombify(my_world,2)

