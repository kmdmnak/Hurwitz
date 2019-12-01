
<template>
  <div id="sidevar">
    <div id="coef-buttons">
      <button v-on:click="push">add</button>
      <button v-on:click="pop_coef">delete</button>
    </div>
    <div id="execution"></div>
    <div id="coefficient-input">
      <li v-for="coef in coefficients" v-bind:key="coef.name">{{coef.name}}:{{coef.value}}</li>
    </div>
  </div>
</template>

<script>
import { stringify } from 'postcss';
export default {
  name: "sidebar",
  methods: {
    push: function() {
      this.coefficients.unshift({
        name: String(this.coefficients.length-1)+"-th coefficient",
        value: null
      });
    },
    pop_coef:function(){
      if(this.coefficients.length==1){
        return;
      }
      this.coefficients.shift()
    }
  },
  data() {
    return {
      coefficients: [{ name: "constant", value: null }]
    };
  }
};
</script>