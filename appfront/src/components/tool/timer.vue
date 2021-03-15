<template>
  <el-container>
    <el-header style="height: auto; margin-top: 20px">
        <el-card>
          <el-form :inline="true" class="demo-form-inline">
            <el-form-item label="定时任务名:" >
              <el-input></el-input>
            </el-form-item >
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
          :data="list"
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
              label="定时任务名"
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
  name: "timer",
  data() {
    return {}
  },
  methods:{
    list(){

    }
  }
}
</script>

<style scoped>

</style>
