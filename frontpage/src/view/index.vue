<template>
  <div id="app">
    <el-container>
      <el-header>
        <el-menu
            class="el-menu-demo"
            mode="horizontal"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b">
          >
          <el-menu-item index="1">动态图表</el-menu-item>
          <el-menu-item index="2">数据显示</el-menu-item>
        </el-menu>
      </el-header>
      <el-main>
        <img alt="Vue logo" src="../assets/logo.png">
        <x-chart :id="id" :option="option"></x-chart>
        <Person />
      </el-main>
    </el-container>
    <el-footer>Footer</el-footer>
  </div>
</template>

<script>
import Person from '../components/Person.vue'
import XChart from '../components/Charts.vue'

import options from '../charts-options/options'
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
}

.el-header, .el-footer {
  padding: 0 0;
  background-color: #545c64;
  color: #333;
  text-align: center;
  line-height: 60px;
}
</style>
