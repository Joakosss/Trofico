async function fetchData() {
    const response = await fetch("https://trofico.onrender.com/get_grafico/");
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
                    type: 'linear',
                    min:0,
                    max:100,
                }
            }
        }
    });
}

window.onload = renderChart;