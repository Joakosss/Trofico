async function fetchData() {
    const response = await fetch("http://127.0.0.1:8000/get_grafico/");
    const data = await response.json();
    return data;
}

async function renderChart() {
    const data = await fetchData();
    const ctx = document.getElementById('chart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: data,
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'category',
                    labels: data.labels
                },
                y: {
                    type: 'linear'
                }
            }
        }
    });
}

window.onload = renderChart;