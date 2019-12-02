
<template>
  <div>
    <link
      rel="stylesheet"
      href="//fonts.googleapis.com/css?family=Roboto:400,500,700,400italic|Material+Icons"
    />
    <div id="content">
      <div class="chart-container">
        <chart />
      </div>
      <div class="sidebar">
        <sidebar />
      </div>
    </div>
  </div>
</template>

<script>
import ChartConteinar from "./components/ChartContainer.vue";
import Sidebar from "./components/Sidebar";
export default {
  components: {
    chart: ChartConteinar,
    sidebar: Sidebar
  },
  data: function() {
    return {
      chartData: null
    };
  }
};
</script>

<style scoped>
.chart-container {
  width: 300px;
  height: 300px;
  float: left;
}
#content {
  position: relative;
}
.sidebar {
  float: left;
}
</style>