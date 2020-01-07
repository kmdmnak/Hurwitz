<template>
  <div id="display">
    <div v-if="isHurwitzStable!==null">
      <h1 v-if="isHurwitzStable" v-bind:style="{color:'blue'}">This polynomial is Hurwitz Stable</h1>
      <h1 v-else v-bind:style="{color:'red'}">This polynomial is not Hurwitz Stable</h1>
    </div>
    <div v-if="formula!==null">
      <vue-mathjax :formula="formula" :safe="false"></vue-mathjax>
    </div>
  </div>
</template>

<style scoped>
#display {
  height: 15%;
  margin-top: 20px;
  text-align: center;
}
</style>

<script>
import { VueMathjax } from "vue-mathjax";
export default {
  props: ["coefficients", "isHurwitzStable"],
  components: {
    "vue-mathjax": VueMathjax
  },
  computed: {
    formula: function() {
      console.log("in formula");
      if (!this.coefficients) {
        return null;
      }
      let formula_sentence = "$$";
      formula_sentence += String(this.coefficients[0]);
      let i = 1;
      this.coefficients.slice(1).forEach(each_coefficient => {
        formula_sentence += "+" + String(each_coefficient) + "s^" + String(i);
        i++;
      });
      formula_sentence += "$$";
      return formula_sentence;
    }
  }
};
</script>
