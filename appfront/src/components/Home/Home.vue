<template>
  <div>
    <div>
      选择测试用例文件: <input type="file" name="test_file" accept=".xlsx" ref="test_file" @change="test_file_change"/>
      选择JSON文件:<input type="file" name="json_file" accept=".json" ref="json_file"/>
      <el-button @click="UploadFile">开始</el-button>
    </div>
    <div>
         <el-table
    :data="table_data"
    style="width: 1000px;clear:both;margin: 0 auto;"
    :row-class-name="tableRowClassName">
    <el-table-column
      prop="name"
      label="测试样例"
      width="200">
    </el-table-column>
    <el-table-column
      prop="result"
      label="返回结果"
      width="700">
    </el-table-column>
    <el-table-column
      prop="is_pass"
      label="状态"
      width="100">
    </el-table-column>
  </el-table>
    </div>

  </div>
</template>

<script>
import XLSX from 'xlsx'
export default {
  name: "Home",
  data() {
    return {
      form: {
        fileSavePath: '',
      },
      xlsx_file: null,
      table_data: [],
      outputs: [],
      file_name: {},
      cookie: '',
      // 让test有序进行
      test_condition: {
        cur_test: '',
        max_test: ''
      }

    }
  },
  methods: {
    test_file_change() {
      let test_file = this.$refs.test_file.files[0]
      const fileReader = new FileReader();
      fileReader.readAsBinaryString(test_file);
      fileReader.onload = (ev) => {
        try {
          const data = ev.target.result;
          const workbook = XLSX.read(data, {type: 'binary'});
          const wsname = workbook.SheetNames[0];//取第一张表
          const ws = XLSX.utils.sheet_to_json(workbook.Sheets[wsname]);//生成json表格内容
          this.table_data = [];//清空接收数据
          //编辑数据
          for (let i = 0; i < ws.length; i++) {
            console.log(ws[i])
            if (ws[i].是否执行 === 'yes') {
              let sheetData = {
                row: ws[i].__rowNum__ + 1,
                case_id: ws[i].case_id,
                name: ws[i].名称,
                result: '',
                is_pass:''
              }
              this.table_data.push(sheetData);
            }
          }
        } catch (e) {
          return false;
        }

      };
    },
    tableRowClassName({row, rowIndex}) {
      status = this.table_data[rowIndex].status
      console.log(status)
      if (status === "") {
        return 'warning-row';
      } else {
        return 'success-row';
      }
    },
    // 上传文件并获得相关文件名
    UploadFile() {
      let n = this.table_data.length

      let test_file = this.$refs.test_file.files[0]
      let json_file = this.$refs.json_file.files[0]
      let formData = new FormData()
      formData.append('test_file', test_file)
      formData.append('json_file', json_file)
      let config = {
        headers: {
          'Authorization': this.token,
          'Content-Type': 'multipart/form-data'
        }
      };
      console.log("---------getAllTestList----------")
      this.$axios.post('http://127.0.0.1:8011/TestCase/UploadFile/', formData, config)
        .then(({data: res}) => {
          this.file_name = res.data
          console.log(this.file_name['test_file'])
          this.TestUnit()
        })
    },

    //一个个执行用例
    TestUnit() {
      // 获得需要执行的用例个数
      let n = this.table_data.length
      //初始化执行列表
      this.test_condition.cur_test = 0
      this.test_condition.max_test = n

      this.TestOne(this.table_data[this.test_condition.cur_test].row)
    },
    TestOne(row) {
      let Data = {}
      Data['row']= row
      Data['testFileName'] = this.file_name['test_file']
      Data['jsonFileName'] = this.file_name['json_file']

      // 显示状态为测试中
      this.table_data[this.test_condition.cur_test].is_pass = "测试中"
      if (this.cookie === '') {
        Data['cookie'] = ''
      } else {
        Data['cookie'] = this.cookie
      }
      let config = {
        headers: {
          'Authorization': this.token,
        }
      };
      this.$axios.post('http://127.0.0.1:8011/TestCase/TestOne/', Data, config)
        .then(({data: res}) => {

          //res中包含有cookie
          if(res.data['cookie'] !== ''){
            this.cookie = res.data['cookie']
          }
          let result = res.data['result']
          this.table_data[this.test_condition.cur_test].result = result

          //是否通过
          let is_pass = res.data['is_pass']
          if(is_pass === 'pass')
            this.table_data[this.test_condition.cur_test].is_pass = "通过"
          else if(is_pass === 'fail')
            this.table_data[this.test_condition.cur_test].is_pass = "失败"
          this.test_condition.cur_test++
          if (this.test_condition.cur_test < this.test_condition.max_test) {
            this.TestOne(this.table_data[this.test_condition.cur_test].row)
          }



          // 执行完毕，解锁

        })
    }
  }
}
</script>

<style scoped>

</style>
