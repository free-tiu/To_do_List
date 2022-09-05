import { createApp } from 'vue'
import './style.css'
import App from './App.vue'


//导入bootstrap样式
import 'bootstrap/dist/css/bootstrap.css'

//挂载到app对象 => index.html中到id="app"
createApp(App).mount('#app');