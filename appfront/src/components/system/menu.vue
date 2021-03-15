<template>
  <el-container>
      <el-table :data="menus" border style="width: 100%"
                row-key="id"
                lazy
                :load=getChildMenu
                :tree-props="{children: 'children', hasChildren: 'has_child'}">>
      <el-table-column
        fixed
        prop="name"
        label="菜单名称"
        width="250"
        sortable>
      </el-table-column>
      <el-table-column
        prop="icon"
        label="菜单图标"
        width="200">
      </el-table-column>
      <el-table-column
        prop="url"
        label="路由地址"
        width="300">
      </el-table-column>
      <el-table-column
        prop="sort"
        label="排序"
        width="120">
      </el-table-column>
        <el-table-column
        prop="menu_icon"
        label="图标"
        width="150">
      </el-table-column>
      <el-table-column
        prop="authority"
        label="权限"
        width="150">
      </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="250">
      <template slot="header" slot-scope="scope">
        <label>操作</label>
        <el-button type="text" size="small" @click="editRootMenu(scope.row)">添加根目录</el-button>
      </template>
      <template slot-scope="scope">
        <el-button type="text" size="small" @click="editMenu(scope.row)">修改</el-button>
        <el-button type="text" size="small" @click="editChildMenu(scope.row)">添加下级菜单</el-button>
        <el-popconfirm
          confirm-button-text='好的'
          cancel-button-text='不用了'
          icon="el-icon-info"
          icon-color="red"
          title="这是一段内容确定删除吗？"
          @confirm="deleteMenu(scope.row.id)"
          >
          <el-button type="text" size="small" slot="reference">删除</el-button>
        </el-popconfirm>

      </template>
    </el-table-column>

    </el-table>
    <el-dialog
      title="修改菜单信息"
      :visible.sync="editMenuVisible"
      width="50%">
      <el-form :model="edit_menu_info" label-width="80px" size="medium" style="margin-left: 40px; margin-right: 40px">
        <el-form-item label="菜单名称:" style="margin-top: 40px">
          <el-input v-model="edit_menu_info.name"></el-input>
        </el-form-item>
        <el-form-item label="菜单地址:">
          <el-input v-model="edit_menu_info.url" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="菜单排序:">
          <el-input v-model="edit_menu_info.sort" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="是否显示:">
          <el-radio-group v-model="edit_menu_info.is_show">
            <el-radio label="0">隐藏</el-radio>
            <el-radio label="1">显示</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="菜单权限:">
          <el-input v-model="edit_menu_info.authority" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="菜单图标:">
          <el-input v-model="edit_menu_info.menu_icon" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="updateMenu">确 定</el-button>
        <el-button @click="editMenuVisible = false">取 消</el-button>
      </span>
    </el-dialog>
    <el-dialog
      title="新增菜单"
      :visible.sync="addMenuVisible"
      width="50%">
      <el-form :model="add_menu_info" label-width="80px" size="medium" style="margin-left: 40px; margin-right: 40px">
        <el-form-item label="父菜单:" style="margin-top: 40px">
          <el-input v-model="add_menu_info.parent" readonly></el-input>
        </el-form-item>
        <el-form-item label="菜单名称:" style="margin-top: 40px">
          <el-input v-model="add_menu_info.name"></el-input>
        </el-form-item>
        <el-form-item label="菜单地址:">
          <el-input v-model="add_menu_info.url" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="菜单排序:">
          <el-input v-model="add_menu_info.sort" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="是否显示:">
          <el-radio-group v-model="add_menu_info.is_show">
            <el-radio label="0">隐藏</el-radio>
            <el-radio label="1">显示</el-radio>
          </el-radio-group>
        </el-form-item>
        <el-form-item label="菜单权限:">
          <el-input v-model="add_menu_info.authority" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="菜单图标:">
          <el-input v-model="add_menu_info.menu_icon" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="addChildMenu">确 定</el-button>
        <el-button @click="addMenuVisible = false">取 消</el-button>
      </span>
    </el-dialog>
  </el-container>
</template>

<script>
import {Message,clone} from "../../js/common";
export default {
  name: "menu",
  data() {
    return{
      menus: [{'name':'test', 'has_child':true, children: [], 'child': '3,4'}],
      editMenuVisible: false,
      addMenuVisible:false,
      edit_menu_info:{
        parent: '',
        parent_id: '',
        id: '',
        name: '',
        url: '',
        has_child: '',
        sort: '',
        is_show: '1',
        authority: '',
        menu_icon: '',
      },
      edit_menu_default_info:{
        parent: '',
        parent_id: '',
        id: '',
        name: '',
        url: '',
        has_child: '',
        sort: '',
        is_show: '1',
        authority: '',
        menu_icon: '',
      },
      add_menu_info:{
        parent: '',
        parent_id: '',
        id: '',
        name: '',
        url: '',
        has_child: '',
        sort: '',
        is_show: '',
        authority: '',
        menu_icon: '',
      },
      add_menu_default_info:{
        parent: '',
        parent_id: '',
        id: '',
        name: '',
        url: '',
        has_child: '',
        sort: '',
        is_show: '',
        authority: '',
        menu_icon: '',
      },
      formLabelWidth: '120px'
    }
  },
  mounted() {
    this.getRootMenu()
  },

  methods:{
    getRootMenu(){
      this.menus = []
      this.$axios.post('/system/menu/')
      .then(({data:res}) =>{
        for(let i=0;i<res.data.length;i++)
        {
          this.menus.push(res.data[i])
          console.log(this.menus)
        }
      })
    },
    getChildMenu(tree, treeNode, resolve){
      let data = {}
      data['id'] = tree['id']
      let child = []
      this.$axios.post('/system/get_child_menu/', data)
      .then(({data:res}) =>{
        child = res.data
        if(child.length>0){
          resolve(child)
        }
        else {
          tree['has_child'] = false
        }

      })
      },
    editMenu(treeNode) {
      // 初始化编辑框
      this.edit_menu_info = clone(this.edit_menu_default_info)

      this.edit_menu_info = clone(treeNode)
      console.log(this.edit_menu_info)
      if(treeNode.is_show===1){
        this.edit_menu_info.is_show = '1'
      }
      else {
        this.edit_menu_info.is_show = '0'
      }
      this.editMenuVisible = true
    },
    updateMenu(){
      let data = {
        'menu_info': this.edit_menu_info
      }
      this.$axios.post('/system/update_menu/', data)
      .then(({data:res}) =>{
        this.editMenuVisible = false
        this.getRootMenu()
      })
    },
    editChildMenu(treeNode) {
      // 初始化菜单信息
      this.add_menu_info = clone(this.add_menu_default_info)

      this.add_menu_info.parent = treeNode.name
      this.add_menu_info.parent_id = treeNode.id
      this.addMenuVisible = true
    },
    addChildMenu() {
      let data = {
        'menu_info': this.add_menu_info
      }
      this.$axios.post('/system/add_child_menu/', data)
      .then(({data:res}) =>{
        this.addMenuVisible = false
        this.getRootMenu()
      })
    },
    editRootMenu(treeNode){
      // 初始化菜单信息
      this.add_menu_info = clone(this.add_menu_default_info)

      this.add_menu_info.parent = "root"
      this.add_menu_info.parent_id = 0
      this.addMenuVisible = true
    },
    deleteMenu(menu_id){
      Message('删除成功',menu_id+'删除成功')
      let data = {
        'menu_id': menu_id
      }
      this.$axios.post('/system/delete_menu/', data)
      .then(({data:res}) =>{

        this.getRootMenu()
      })
    },
  }
}
</script>

<style scoped>

</style>
