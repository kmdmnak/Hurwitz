<template>
  <vue-mathjax :formula="formula" :safe="false"></vue-mathjax>
</template>

<script>
import { VueMathjax } from 'vue-mathjax'
export default {
  props: ["coefficients"],
  components:{
    'vue-mathjax': VueMathjax
  },
  computed: {
    formula: function() {
      console.log("in formula");
      if (!this.coefficients) {
        return;
      }
      let formula_sentence = '$$';
      formula_sentence += String(this.coefficients[0].value);
      let i = 1;
      this.coefficients.slice(1).forEach(each_coefficient => {
        formula_sentence += '+' + String(each_coefficient.value) + 's^' + String(i);
        i++;
      });
      formula_sentence += '$$';
      return formula_sentence;
    }
  }
};
</script>
