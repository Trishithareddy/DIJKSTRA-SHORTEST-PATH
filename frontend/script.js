document.getElementById('runAlgorithm').addEventListener('click', async function () {
    const graphInput = document.getElementById('graphInput').value;
    const sourceInput = document.getElementById('sourceInput').value;

    try {
        // Parse the graph input from the user
        const graph = JSON.parse(graphInput);

        // Make a POST request to the backend
        const response = await fetch('http://127.0.0.1:5001/shortest-path', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ graph: graph, source: sourceInput }),
        });

        // Check for response errors
        if (!response.ok) {
            const errorMessage = await response.text();
            throw new Error(errorMessage);
        }

        // Get the result and display it
        const result = await response.json();
        document.getElementById('output').textContent = JSON.stringify(result, null, 2);
    } catch (error) {
        console.error(error);
        document.getElementById('output').textContent = 'Error: ' + error.message;
    }
});
