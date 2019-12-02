<template>
  <div>
    <scatter-chart :chartdata="chartdata" :options="options" />
  </div>
</template>

<script>
import ScatterChart from "./Chart.vue";

export default {
  name: "chart",
  components: {
    ScatterChart
  },
  methods:{
    makeData:function(){

    }
  },
  data: () => ({
    loaded: false,
    chartdata: {
      datasets: [
        {
          data: [
            {
              x: -10,
              y: 0
            },
            {
              x: 0,
              y: 10
            },
            {
              x: 10,
              y: 5
            }
          ]
        }
      ]
    },
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

