import Vue from 'vue';
import App from './App.vue'
import vueMaterial from 'vue-material';
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'
import Mathjax from 'mathjax'
Vue.config.productionTip = false
Vue.use(vueMaterial);
new Vue({
    el: "#app",
    template: "<App/>",
    components: { App }
})