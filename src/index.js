import Vue from 'vue';
import App from './App.vue'
import Chart from './components/Chart.vue';
import vueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
Vue.use(vueMaterial);
new Vue({
    el: "#app",
    template: "<App/>",
    components: { App }
})