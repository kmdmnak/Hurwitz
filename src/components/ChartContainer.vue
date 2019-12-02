<template>
  <div>
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
            position: "bottom"
          }
        ]
      }
    }
  })
};
</script>

