
<template>
  <span id="sidebar">
    <div id="coef-buttons">
      <button v-on:click="push">add</button>
      <button v-on:click="pop_coef">delete</button>
      <button v-on:click="hurwitz">execute</button>
    </div>
    <div id="execution"></div>
    <!--<draggable v-model="coefficients" @end="onEnd">-->
      <div
        is="coefficient-input"
        v-for="coef in coefficients"
        v-bind:key="coef.id"
        v-bind:label="coef.name"
        v-bind:coefficient="coef.value"
        v-bind:index="coef.index"
        @input="updatedInput"
      ></div>
    <!--</draggable>-->
    <button v-on:click="check">check</button>
  </span>
</template>

<style>
#sidebar {
  display: inline-block;
  width: 20%;
  height: 100%;
  vertical-align: top;
}
</style>

<script>
import CoefficientInput from "./CoefficientInput";
import draggable from "vuedraggable";
export default {
  name: "sidebar",
  methods: {
    push: function() {
      this.coefficients.push({
        name: String(this.coefficients.length) + "-th coefficient",
        value: null,
        index: this.coefficients.length,
        id: this.coefficients.length
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
      const coefficient_values_reversed = this.coefficients
        .map(each_element => each_element.value)
        .reverse();
      // 先頭のnullを取り除く
      const coefficient_values = [];
      coefficient_values_reversed.forEach(v => {
        if (v) {
          coefficient_values.push(v);
        }
      });
      const result = await fetch("/hurwitz", {
        method: "POST",
        body: JSON.stringify({
          coefficients: coefficient_values
        })
      }).then(res => res.json());

      const roots = result.roots;
      if (!roots) {
        return;
      }
      this.$emit("changeCoefficient",coefficient_values.reverse());
      this.$emit("changeChartData", result);
    },
    onEnd: function() {
      let i = 0;
      this.coefficients.forEach(each_element => {
        each_element["index"] = i;
        each_element["name"] =
          i !== 0 ? String(i) + "-th coefficient" : "const";
        i++;
      });
    }
  },
  data() {
    return {
      coefficients: [{ name: "constant", value: null, index: 0 }]
    };
  },
  components: {
    "coefficient-input": CoefficientInput,
    draggable
  }
};
</script>