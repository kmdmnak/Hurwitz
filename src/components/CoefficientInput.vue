<template>
  <span class="coefficient-input">
    <md-field>
      <label>{{label}}</label>
      <md-input :value="coefficient" v-model="value" @input="$emit('input',index, value)"></md-input>
    </md-field>
  </span>
</template>

<script>
export default {
  name: "coefficient-input",
  props: ["label", "coefficient", "index"],
  data: function() {
    return {
      value: null,
      type: null,
      withLabel: null,
      inline: null,
      number: null,
      textarea: null,
      autogrow: null,
      disabled: null
    };
  }
};
</script>

<style scoped>
.coefficient-input {
  height: 10px;
  /*margin: 10px;*/
}
</style>