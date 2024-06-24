<template>
  <div>
    <myhead></myhead>
    <myaside></myaside>
    <div id="main" style="position:  absolute;top:60px;bottom:60px;left:200px;right: 0">
      <el-table
          :data="tableData"
          style="width: 100%"
          max-height="100%">
          <el-table-column
            fixed
            prop="id"
            label="id"
            width="150">
          </el-table-column>
          <el-table-column
            prop="password"
            label="密码"
            width="120">
          </el-table-column>
          <el-table-column
            prop="last_login"
            label="最后登录"
            width="120">
          </el-table-column>
          <el-table-column
            prop="username"
            label="用户名"
            width="120">
          </el-table-column>
          <el-table-column
            prop="create_time"
            label="创建时间"
            width="300">
          </el-table-column>
          <el-table-column
            fixed="right"
            label="操作"
            width="120">
            <template slot-scope="scope">
              <el-button
                @click.native.prevent="deleteRow(scope.$index, tableData)"
                type="text"
                size="small">
                移除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
    </div>
    <myfooter></myfooter>
  </div>
</template>
<script>
import myhead from '@/views/app/head'
import myaside from '@/views/app/aside'
import myfooter from '@/views/app/footer'
import axios from 'axios'

export default {
  data () {
    return {
      tableData: [],
      // baseURL: 'http://192.168.182.128:8000',
      baseURL: 'http://127.0.0.1:8000/',
      // ====分页相关变量====
      total: 100, // 数据总行数
      currentpage: 1, // 当前所在页
      pagesize: 10, // 每页显示多少行
      username: '',
      password: '',
      mobile: '',
      err_username: '',
      err_password: '',
      err_mobile: ''
    }
  },
  components: {
    myhead,
    myaside,
    myfooter
  },
  mounted () {
    // 自动加载数据
    this.get_users()
  },
  methods: {
    get_users () {
      let that = this
      // 使用Axios实现jax请求
      axios
        .get(this.baseURL + 'users/users/')
        .then(function (res) {
          if (res.data.code === 1) {
            // 把数据给表格
            that.tableData = res.data.data
            that.$message({
              message: '数据加载成功',
              type: 'success'
            })
          } else {
            that.$message.error(res.data.msg)
          }
        })
        .catch(function (res) {
          console.log(res)
        })
    }
  }
}
</script>

<style scoped>
@import "../../../static/css/login.css";
</style>
