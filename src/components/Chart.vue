<script>
import { Scatter } from "vue-chartjs";

export default {
  extends: Scatter,
  props: {
    chartdata: {
      type: Object,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  computed: {
    data: function() {
      return this.chartdata;
    }
  },
  watch: {
    data: function() {
      //this.renderChart(this.data, this.options);
      this.renderChart(this.data,this.options);
    }
  },
  mounted() {
    this.renderChart(this.data, this.options);
  }
};
</script>