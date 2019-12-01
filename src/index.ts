import Vue from "vue";
import Chart from './component/Chart.vue'
import Sidebar from './components/Sidebar.vue'
import App from "./App.vue";

Vue.component(
    'Chart',
    {
        template:'<Chart/>'
    }
)

new Vue({
  el: "#app",
  template: "<App/>",
  components: { App }
});
