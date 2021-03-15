import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home/Home";
import TestCase from "../components/test/TestCase";
import Monitor from "../components/Home/Monitor";
import vueResources from 'vue-resource'
import VueCookies from 'vue-cookies'
import VersionControl from "../components/version/VersionControl";
import Login from "../components/Home/Login";
import project from "../components/system/project"
import SQLParmImport from "../components/tool/SQLParmImport";
Vue.use(VueCookies);
Vue.use(Router)
Vue.use(vueResources)

const router =  new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta:{keepAlive: true}
    },
    {
      path: '/Home',
      name: 'Home',
      component: Home,
      meta:{keepAlive: true}
    },
    {
      path: '/TestCase',
      name: 'TestCase',
      component: TestCase,
      meta: {keepAlive: true}
    },
    {
      path: '/Monitor',
      name: 'Monitor',
      component: Monitor,
      meta: {keepAlive: true}
    },
    {
      path: '/VersionControl',
      name: 'VersionControl',
      component: VersionControl,
      meta: {keepAlive: true}
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: {keepAlive: false}
    },
    {
      path: '/test',
      name: 'Test',
      component: SQLParmImport,
      meta: {keepAlive: false}
    }
  ],
})
// // 导航守卫
// // 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
// router.beforeEach((to, from, next) => {
//   if (to.path === '/login') {
//     next();
//   }
//   else
//     {
//       let token = localStorage.getItem('Authorization');
//       if (token === null || token === '') {
//       next('/login');
//     } else {
//       next();
//     }
//   }
// });

export default router;
