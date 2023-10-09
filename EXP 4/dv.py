import sys

# Initialize the network topology
network = {
    'A': {'A': 0, 'B': 1, 'C': sys.maxsize, 'D': sys.maxsize},
    'B': {'A': 1, 'B': 0, 'C': 5, 'D': sys.maxsize},
    'C': {'A': sys.maxsize, 'B': 5, 'C': 0, 'D': 2},
    'D': {'A': sys.maxsize, 'B': sys.maxsize, 'C': 2, 'D': 0}
}

# Function to perform the Bellman-Ford algorithm
def bellman_ford(network):
    nodes = list(network.keys())
    num_nodes = len(nodes)

    for _ in range(num_nodes):
        for node in nodes:
            for neighbor in nodes:
                for dest in nodes:
                    if network[node][neighbor] + network[neighbor][dest] < network[node][dest]:
                        network[node][dest] = network[node][neighbor] + network[neighbor][dest]

# Function to print the distance matrix
def print_distance_matrix(network, label):
    print(f"\n{label} Distance Matrix:")
    nodes = list(network.keys())
    print("\t" + "\t".join(nodes))
    for node in nodes:
        row = [str(network[node][dest]) if network[node][dest] != sys.maxsize else '∞' for dest in nodes]
        print(f"{node}\t" + "\t".join(row))

# Make a copy of the initial network
initial_network = {node: {dest: cost for dest, cost in table.items()} for node, table in network.items()}

# Perform the Bellman-Ford algorithm
bellman_ford(network)

# Print the initial distance matrix
print_distance_matrix(initial_network, "Initial")

# Print the final distance matrix
print_distance_matrix(network, "Final")
