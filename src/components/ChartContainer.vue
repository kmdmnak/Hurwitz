<template>
  <span id="chart-container">
    <scatter-chart :chartdata="chartData" :options="options" />
  </span>
</template>

<style scoped>
#chart-container {
  padding: 10px;
  width: 400px;
  height: 400px;
  float: left;
  text-align: center;
}
</style>

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
      legend: {
        //凡例設定
        display: false //表示設定
      },
      title: {
        display: false //表示設定
      },
      scales: {
        xAxes: [
          {
            type: "linear",
            scaleLabel: {
              display: true,
              labelString: "real"
            }
          }
        ],
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "image"
            }
          }
        ]
      }
    },
    data: {
      datasets: [
        {
          data: [{ x: 1, y: -4.5 }, { x: 3, y: 2.2 }]
        }
      ]
    }
  })
};
</script>
