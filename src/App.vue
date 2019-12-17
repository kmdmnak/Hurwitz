
<template>
  <div>
    <link
      rel="stylesheet"
      href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
    />
    <div id="content">
      <display :coefficients="coefficients" :isHurwitzStable="isHurwitzStable" />
      <div id="chart-sidebar">
        <chart :chartData="chartData" />
        <sidebar @changeChartData="changeChartData" @changeCoefficient="changeCoefficient" />
      </div>
    </div>
  </div>
</template>

<script>
import ChartConteinar from "./components/ChartContainer.vue";
import Sidebar from "./components/Sidebar";
import Display from "./components/Display";
console.log("In app")
export default {
  components: {
    chart: ChartConteinar,
    sidebar: Sidebar,
    display: Display
  },
  methods: {
    changeChartData: function(api_response) {
      // make chartData
      const newData = api_response.roots;
      const pointBackgroundColor = newData.map(each_data => {
        return each_data.x > 0 ? "#ff0000" : "#0000ff";
      });
      this.chartData = {
        datasets: [
          {
            data: newData,
            pointBackgroundColor: pointBackgroundColor
          }
        ]
      };
      this.isHurwitzStable = api_response.hurwitz_test;
      console.log("in change chart data");
      console.log(this.chartData);
    },
    changeCoefficient: function(newCoefficient) {
      this.coefficients = newCoefficient;
    }
  },
  data: function() {
    return {
      chartData: null,
      coefficients: null,
      isHurwitzStable: null
    };
  }
};
</script>

<style>
body {
  width: 100%;
  height: 100%;
}
#content {
  /*position: relative;*/
  width: 100%;
  height: 100%;
}
#chart-sidebar {
  height: 80%
}
</style>