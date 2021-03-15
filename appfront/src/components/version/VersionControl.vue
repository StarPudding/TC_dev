<template>
  <el-container class="test_form">
    <el-header>
      <el-form :inline="true" :model="projects" class="demo-form-inline">
      <el-form-item label="项目:" >
        <el-select v-model="project" placeholder="" @change="getEnvironmentByProject" >
          <el-option v-for="project in projects" :label="project.project_name" :value="project.project_id" :key="project.project_id"></el-option>
        </el-select>
      </el-form-item >
      <el-form-item label="环境:">
        <el-select v-model="environment" @change="ReadLogList">
          <el-option v-for="environment in environments" :label="environment.environment_name" :value="environment.environment_id" :key="environment.environment_id"></el-option>
        </el-select>
      </el-form-item>
      </el-form>
    </el-header>
    <el-main v-if="environment===1||environment===2">
        <div style="margin: 0 auto; width: 80%">
                <el-input
          type="textarea"
          autosize
          placeholder="请输入需要发布的版本"
          v-model="versionList">
        </el-input>
        <el-input
          type="textarea"
          autosize
          placeholder="请输入提交时的注释"
          v-model="message">
        </el-input>
        </div>
      <div style="margin: 20px 20% 20px 20%">
        <el-button @click="UpdateAndCombine">合并版本</el-button>
        <el-button @click="commit">提交版本</el-button>
        <el-button @click="restore">回退版本</el-button>
        <el-button @click="cleanup">解锁</el-button>
        <el-button @click="log">查看记录</el-button>
        <el-button @click="clear">清空控制台</el-button>
        <el-button @click="jenkins_build">jenkins构建</el-button>
      </div>
      <el-input
        type="textarea"
        :autosize="{ minRows: 16, maxRows: 16}"
        placeholder="信息将会打印在这..."
        v-model="console"
        readonly>
      </el-input>
    </el-main>

    <el-dialog
      title="历史提交记录"
      :visible.sync="logVisible"
      width="50%">
        <el-table
          v-loading="logLoading"
          :data="logs"
          border
          style="width: 100%"
          min-height="200px">
          <el-table-column
            fixed
            prop="version"
            label="修订号"
            min-width="40px"
            resizable>
          </el-table-column>
          <el-table-column
            prop="author"
            label="作者"
            min-width="40px"
            resizable>
          </el-table-column>
          <el-table-column
            prop="date"
            label="时间"
            resizable>
          </el-table-column>
          <el-table-column
            prop="remark"
            label="备注"
            resizable>
          </el-table-column>
        </el-table>
    </el-dialog>
    <el-main v-if="environment===3">
      <el-main>
       <el-select v-model="chosenVersion" multiple style="width: 80%;margin-bottom: 20px" placeholder="请选择">
          <el-option
            v-for="item in chosenVersion"
            :key="item"
            :label="item"
            :value="item">
          </el-option>
        </el-select>
        <el-input
          type="textarea"
          autosize
          placeholder="请输入提交时的注释"
          v-model="message">
        </el-input>
        <el-table
        :data="versions"
        border
        style="width: 100%"
        min-height="400px"
        v-loading="page.searchLoading">
        <el-table-column
          prop="version"
          label="版本号"
          width="150">
        </el-table-column>
        <el-table-column
          prop="author"
          label="提交人"
          width="120">
        </el-table-column>
        <el-table-column
          prop="date"
          label="提交时间"
          resizable>
        </el-table-column>
        <el-table-column
          prop="remark"
          label="备注"
          resizable>
        </el-table-column>
          <el-table-column
          label="操作"
          width="100">
          <template slot="header" slot-scope="scope">
            <label>操作</label>
          </template>
          <template slot-scope="scope">
            <el-button v-if="isVersionChosen(scope.row)===false"
                       type="primary" size="small" @click="addVersion(scope.row)">添加</el-button>
            <el-button v-else type="warning" size="small" @click="deleteVersion(scope.row)">移除</el-button>
          </template>
        </el-table-column>
      </el-table>
        <div class="page">
            <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="page.current_page"
              :page-sizes="[10, 20, 30, 40]"
              :page-size="page.page_size"
              layout="total, sizes, prev, pager, next, jumper"
              :total="page.total">
            </el-pagination>
          </div>
      </el-main>
      <div style="margin: 20px 20% 20px 20%">
        <el-button @click="UpdateAndCombine">合并版本</el-button>
        <el-button @click="commit">提交版本</el-button>
        <el-button @click="restore">回退版本</el-button>
        <el-button @click="cleanup">解锁</el-button>
        <el-button @click="log">查看记录</el-button>
        <el-button @click="clear">清空控制台</el-button>
        <el-button @click="jenkins_build">jenkins构建</el-button>
      </div>
      <el-input
        type="textarea"
        :autosize="{ minRows: 16, maxRows: 16}"
        placeholder="信息将会打印在这..."
        v-model="console"
        readonly>
      </el-input>
    </el-main>
  </el-container>
</template>

<script>
import {Message} from "../../js/common";

export default {
  name: "VersionControl",
  data() {
    return {
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
        searchLoading: false,
      },
      versions: [],
      allVersion:[],
      chosenVersion: [],
    }
  },
  mounted() {
    this.getAllProject()
  },
  methods:{
      //每页条数改变时触发 选择一页显示多少行
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.page.current_page = 1;
      this.page.page_size = val;
      this.showVersion()
    },
    //当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.page.current_page = val;
      this.showVersion()
    },
    isVersionChosen(row){
      for(let i=0; i<this.chosenVersion.length;i++){
        if(row.version===this.chosenVersion[i]){
          return true
        }
      }
      return false
    },
    addVersion(row) {
      console.log(row.version)
      this.chosenVersion.push(row.version)
      this.chosenVersion.sort()

      let str = ''
      for(let i=0;i<this.chosenVersion.length;i++)
      {
        if(i===0){
          str = str + this.chosenVersion[i]
        }
        else {
          str = str + "," + this.chosenVersion[i]
        }
      }
      console.log(str)
      this.versionList = str
     },
    deleteVersion(row){
      this.chosenVersion.some((item, i) => {
        if(item===row.version){
          this.chosenVersion.splice(i, 1)
          return true
        }
      })
      return false
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
    //
    ReadLogList(){
      this.versionList = ''
      this.chosenVersion = []
      this.page.current_page = 1
      if(this.environment===3)
      {
        this.getSvnVersionList()
      }
    },
    // 获得相应svn所有版本号
    getSvnVersionList(){
      let data = {}
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      this.page.searchLoading= true
      this.$axios.post('/VersionControl/getSVNVersionList/', data)
        .then(({data:res}) =>{

        this.allVersion = res.data
          this.page.total = this.allVersion.length
          this.showVersion()
          this.page.searchLoading= false
      })
    },
    // 将版本号展示在前端
    showVersion(){
      let start = (this.page.current_page-1)*this.page.page_size
      let end = this.page.current_page*this.page.page_size-1
      if(end >=this.allVersion.length)
      {
        end = this.allVersion.length-1
      }
      this.versions = this.allVersion.slice(start, end+1)
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
      console.log("versionList:" + this.versionList)
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
