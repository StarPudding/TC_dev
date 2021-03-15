<template>
  <el-container>
    <el-header style="height: auto">
      <el-card>
        <el-form :inline="true" :model="projects" class="demo-form-inline">
          <el-form-item label="项目:" >
            <el-select filterable
                       v-model="form.project" placeholder="" @change="getEnvironmentByProject" >
              <el-option v-for="project in projects" :label="project" :value="project" :key="project"></el-option>
            </el-select>
          </el-form-item >
          <el-form-item label="状态:">
            <el-select v-model="form.status">
              <el-option v-for="environment in environments" :label="environment.environment_name" :value="environment.environment_id" :key="environment.environment_id"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="提交人:">
            <el-input v-model="form.submitter"></el-input>
          </el-form-item>
          <el-form-item label="版本号:">
            <el-input v-model="form.submitter"></el-input>
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
        :data="users"
        border
        style="width: 100%"
        min-height="400px">
          <el-table-column
          type="selection"
          width="55">
        </el-table-column>
        <el-table-column
          prop="username"
          label="样例名"
          width="150">
        </el-table-column>
        <el-table-column
          prop="mobile"
          label="手机号"
          width="120">
        </el-table-column>
        <el-table-column
          prop="email"
          label="邮箱"
          resizable>
        </el-table-column>
        <el-table-column
          label="操作"
          width="250">
          <template slot="header" slot-scope="scope">
            <label>操作</label>

          </template>
          <template slot-scope="scope">
            <el-button type="text" size="small" @click="">编辑</el-button>
            <el-button type="text" size="small" @click="">修改密码</el-button>
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
      </el-card>

    </el-container>
  </el-container>
</template>

<script>
export default {
name: "Jmeter",data() {
    return {
      projects: [
      ],
      environments: [
      ],
      form:{
        project:'',
        status:'',
        version: '',
        submitter: ''
      },
      user: {
        username: ''
      },
      users:[
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
        { username: '唐顺意', mobile: '15616641127', email: '767067326@qq.com'},
      ],
      page: {
        current_page: 1, //当前页数
        page_size: 10, //当前显示的数量
        total: '',
      },
    }
  },
  mounted() {
    this.list()
    this.getAllProjects()
  },
  methods:{
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
    getAllProjects(){
      this.$axios.post('/VersionControl/getAllProjects/')
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
  //每页条数改变时触发 选择一页显示多少行
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.page.current_page = 1;
      this.page.page_size = val;
      this.list();
    },
    //当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.page.current_page = val;
      this.list();
    },
    list(){
      let data = {}
      // 后台通过这两个值判断要取哪些
      data['current_page'] = this.page.current_page
      data['page_size'] = this.page.page_size
      this.$axios.post('/system/get_user/', data)
        .then(({data:res}) =>{
          this.users = res.data['dataset']
          this.page.total = res.data['count']
        })
    }
  }
}
</script>

<style scoped>
.button-area{
  margin-bottom: 10px;
}
.page{
  text-align: center;
}
div{
  font-size: 12px !important;
}



</style>
