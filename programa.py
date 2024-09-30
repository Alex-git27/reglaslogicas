import heapq  # Importamos la biblioteca heapq que nos permitirá usar una cola de prioridad para el algoritmo de Dijkstra

# Introducimos la clase que representa el sistema de transporte del Metro de Medellín
class MetroMedellin:
    def __init__(self):
        # Inicializamos un grafo  para representar las estaciones y las rutas
        # Cada nodo es una estación y tiene una lista de vecinos con el peso (distancia o tiempo entre ellos)
        self.grafo = {}

    # Método para agregar una ruta entre dos estaciones
    def agregar_ruta(self, origen, destino, peso):
        # Si la estación de origen no está en el grafo, la agregamos
        if origen not in self.grafo:
            self.grafo[origen] = []
        # Si la estación de destino no está en el grafo, la agregamos
        if destino not in self.grafo:
            self.grafo[destino] = []
        # Añadimos la ruta de ida desde origen a destino con el peso (distancia o tiempo)
        self.grafo[origen].append((destino, peso))
        # Añadimos la ruta de vuelta desde destino a origen con el mismo peso
        self.grafo[destino].append((origen, peso))

    #  Encontramos la ruta más corta entre dos estaciones usando el algoritmo de Dijkstra
    def encontrar_ruta_mas_corta(self, inicio, destino):
        # Cola de prioridad que almacenará los nodos por explorar, empezando desde la estación inicial
        cola_prioridad = [(0, inicio)]  # El formato es (distancia acumulada, nodo actual)
        # Diccionario para almacenar las distancias mínimas desde la estación de inicio a todas las demás estaciones
        distancias = {nodo: float('inf') for nodo in self.grafo}  # Inicializamos todas las distancias como "infinito"
        distancias[inicio] = 0  # La distancia a la estación de inicio es 0
        # Diccionario para almacenar el camino más corto previo a cada estación
        camino_previo = {nodo: None for nodo in self.grafo}

        # Mientras haya nodos por explorar
        while cola_prioridad:
            # Sacamos el nodo con la distancia más baja (esto es lo que hace Dijkstra eficiente)
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            # Si hemos llegado a la estación destino, podemos salir del bucle
            if nodo_actual == destino:
                break

            # Recorremos todas las estaciones vecinas (adyacentes) al nodo actual
            for vecino, peso in self.grafo[nodo_actual]:
                # Calculamos la distancia desde el nodo actual hasta este vecino
                distancia = distancia_actual + peso
                # Si encontramos una distancia más corta para llegar a este vecino, la actualizamos
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    camino_previo[vecino] = nodo_actual  # Guardamos el nodo anterior en el camino
                    # Añadimos el vecino a la cola de prioridad para seguir explorando
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        # Reconstruimos el camino desde la estación destino hasta la estación de inicio
        ruta = []
        nodo = destino
        while nodo is not None:
            ruta.append(nodo)  # Añadimos cada nodo al camino
            nodo = camino_previo[nodo]  # Seguimos el rastro de nodos previos

        ruta.reverse()  # Invertimos la lista para obtener el camino en el orden correcto
        return ruta, distancias[destino]  # Devolvemos el camino más corto y la distancia total

# Cremaos el sistema de transporte del Metro de Medellín
metro = MetroMedellin()

# Agregamos rutas representando sitios turísticos de Medellín (nodos y aristas con pesos, para que tengamos
# en cuenta , los pesos pueden representar distancias o tiempos de viaje en minutos entre los sitios
metro.agregar_ruta("Parque Explora", "Jardín Botánico", 5)
metro.agregar_ruta("Jardín Botánico", "Parque de los Deseos", 2)
metro.agregar_ruta("Parque Explora", "Parque Arví", 30)
metro.agregar_ruta("Parque Arví", "Pueblito Paisa", 40)
metro.agregar_ruta("Pueblito Paisa", "Museo de Antioquia", 15)
metro.agregar_ruta("Museo de Antioquia", "Plaza Botero", 1)
metro.agregar_ruta("Plaza Botero", "Jardín Botánico", 20)

# ahora escribimos la linea de codigo donde encontramos la mejor ruta entre dos sitios turísticos
# Ejemplo: encontrar la ruta desde el "Parque Explora" hasta el "Museo de Antioquia"
ruta, distancia = metro.encontrar_ruta_mas_corta("Parque Explora", "Museo de Antioquia")
print(f"La mejor ruta es: {ruta} con una distancia total de {distancia} minutos.")
