<template>
  <el-container class="test_form">
    <div v-if="step=1" style="margin-top: 10px">
      <el-button @click="publishTest">
        test环境发布
      </el-button>
      <el-button>
        stage环境发布
      </el-button>
      <el-button>
        prod环境发布
      </el-button>
    </div>
  </el-container>
</template>

<script>
import {Message} from "../../js/common";

export default {
  name: "VersionControlTest",
  beforeCreate() {

  },
  data() {
    return {
      step: 1,
      kind: 1,
      projects: [
      ],
      environments: [
      ],
      versionList:'',
      console: '',
      project:'',
      environment:'',
      message: '',
      log_number: 50,
      logVisible: false,
      logLoading: false,
      logs: [],
      page: {
        current_page: 1, //当前页数
        page_size: 10, //当前显示的数量
        total: '',
      },
    }
  },
  mounted() {
    this.getAllProject()
  },
  methods:{
    // 发布test
    publishTest(){

    },

    // 根据id，获得environment_name
    getProjectById(project_id){
      let _this = this;
      for(let i=0;i<_this.projects.length;i++){
        let id = _this.projects[i].project_id
        if(project_id === id){
          return _this.projects[i].project_name
        }
      }
      return null
    },
    // 根据id，获得environment_name
    getEnvironmentById(environment_id){
      let _this = this;
      for(let i=0;i<_this.environments.length;i++){
        let id = _this.environments[i].environment_id
        if(environment_id === id){
          return _this.environments[i].environment_name
        }
      }
      return null
    },
    // 进入界面时，读取项目表
    getAllProject(){
      this.$axios.post('/system/get_all_project/')
      .then(({data:res}) =>{
        this.projects = res.data
      })
    },
    // 通过选择的项目获得环境列表
    getEnvironmentByProject(){
      let data = {'project_id': this.project}
      this.$axios.post('/system/get_environment_by_project/', data)
      .then(({data:res}) =>{
        this.environments = res.data
        this.environment = ''
      })
    },
    // 项目变化时，相应的环境列表也要变
    onProjectChange(){
      this.environment = ''
      // 从数据库里取
      // this.$axios.postr
    },
    // 更新并且合并版本
    UpdateAndCombine(){
      let data = {}
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      // 合并版本之前，首先要进行更新
      this.console = this.console + "版本正在更新中...." + '\n'
      this.$axios.post('/VersionControl/Update/', data)
        .then(({data:res}) =>{
          if(res.message === 'success'){
            //更新版本成功
            this.console = this.console  + res.data + '\n'
            this.console = this.console + "版本更新完成\n"
            //开始合并
            this.Combine()
          }
          else if(res.message === 'fail'){
            //更新版本失败
            this.console = this.console  + res.data + '\n'
            this.console = this.console + "版本更新失败，请重试\n"
          }
      })
    },
    // 合并版本
    Combine(){
      let data = {}
      data['versionList'] = this.versionList
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      this.console = this.console + "版本正在合并中...." + '\n'
      this.$axios.post('/VersionControl/Combine/', data)
      .then(({data:res}) =>{
        if(res.message === 'conflicts'){
          this.console = this.console  + res.data + '\n'
          this.console = this.console + "版本合并冲突!请联系开发人员解决\n"
                  // 弹窗消息
          let title = this.system + '_' + this.environment
          let message = '版本号: ' + this.versionList + ' 合并冲突!'
          Message(title, message)
        }
        else if(res.message === 'success'){
          this.console = this.console  + res.data + '\n'
          this.console = this.console + "版本合并完成\n"
          let title = this.getProjectById(this.project) + '_' + this.getEnvironmentById(this.environment)
          let message = '版本号: ' + this.versionList + ' 合并完成!'
          Message(title, message)
        }


      })
    },
    // 提交版本
    commit(){
      let data = {}
      data['message'] = this.message
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      this.console = this.console + "版本正在提交中...." + '\n'
      this.$axios.post('/VersionControl/Commit/', data)
      .then(({data:res}) =>{
        this.console = this.console + res.data + '\n'
        this.console = this.console + "版本提交完成\n"
        // 弹窗消息
        let title = this.getProjectById(this.project) + '_' + this.getEnvironmentById(this.environment)
        let message = '版本号: ' + this.versionList + ' 提交完毕!'
        Message(title, message)
      })
    },
    // 还原版本
    restore(){
      let data = {}
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      this.console = this.console  + "版本正在还原中...." + '\n'
      this.$axios.post('/VersionControl/Revert/', data)
      .then(({data:res}) =>{
        this.console = this.console  + res.data + '\n'
        this.console = this.console + "版本还原完成\n"
        // 弹窗消息
        let title = this.getProjectById(this.project) + '_' + this.getEnvironmentById(this.environment)
        let message = '版本号: ' + this.versionList + ' 还原完毕!'
        Message(title, message)
      })
    },
    // 清空显示列表
    clear(){
      this.console = ''
    },
    // 解锁
    cleanup(){
      let data = {}
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      this.console = this.console + "正在cleanup....\n"
      this.$axios.post('/VersionControl/Cleanup/', data)
      .then(({data:res}) =>{
        this.console = this.console + res.data + '\n'
        this.console = this.console + "cleanup完成\n"
        // 弹窗消息
        let title = this.getProjectById(this.project) + '_' + this.getEnvironmentById(this.environment)
        let message = '版本号: ' + this.versionList + ' 解锁完毕!'
        Message(title, message)
      })
    },
    // 查看记录
    log(){
      let data = {}
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      data['number'] = this.log_number
      // 打开窗口
      this.logs = []
      this.logVisible = true
      this.logLoading = true
      // 查看记录之前，首先要进行更新
      this.$axios.post('/VersionControl/Update/', data)
        .then(({data:res}) =>{
          if(res.message === 'success'){
            this.$axios.post('/VersionControl/Log/', data)
              .then(({data:res}) =>{
                this.logLoading = false
                this.logs = res.data
              })
          }
          else if(res.message === 'fail'){
          }
      })

    },
    // jenkins构建
    jenkins_build(){
      let data = {}
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      this.console = this.console + "正在构建项目....\n"
      this.$axios.post('/VersionControl/Jenkins_build/', data)
      .then(({data:res}) =>{
        // 弹窗消息
        let title = this.getProjectById(this.project) + '_' + this.getEnvironmentById(this.environment)
        let message = '构建开始!请到jenkins查看具体构建信息'
        Message(title, message)
      })
    }
  }
}

</script>

<style scoped>
.test_form{
  text-align: center;

}
</style>
