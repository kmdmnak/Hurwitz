<template>
  <div class="chart-container">
    <scatter-chart :chartdata="chartData" :options="options" />
  </div>
</template>

<script>
import ScatterChart from "./Chart.vue";

export default {
  name: "chart",
  components: {
    ScatterChart
  },
  props: ["chartData"],
  data: () => ({
    loaded: false,
    options: {
      scales: {
        xAxes: [
          {
            type: "linear",
          }
        ],
        yAxes: [
        ]
      }
    },
    data: {
      datasets: [
        {
          label: "Scatter Dataset",
          data: [{ x: 1, y: -4.5 }, { x: 3, y: 2.2 }]
        }
      ]
    }
  })
};
</script>
