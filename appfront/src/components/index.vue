<template>
  <el-container class="index">
    <el-header style="height: 60px">
      <div>
        <span>中拓信科-版本管理平台</span>
      </div>
    </el-header>
    <el-container class="mainWindow">
      <el-scrollbar>
        <el-menu router
               default-active="1-4-1"
               class="el-menu-vertical-demo"
               @open="handleOpen"
               @close="handleClose"
               :collapse="isCollapse"
               collapse-transition="true">

        <el-submenu v-for="submenu in all_menu" v-if="submenu.is_show" :index="submenu.index" :key="submenu.index">
          <template slot="title">
            <i :class="submenu.menu_icon"></i>
            <span slot="title">{{submenu.menu_name}}</span>
          </template>
          <el-menu-item v-for="menu in submenu.child" v-if="menu.is_show" @click="addTab(menu.menu_name, menu.menu_url)" :key="menu.index">
            <i :class="menu.menu_icon"></i>
            <span slot="title">{{menu.menu_name}}</span>
          </el-menu-item>
        </el-submenu>
      </el-menu>
      </el-scrollbar>
        <el-button style="width: 10px; padding: 0" @click="test"></el-button>
      <el-container>
        <el-tabs v-model="editableTabsValue" type="card" closable @tab-remove="removeTab" style="width: 100% !important">
          <el-tab-pane
            v-for="(item, index) in editableTabs"
            :key="item.name"
            :label="item.title"
            :name="item.name"
          >
          <component :is="item.content"/>
  <!--          <router-view/>-->
          </el-tab-pane>

        </el-tabs>

      </el-container>
    </el-container>
    <el-scrollbar class="page-component__scroll">

    </el-scrollbar>
  </el-container>
</template>

<script>
import router from "../router";
import getRouters from "../router/index"
import VersionControl from "./version/VersionControl";
export default {
  data() {
      return {
        all_menu:[
          {
            menu_name: '测试界面', index:1, child:[
              {menu_name: '版本管理', menu_url: '/version/VersionControl', child:[]},
            ]
          },
        ],
        activeIndex: '1',
        activeIndex2: '1',
        isCollapse: false,
        editableTabsValue: '2',
        editableTabs: [],
        tabIndex: 2
      };

    },
  mounted() {
    this.getAllMenu()

    // 添加父元素
    let child = document.getElementsByClassName("el-tabs__content")[0]
    console.log(child)
    let parent = document.getElementsByClassName('page-component__scroll')[0]
    console.log(parent)
    child.parentNode.replaceChild(parent, child)
    parent.firstChild.firstChild.appendChild(child)


    // $("div.el-tabs__content").wrap('<el-scrollbar class=\'page-component__scroll\'></el-scrollbar>')
  },
  methods: {
    test(){
      this.isCollapse = ! this.isCollapse
    },
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      },
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      },
      addTab(targetName, url) {
        let newTabName = ++this.tabIndex + '';
        let name = 'VersionControl'
        const temp = resolve => require(['../components' + url + '.vue'], resolve)
        this.editableTabs.push({
          title: targetName,
          name: newTabName,
          content: temp
        });
        this.editableTabsValue = newTabName;
      },
      removeTab(targetName) {
        let tabs = this.editableTabs;
        let activeName = this.editableTabsValue;
        if (activeName === targetName) {
          tabs.forEach((tab, index) => {
            if (tab.name === targetName) {
              let nextTab = tabs[index + 1] || tabs[index - 1];
              if (nextTab) {
                activeName = nextTab.name;
              }
            }
          });
        }

        this.editableTabsValue = activeName;
        this.editableTabs = tabs.filter(tab => tab.name !== targetName);
      },
      getAllMenu(){
        let data = {'test':'test'}
        console.log('get_menu')
        this.$axios.post('/system/get_all_menu/', data)
        .then(({data:res}) =>{
          this.all_menu = res.data
        })
      }
    }

}
</script>

<style scoped>
.mainWindow{
  height: calc(100vh - 100px);
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 150px;
  min-height: 400px;
  /*text-align: left;*/
  /*min-width: 150px;*/
}
.el-submenu .el-menu-item{
  min-width: 10px;

}
/deep/ .el-tabs__item{
  font-size: 12px !important;
}
.index{
  height: 100%;
  width: 100%;
}
.index span{
  font-size: 12px;
}
.el-header{
  padding-left: 0px;
  color: white;
  text-align: left;
  background-color: black;
}
.el-header span{
  margin: 20px;
  line-height: 60px;
  font-size: 25px;
}
.el-menu-item.is-active{
  color: black !important;
}
/*.el-menu-item, .el-submenu__title{*/
/*  height: 40px !important;*/
/*  line-height: 40px !important;*/
/*}*/

/* 标签页样式改变*/
/deep/ .el-tabs__nav-wrap{
  margin-bottom: 0 !important;
}
.el-scrollbar {
  overflow: hidden;
}

</style>
