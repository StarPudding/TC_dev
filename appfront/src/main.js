// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import axios from 'axios'
import store from "./store";

import qs from 'qs'
Vue.config.productionTip = false
Vue.use(ElementUI, {size: 'small', zIndex: 3000})
// axios.defaults.headers['Content-Type'] = 'Access-Control-Allow-Origin'
// axios.defaults.baseURL = "http://localhost:8011/"
Vue.prototype.$axios = axios; //全局注册，使用方法为:this.$axios

Vue.config.productionTip = false;
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  store: store,
  template: '<App/>'
})
// 添加请求拦截器，在请求头中加token
axios.interceptors.request.use(
  config => {
    if (localStorage.getItem('Authorization')) {
      config.headers.Authorization = localStorage.getItem('Authorization');
    }

    return config;
  },
  error => {
    return Promise.reject(error);
  });

//http response拦截器
axios.interceptors.response.use(
  response =>{
    let code = response.data.code
    console.log('code:', code)
    if(code === 401)
    {
      localStorage.removeItem('Authorization');
      alert(response.data.message)
      router.replace({
        path: '/login',
        query: {redirect: router.currentRoute.fullPath}
        //登录成功后跳入浏览的当前页面
      })
    }
    return response;
  },
  error=>{
    if(error.response){
      switch(error.response.status){
        case 401:
          localStorage.removeItem('token');
     /*     router.push('/views/login');*/
          router.replace({
            path: '/views/login',
            query: {redirect: router.currentRoute.fullPath}//登录成功后跳入浏览的当前页面
          })
      }
    }

  }
)
