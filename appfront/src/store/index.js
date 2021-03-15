import Vue from 'vue';
import Vuex from 'vuex';
Vue.use(Vuex);

const store = new Vuex.Store({

  state: {
    // 存储token
    Authorization: localStorage.getItem('Authorization') ? localStorage.getItem('Authorization') : ''
  },

  mutations: {
    // 修改token，并将token存入localStorage
    setToken (state, token) {
      state.Authorization = token.Authorization;
      console.log('set')
      localStorage.setItem('Authorization', token.Authorization);
    },
    delToken (state){
      state.Authorization = '';
      console.log('delete')

      localStorage.removeItem('Authorization');
      console.log(localStorage.getItem('Authorization'))
    }
  }
});
export default store;
