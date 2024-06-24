<template>
  <div id="i1">
    <link href="../../../static/css/style.css" rel="stylesheet" type="text/css" />
    <myhead></myhead>
    <myaside></myaside>
    <myfooter></myfooter>
  </div>
</template>
<style scoped>
</style>
<script>
import myhead from '@/views/app/head'
import myaside from '@/views/app/aside'
import myfooter from '@/views/app/footer'
export default {
  data () {
    return {}
  },
  components: {
    myhead,
    myaside,
    myfooter
  }
}
</script>
<script setup lang="ts">
</script>
