<template>
  <el-container>
    <el-form :model="form" class="demo-form-inline"
              style="margin: 0 auto; width: 80%">
      <el-form-item>
        <el-input type="textarea"
                :rows="5"
                v-model="form.sql"
                style="width: 100%">
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-input type="textarea"
                  :rows="5"
                  v-model="form.parameter"
                  style="width: 100%">
        </el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="getResult">
          生成结果
        </el-button>
      </el-form-item>
      <el-form-item>
        <el-input type="textarea"
                  :rows="5"
                  v-model="result"
                  style="width: 100%">
        </el-input>
      </el-form-item>
    </el-form>

  </el-container>
</template>

<script>
export default {
  name: "SQLParmImport",
  data() {
    return {
      form:{
        sql: '',
        parameter: ''
      },
      result: ''
    }
    },
  methods:{
    getResult(){
      let data = {}
      data['sql'] = this.form.sql
      data['parameter'] = this.form.parameter
      this.$axios.post('/Tool/CombineSQLAndParameter/', data)
        .then(({data:res}) =>{
          this.result = res.data
      })
    }
  }
}
</script>

<style scoped>

</style>
