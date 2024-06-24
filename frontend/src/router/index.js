import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      name: 'index',
      path: '/index',
      component: () => import('@/views/index/index'),
      meta: {
        title: '商城首页'
      }
    },
    {
      name: 'users',
      path: '/users',
      component: () => import('@/views/user/users'),
      meta: {
        title: '用户列表'
      }
    },
    {
      name: 'login',
      path: '/login',
      component: () => import('@/views/user/login'),
      meta: {
        title: '用户登录'
      }
    },
    {
      name: 'reg',
      path: '/reg',
      component: () => import('@/views/user/reg'),
      meta: {
        title: '用户注册'
      }
    }
  ]
})
