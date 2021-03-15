<template>
<el-container>
  <el-header style="height: auto; margin-top: 20px">
    <el-card>
      <el-form :inline="true" class="demo-form-inline">
        <el-form-item label="仓库名:">
          <el-select v-model="warehouse.name" filterable placeholder="">
            <el-option v-for="warehouse in warehouse_list" :label="warehouse.name" :value="warehouse.value" :key="warehouse.name"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="状态:">
          <el-select v-model="warehouse.status" placeholder="">
            <el-option v-for="item in warehouse_status" :label="item.name" :value="item.id" :key="item.id"></el-option>
          </el-select>
      </el-form-item>
      <el-form-item>
        <el-button @click="search">搜索</el-button>
      </el-form-item>
    </el-form>
    </el-card>
  </el-header>
      <el-container>
        <el-card style="width: 100%; margin: 20px 20px 20px">
          <el-table
          :data="show_warehouses_info"
          border
          style="width: 100%"
          min-height="400px"
          v-loading="page.searchLoading">
            <el-table-column
            type="selection"
            width="55">
          </el-table-column>
          <el-table-column
            fixed
            prop="name"
            label="仓库名"
            width="150">
          </el-table-column>
          <el-table-column
            prop="max_online"
            label="最大在线数"
            width="120">
          </el-table-column>
          <el-table-column
            prop="last_online"
            label="上次在线数"
            resizable>
          </el-table-column>
          <el-table-column
            prop="last_check_time"
            label="检查时间"
            resizable>
          </el-table-column>
            <el-table-column
            prop="status"
            label="检查状态"
            resizable>
              <template slot-scope="scope">
                <el-tag v-if="scope.row.status == '正常'" effect="dark" type="success">
                  {{scope.row.status}}
                </el-tag>
                <el-tag v-if="scope.row.status == '异常'" effect="dark" type="warning">
                  {{scope.row.status}}
                </el-tag>
                <el-tag v-if="scope.row.status == '未被检查'" effect="dark" type="danger">
                  {{scope.row.status}}
                </el-tag>
            </template>
          </el-table-column>
        </el-table>
          <div class="page" style="text-align: center">
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
import {Message} from "../../js/common";

export default {
  name: "Monitor",
  data () {
    return {
      warehouse:{
        status: 0,
        name: '',
      },
      warehouse_list:[{name: '全部', value: ''}],
      warehouse_status:[
        {id: 0, name: '全部'},
        {id: 1, name: '正常'},
        {id: 2, name: '异常'},
        {id: 3, name: '掉线'}
      ],
      warehouses_info: [],
      show_warehouses_info: [],
      page: {
        current_page: 1, //当前页数
        page_size: 10, //当前显示的数量
        total: 20,
        searchLoading: false,
      },
      monitor_list: [],
      monitor_cookie: '',
      wms_cookie: '',
      table_data: [{'monitor_id': '', 'monitor_name': '', 'last_offline_date': '', 'status':''}],
      timer: '',
      monitor_condition: {
        cur_monitor: '',
        max_monitor: ''
      },

    }
  },
  mounted() {
    this.getAllWarehouse()
    this.search()
  },
  methods: {
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      this.page.current_page = 1;
      this.page.page_size = val;
      this.show();
    },
    //当前页改变时触发 跳转其他页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      this.page.current_page = val;
      this.show();
    },
    show(){
      let start = (this.page.current_page-1)*this.page.page_size
      let end = this.page.current_page*this.page.page_size-1
      if(end >=this.warehouses_info.length)
      {
        end = this.warehouses_info.length-1
      }
      this.show_warehouses_info = this.warehouses_info.slice(start, end+1)
    },
    search() {
      let data = {}
      data['status'] = this.warehouse.status
      data['name'] = this.warehouse.name
      this.page.searchLoading = true
      this.page.current_page = 1
      this.$axios.post('/monitor/getMonitorInfo/', data)
        .then(({data: res}) => {
          this.warehouses_info = res.data
          this.page.total = this.warehouses_info.length
          this.page.searchLoading = false
          this.show()
        })
    },
    getAllWarehouse(){
      this.$axios.post('/monitor/getAllWarehouse/')
        .then(({data: res}) => {
          let temp = res.data
          for(let i=0;i<temp.length;i++){
            this.warehouse_list.push({'name': temp[i].name, 'value': temp[i].name})
          }
          console.log(this.warehouse_list)
        })
    }
  }
}
</script>

<style>
.monitor-show{
  margin:0px auto;
  text-align:center;
}
.el-divider{
  margin: 12px 0 !important;
}
.monitor{
  margin: 0px 10px 10px 0px;
  border: solid;
  border-radius: 4px;
  float: left;
  height: 30px;
  width: 200px;
}
 .el-table .warning-row {
    background: darkred;
    color: white;
  }

  .el-table .success-row {
    background: #ffffff;
    color: black;
  }
  .el-table .warning-row:hover>td {
    background: transparent !important;
  }
</style>
