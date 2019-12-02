
<template>
  <div id="sidevar">
    <div id="coef-buttons">
      <button v-on:click="push">add</button>
      <button v-on:click="pop_coef">delete</button>
      <button v-on:click="hurwitz">execute</button>
    </div>
    <div id="execution"></div>
    <div
      is="coefficient-input"
      v-for="coef in coefficients"
      v-bind:key="coef.name"
      v-bind:label="coef.name"
      v-bind:coefficient="coef.value"
      v-bind:index="coef.index"
      @input="updatedInput"
    ></div>
    <button v-on:click="check">check</button>
  </div>
</template>

<script>
import CoefficientInput from "./CoefficientInput";
export default {
  name: "sidebar",
  methods: {
    push: function() {
      this.coefficients.push({
        name: String(this.coefficients.length) + "-th coefficient",
        value: null,
        index: this.coefficients.length
      });
    },
    pop_coef: function() {
      if (this.coefficients.length == 1) {
        return;
      }
      this.coefficients.pop();
    },
    check: function() {
      console.log(this.coefficients);
    },
    updatedInput(index, newValue) {
      console.log(index, newValue);
      this.coefficients[Number(index)].value = Number(newValue);
    },
    hurwitz: async function() {
      // make data for api
      const coefficient_values = this.coefficients.map(
        each_element => each_element.value
      ).reverse();
      console.log("in hurwitz")
      console.log(coefficient_values)
      const result = await fetch("/hurwitz", {
        method: "POST",
        body: JSON.stringify({
          coefficients: coefficient_values
        })
      }).then((res)=>res.json());
      console.log(result);
      const roots=result.roots
      if(!roots){
        return;
      }
      
    }
  },
  data() {
    return {
      coefficients: [{ name: "constant", value: null, index: 0 }]
    };
  },
  components: {
    "coefficient-input": CoefficientInput
  }
};
</script>