<template>
  <div id="header" class="new_header" style="width:100%;">
    <el-container>
        <el-header><ul>
          <li id="ECS_MEMBERZONE" v-if="userinfo">
            <el-row :gutter="4">
              <el-col :span="4" style="min-height:1px;font-size: 36px">XXX管理系统</el-col>
              <el-col :span="15" style="min-height:1px;"></el-col>
              <el-col :span="1"><div class="grid-content bg-purple"><router-link :to="'/profile'">{{ userinfo.name }}</router-link></div></el-col>
              <el-col :span="1"><div class="grid-content bg-purple"><s>|</s></div></el-col>
              <el-col :span="1"><div class="grid-content bg-purple"><a @click="logout">退出</a></div></el-col>
              <el-col :span="2" style="min-height:1px;"></el-col>
            </el-row>
          </li>
          <li id="ECS_MEMBERZONE" v-else>
            <el-row :gutter="4">
              <el-col :span="4" style="min-height:1px;font-size: 36px">XXX管理系统</el-col>
              <el-col :span="15" style="min-height:1px;"></el-col>
              <el-col :span="1"><div class="grid-content bg-purple"><router-link :to="'/login'">请登录</router-link></div></el-col>
              <el-col :span="1"><div class="grid-content bg-purple"><s>|</s></div></el-col>
              <el-col :span="1"><div class="grid-content bg-purple"><router-link :to="'/reg'">免费注册</router-link></div></el-col>
              <el-col :span="2" style="min-height:1px;"></el-col>
            </el-row>
          </li>
        </ul>
        </el-header>
    </el-container>
<!--<div class="line"></div>-->
  </div>
</template>
<style scoped>
html,body,#app,.el-container{
  height: 100%;
}
.el-header {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
}
ul {
  list-style-type: none;
}
.router-link{
  text-decoration: none;
  color: black;
}
a {
  text-decoration: none;
  color: black;
}

.line {
  height: 1px;
  margin-top: 10px; /* 线与其他元素的距离 */
  margin-left: 40px; /* 左侧留白 */
  margin-right: 40px; /* 右侧留白 */
  background: linear-gradient(to right, black, gray);
}
</style>

<script>
import { mapGetters } from 'vuex'
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css' // 引入Element UI样式

Vue.use(ElementUI)
export default {
  data () {
    return {
      showmenu: false,
      allMenu: [],
      showsubmenu: -1, // 菜单显示控制
      first: false,
      current: false,
      showCart: false
    }
  },
  methods: {
    getAllMenu () {
    },
    logout () {
      this.$store.dispatch('delUser')
    }
  },
  computed: {
    ...mapGetters({
      userinfo: 'userinfo'
    })
  },
  created () {
    this.getAllMenu()
    // console.log(this.cart_lists)
  }
}
</script>
