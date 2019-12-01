
<template>
  <div id="sidevar">
    <div>
      <li v-for="coef in coefficients" v-bind:key="coef.name">{{coef.name}}:{{coef.value}}</li>
    </div>
    <div id="coef-buttons">
      <button v-on:click="message('Plus!')">plus</button>
      <button v-on:click="message('minus')">minus</button>
    </div>
    <div id="execution"></div>
  </div>
</template>

<script>
export default {
  name: "sidebar",
  methods: {
    message: function() {
      this.coefficients.push({
        name: "1",
        value: null
      });
    }
  },
  data() {
    return {
      coefficients: [{ name: "constant", value: null }]
    };
  }
};
</script>