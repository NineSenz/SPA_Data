<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <x-chart :id="id" :option="option"></x-chart>
    <Person />
  </div>
</template>

<script>
import Person from './components/Person.vue'
import XChart from './components/Charts.vue'

import options from './charts-options/options'
export default {
  name: 'App',
  data() {
    let option = options.bar
    return {
      id: 'test',
      option: option
    }
  },
  components: {
    Person,
    XChart
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
