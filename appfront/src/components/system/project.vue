<template>
  <el-container>
    <el-dialog
      title="基础信息"
      :visible.sync="base_info.baseInfoVisible"
      width="60%">
      <el-form :model="base_info" label-width="80px" size="medium" style="margin-left: 40px; margin-right: 40px"
        v-loading="base_info.baseInfoLoading">
        <el-form-item label="项目地址:">
          <span v-if="base_info.project_position==''">(空)</span>
          <span v-else>{{base_info.project_position}}</span>
        </el-form-item>
        <el-form-item label="svn地址:" style="margin-top: 40px">
          <span v-if="base_info.svn_position==''">(空)</span>
          <span v-else>{{base_info.svn_position}}</span>
        </el-form-item>
        <el-form-item label="jenkins地址:" style="margin-top: 40px">
          <span v-if="base_info.jenkins_position==''">(空)</span>
          <span v-else>{{base_info.jenkins_position}}</span>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" >确 定</el-button>
        <el-button @click="base_info.baseInfoVisible = false">取 消</el-button>
      </span>
    </el-dialog>
    <el-dialog
      title="基础信息"
      :visible.sync="base_info.baseInfoVisible"
      width="60%">
      <el-form :model="base_info" label-width="80px" size="medium" style="margin-left: 40px; margin-right: 40px"
        v-loading="base_info.baseInfoLoading">
        <el-form-item label="项目地址:">
          <span v-if="base_info.project_position==''">(空)</span>
          <span v-else>{{base_info.project_position}}</span>
        </el-form-item>
        <el-form-item label="svn地址:" style="margin-top: 40px">
          <span v-if="base_info.svn_position==''">(空)</span>
          <span v-else>{{base_info.svn_position}}</span>
        </el-form-item>
        <el-form-item label="jenkins地址:" style="margin-top: 40px">
          <span v-if="base_info.jenkins_position==''">(空)</span>
          <span v-else>{{base_info.jenkins_position}}</span>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" >确 定</el-button>
        <el-button @click="base_info.baseInfoVisible = false">取 消</el-button>
      </span>
    </el-dialog>
    <el-header style="height: auto; margin-top: 20px">
        <el-card>
          <el-form :inline="true" class="demo-form-inline">
            <el-form-item label="项目:" >
              <el-select v-model="project" placeholder="" @change="getEnvironmentByProject">
                <el-option v-for="project in projects" :label="project.project_name" :value="project.project_id" :key="project.project_id"></el-option>
              </el-select>
            </el-form-item >
            <el-form-item label="环境:">
              <el-select v-model="environment">
                <el-option v-for="environment in environments" :label="environment.environment_name" :value="environment.environment_id" :key="environment.environment_id"></el-option>
              </el-select>
            </el-form-item>
            <el-form-item>
              <el-button @click="list">搜索</el-button>
            </el-form-item>
          </el-form>
        </el-card>
      </el-header>
    <el-container>
        <el-card style="width: 100%; margin: 20px 20px 20px">
          <div class="button-area">
            <el-button>新增</el-button>
          </div>
          <el-table
          :data="lists"
          border
          style="width: 100%"
          min-height="400px">
            <el-table-column
            type="selection"
            width="55">
            </el-table-column>
            <el-table-column
              fixed
              prop="project_name"
              label="项目"
              min-width="150">
            </el-table-column>
          <el-table-column
            prop="environment_name"
            label="环境"
            min-width="120">
          </el-table-column>
          <el-table-column
            fixed="right"
            label="操作"
            min-width="250">
            <template slot="header" slot-scope="scope">
              <label>操作</label>
            </template>
            <template slot-scope="scope">
              <el-button type="text" size="small" @click="showBaseInfo(scope.row)">查看基础信息</el-button>
              <el-button type="text" size="small" @click="">修改SVN信息</el-button>
              <el-button type="text" size="small" @click="">修改Jenkins信息</el-button>
              <el-popconfirm
                confirm-button-text='好的'
                cancel-button-text='不用了'
                icon="el-icon-info"
                icon-color="red"
                title="这是一段内容确定删除吗？"
                @confirm=""
                >
                <el-button type="text" size="small" slot="reference">删除</el-button>
              </el-popconfirm>

            </template>
          </el-table-column>
        </el-table>
        </el-card>
      </el-container>
  </el-container>
</template>

<script>
export default {
  name: "project",
  data() {
    return {
      projects: [
      ],
      environments: [
      ],
      project:'',
      environment:'',

      page: {
        current_page: 1, //当前页数
        page_size: 10, //当前显示的数量
        total: '',
      },
      // 列表
      lists: [],
      //基础信息
      base_info:{
        baseInfoVisible: false,
        baseInfoLoading: false,
        project_position: '',
        svn_position: '',
        jenkins_position: ''
      },
    }
  },
  mounted() {
    this.getAllProject()
    this.list()
  },
  methods:{
    // 读取项目表
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
    // 获得所有项目环境列表
    list(){
      let data ={}
      data['project_id'] = this.project
      data['environment_id'] = this.environment
      this.$axios.post('/system/getAllProjectAndEnvironment/', data)
      .then(({data:res}) =>{
        this.lists = res.data
      })
    },
    // 显示项目基础信息
    showBaseInfo(row){
      // 打开列表
      this.base_info.baseInfoVisible = true
      this.base_info.project_position = ''
      this.base_info.svn_position = ''
      this.base_info.jenkins_position = ''
      this.base_info.baseInfoLoading = true

      // 准备data
      let data = {}
      data['id'] = row.id
      this.$axios.post('/system/getMainInfo/', data)
      .then(({data:res}) =>{
        this.base_info.project_position = res.data.project_position
        this.base_info.svn_position = res.data.svn_position
        this.base_info.jenkins_position = res.data.jenkins_position
        this.base_info.baseInfoLoading = false
      })
    }
  }
}
</script>

<style scoped>

</style>
