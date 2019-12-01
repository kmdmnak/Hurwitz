<template>
  <div>
    <p>{{test}}</p>
    <chart />
    <sidebar/>
  </div>
</template>

<script>
import Chart from "./components/Chart";
import Sidebar from './components/Sidebar'
export default {
  data() {
    return {
      test: "Hello Vue!!"
    };
  },
  components: {
    'chart':Chart,
    'sidebar':Sidebar
  }
};
</script>
