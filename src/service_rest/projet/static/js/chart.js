// Initialize the chart
const ctx = document.getElementById('realtime-chart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Real-Time Data',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1,
      data: [],
    }],
  },
  options: {
    scales: {
      x: {
        type: 'linear',
        position: 'bottom',
      },
      y: {
        beginAtZero: true,
      },
    },
  },
});

// Function to update the chart in real-time
function updateChart() {
  // Generate new data (e.g., random values)
  const randomValue = Math.random() * 100;

  // Add the new data point to the chart
  chart.data.labels.push(chart.data.labels.length + 1);
  chart.data.datasets[0].data.push(randomValue);

  // Limit the number of data points displayed (e.g., show the last 10)
  if (chart.data.labels.length > 10) {
    chart.data.labels.shift();
    chart.data.datasets[0].data.shift();
  }

  // Update the chart
  chart.update();
}

// Update the chart every second (adjust the interval as needed)
setInterval(updateChart, 1000);
