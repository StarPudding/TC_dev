<template>
  <div>
    <div class="LoginForm">
      <el-input
        placeholder="请输入用户名"
        suffix-icon="el-icon-user"
        id="username"
        name="username"
        class="input_field"
        v-model="loginForm.username">
      </el-input>
      <el-input
        type="password"
        show-password
        placeholder="请输入密码"
        suffix-icon="el-icon-lock"
        id="password"
        name="password"
        class="input_field"
        v-model="loginForm.password">
      </el-input>
      <el-button @click="login">登录</el-button>
    </div>

  </div>
</template>

<script>
import { mapMutations } from 'vuex';
export default {
  name: "Login",
   data () {
    return {
      loginForm: {
        username: '',
        password: ''
      }
    };
  },
  methods:{
    ...mapMutations(['setToken']),
    ...mapMutations(['delToken']),
    login(){
      this.$axios.post('/user/login/', this.loginForm)
      .then(({data:res}) =>{
        console.log(res)
        let flag = res.code
        this.userToken = res.data.token
        console.log(flag)
        if(flag===200)
        {
          this.setToken({ Authorization: this.userToken })
          this.$router.push('/Home')
        }
      })
    }
  }
}
</script>

<style scoped>
.LoginForm {
  height: 300px;
  width: 300px;
  margin: 20px auto 0;
}
.input_field{
  padding-top: 4px;
  padding-bottom: 4px;
}
</style>
