<template>
  <md-list-item>
    <md-field>
      <md-input v-model="coefficient"></md-input>
      <label>{{name}}+th-coefficient</label>
    </md-field>
  </md-list-item>
</template>

<script>
export default {
  name: "coefficient-input",
  props: ["name"],
  data: function() {
    return {
      coefficient: 0
    };
  }
};
</script>