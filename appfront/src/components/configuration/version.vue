<template>
  <el-container>
    <el-row :gutter="20">
      <el-col :span="30">
        <span>
          选择系统:
        </span>
        <el-select v-model="test" placeholder="所属系统">
          <el-option label="区域一" value="shanghai"></el-option>
          <el-option label="区域二" value="beijing"></el-option>
        </el-select>
      </el-col>

    </el-row>
  </el-container>
</template>

<script>
export default {
  name: "version",
  data() {
    return {
      test: ''
    }
  }
}
</script>

<style scoped>

</style>
