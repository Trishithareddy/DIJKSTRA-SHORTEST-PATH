from flask import Flask, request, jsonify
from flask_cors import CORS
import heapq  # For priority queue

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

# Function to implement Dijkstra's algorithm
def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}  # Set all distances to infinity
    distances[source] = 0  # Distance to the source is 0
    priority_queue = [(0, source)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the distance is greater than the recorded distance, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# API route to handle the shortest path request
@app.route('/shortest-path', methods=['POST'])
def shortest_path():
    data = request.get_json()

    graph = data.get('graph')
    source = data.get('source')

    if not graph or source not in graph:
        return jsonify({"error": "Invalid input"}), 400

    result = dijkstra(graph, source)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
