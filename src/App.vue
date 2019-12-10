
<template>
  <div>
    <link
      rel="stylesheet"
      href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
    />
    <div id="content">
      <div class="chart-container">
        <chart :chartData="chartData" />
      </div>
      <div class="sidebar">
        <sidebar
        @changeChartData="changeChartData" 
        @changeCoefficient="changeCoefficient"
        />
      </div>
      <div class="display">
        <display :coefficients="coefficients"/>
      </div>
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
    changeChartData: function(newData) {
      // make chartData
      const pointBackgroundColor = newData.map(each_data => {
        return each_data.x > 0 ? "#ff0000" : "#0000ff";
      });
      this.chartData = {
        datasets: [
          {
            label: "Scatter Dataset",
            data: newData,
            pointBackgroundColor: pointBackgroundColor
          }
        ]
      };
      console.log("in change chart data");
      console.log(this.chartData);
    },
    changeCoefficient:function(newCoefficient){
      this.coefficients=newCoefficient;
    }
  },
  data: function() {
    return {
      chartData: null,
      coefficients:null
    };
  }
};
</script>

<style scoped>
.chart-container {
  padding: 30px;
  width: 500px;
  height: 500px;
  float: left;
}
#content {
  position: relative;
}
.sidebar {
  float: left;
  width: 150px;
  margin: 20px;
}
</style>