import Vue from 'vue';
import App from './App.vue'
import Chart from './components/Chart.vue';

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
})
