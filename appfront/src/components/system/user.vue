<template>
  <el-container>
      <el-header style="height: auto; margin-top: 20px">
        <el-card>
          <el-form :inline="true" class="demo-form-inline">
          <el-form-item label="用户名:">
            <el-input v-model="user.name"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button>搜索</el-button>
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
            fixed
            prop="username"
            label="用户名"
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
            fixed="right"
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
name: "user",
  data() {
    return {
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
  },
  methods:{
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
  margin-bottom: 20px;
}
.page{
  text-align: center;
  margin-top: 20px;
}
</style>
