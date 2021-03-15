<template>
  <div class="test_form">
    <el-form ref="test" :rules="rules" :model="test" label-width="120px" label-position="left">
      <el-form-item label="测试名称" prop="name">
        <el-input v-model="test.name"></el-input>
      </el-form-item>
      <el-form-item label="测试url">
        <el-input v-model="test.url"></el-input>
      </el-form-item>
      <el-form-item label="请求方式" filterable placeholder="请选择">
        <el-select v-model="test.method" filterable placeholder="请选择">
          <el-option
            v-for="item in method"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="是否有请求头">
        <el-switch v-model="test.header"></el-switch>
      </el-form-item>
      <el-form-item label="是否需要cookie" filterable placeholder="请选择">
        <el-select v-model="test.cookie">
          <el-option
            v-for="item in cookie"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="需发送的表单" style="width: 500px" placeholder="请选择">
        <el-input v-model="test.form" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="前置case" style="width: 500px" placeholder="请选择">
        <el-select v-model="test.dependent_id">
          <el-option
            v-for="item in case_list"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="依赖case的哪些数据" style="width: 500px" placeholder="请选择">
        <el-input v-model="test.dependent_data" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="依赖的数据应该填在哪里" style="width: 500px" placeholder="请选择">
        <el-input v-model="test.data_position" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="数据" style="width: 500px" placeholder="请选择">
        <el-input v-model="test.data" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="预期结果" style="width: 500px" placeholder="请选择">
        <el-input v-model="test.expect_result" type="textarea"></el-input>
      </el-form-item>
      <el-form-item label="预期结果类型" style="width: 500px" placeholder="请选择">
        <el-select v-model="test.expect_result_type">
          <el-option
            v-for="item in expect_result_type"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
        </el-select>
      </el-form-item>
  </el-form>
    <el-button @click="addTestCase">增加用例</el-button>
  </div>

</template>

<script>
export default {
  name: "TestCase",
  data() {
    return {
      test: {
        name:'',
        url: '',
        method:'',
        header:'',
        cookie:'',
        form:'',
        dependent_id: '',
        dependent_data:'',
        data_position:'',
        data:'',
        expect_result: '',
        expect_result_type: ''
      },
      method: [
        {id:'post', name:'post'},
        {id:'get', name:'get'},
        {id:'delete', name:'delete'},
        {id:'put', name:'put'}
        ],
      cookie: [
        {id:'write', name:'这是登录请求'},
        {id:'yes', name:'需要'},
        {id:'no', name:'不需要'},
      ],
      case_list:[
        {id: 'case_id', name: 'case_name'}
      ],
      expect_result_type: [
        {id: 0, name: 'html'},
        {id: 1, name: 'json'}
        ],
      rules: {
          name: [
            { required: true, message: '请输入用例名称', trigger: 'blur' },
            { min: 3, max: 5, message: '长度在 3 到 5 个字符', trigger: 'blur' }
          ]
        }
    }
  },
  methods:{
    addTestCase(){
      this.$axios.post('/TestCase/', data)
      .then(({data:res}) =>{
        this.table_data = res.data
      })
    }
  }
}
</script>

<style scoped>
.test_form{
  width: 400px;
  margin: 0 auto;
  margin-top: 20px;
}

</style>
