import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Person from '@/components/Person'
import Chart from '@/components/Chart'
Vue.use(Router)
export default new Router({
    routes: [
        {
            path: '/person',
            name: 'Person',
            component: Person
        },
        {
            path: '/chart',
            name: 'Chart',
            component: Chart
        }
    ]
})
