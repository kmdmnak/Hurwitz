
<template>
  <div>
    <link
      rel="stylesheet"
      href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
    />
    <div id="content">
      <display :coefficients="coefficients" :isHurwitzStable="isHurwitzStable"/>
      <chart :chartData="chartData" />
      <sidebar @changeChartData="changeChartData" @changeCoefficient="changeCoefficient" />
    </div>
  </div>
</template>

<script>
import ChartConteinar from "./components/ChartContainer.vue";
import Sidebar from "./components/Sidebar";
import Display from "./components/Display";

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

<style scoped>
#content {
  /*position: relative;*/
  text-align: center;
}
</style>