<template>
  <div id="app">
<!--     <div class="left">-->
<!--         <el-scrollbar class='page-component__scroll'>-->
<!--             <div class="box">123</div>-->
<!--         </el-scrollbar>-->
<!--     </div>-->
<!--     <div class="right">-->
<!--         <el-scrollbar class='page-component__scroll'>-->
<!--             <div class="box">123</div>-->
<!--         </el-scrollbar>-->
<!--     </div>-->
    <div v-if="$route.meta.keepAlive" style="width: 100%" id="app1">
      <el-container>
        <header-nav></header-nav>
      </el-container>
    </div>
    <div v-else>
      <router-view/>
    </div>
  </div>
</template>

<script>
import MainTabBar from "@/components/index"
export default {
  name: 'App',
  components: {
    headerNav: MainTabBar
  },
 /* 监听table数据对象 */
  watch: {
    tableData(val) {
      this.doLayout();
    }
  },
  methods:{
    doLayout(){
        this.$nextTick(() => {
                this.$refs.table.doLayout()
        })
  }


}
}
</script>

<style>

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 0px;
  width: 100%;
  height: 100%;
}
#app1{
  width: 100%;
  height: 100%;
}
.el-container{
  width: 100%;
  height: 100%;
}
html, body{
  width: 100%;
  height: 100%;
  margin: 0;
}
.left{
        width:200px;
        height:100%;
        background:#f00;
        float:left;
    }

.page-component__scroll{
   height:calc(100vh - 117px);
   width: 100%;
}
   .box{
height:1500px;
background-color:#000000;
width:200px;
color:#fff;
    }
.el-scrollbar__wrap {
 overflow-x: hidden;

}

tr .is-hidden {
        display: table-cell;
        overflow: hidden;
      }

.el-select-dropdown .el-scrollbar {padding-bottom: 17px;}
</style>
