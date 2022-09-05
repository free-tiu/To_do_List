<script setup>
    /**
     * 使用模块化方式 从vue中导入ref，创建todo的数据，创建form的数据
     */
    import {onMounted, ref, reactive, computed} from 'vue';
    let todos = ref([]);
    let form = reactive({
        title: '',
        done: false,
    });

    const undone_count = computed(() =>{
        return todos.length;
    });

    //1.请求服务器数据
    const fetchData = () => {
        fetch(`http://127.0.0.1:5000/todo`).then(res => {
            return res.json();
        }).then((data) => {
            console.log(data);
            todos.value = data;
            console.log(todos)
        });
    };

    //2.切换任务的完成状态
    const change_todo_status = (item) => {
        console.log(JSON.stringify(item));
        fetch(`http://127.0.0.1:5000/todo/${item.id}`,{
            method: 'put',
            body: JSON.stringify(item),
            headers:{
                'Content-Type': 'application/json',
            },
        }).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log(data);
        });
    };

    //3.添加任务
    const add_todo = () => {
        fetch(`http://127.0.0.1:5000/todo`,{
            method: 'POST',
            body: JSON.stringify(form),
            headers:{
                'Content-Type': 'application/json',
            },
        }).then((response) => {
            return response.json();
        }).then((data) => {
            console.log(data);
            form.title ='';
            fetchData();
        });
    };

    //4.删除任务
    const delete_todo = (index) => {
        fetch(`http://127.0.0.1:5000/todo/${index}`,{
            method: 'DELETE',
            body: JSON.stringify({id: index})
        }).then((response) => {
            return response.json();
        }).then((data) => {
            console.log(data);
            fetchData();
        });
    };

    //当页面渲染完之后，加载fetchData函数
    onMounted(() => {
        fetchData()
    })

</script>

<template>
    <div class="container mt-3">
        <div class="row">
            <div class="col-6 m-auto" style="width: 100%;">
                <form action="/add_todo" method="post">
                    <div class="input-group mb-3">
                        <!-- 使用form的数据 -->
                        <input type="text" class="form-control"
                               placeholder="请输入任务" name="title"
                               v-model="form.title">
                        <button type="submit" class="btn btn-primary" @click.prevent="add_todo">添加事项</button>
                    </div>
                </form>
            </div>
        </div>

    <div class="row">
        <div class="col-6 m-auto">
            <div class="list-group mb-3">
                <label class="list-group-item" v-for="todo in todos">
                    <!-- 使用todo的数据 -->
                    <input class="form-check-input me-1 todo-input"
                           type="checkbox" v-if="todo.done" checked
                           value="{{ todo.id }}"
                           @change="change_todo_status(todo)">

                    <input class="form-check-input me-1 todo-input"
                           type="checkbox" v-if="!todo.done"
                           value="{{ todo.id }}"
                           @change="change_todo_status(todo)">

                    <span class="text-muted">{{ todo.title }}</span>
                    <a class="text-decoration-none float-end" @click="delete_todo(todo.id)">删除</a>
                </label>
            </div>
        </div>
    </div>

    <div class="row">
        <div class="col-6 m-auto d-flex justify-content-between" style="width: 100%;">
            <button type="button" class="btn text-decoration-none" disabled>{{ undone_count }}条剩余</button>

            <div class="btn-group">
                <a href="/?key=all" class="btn btn-outline-primary {% if key=='all' %}activa{% endif %}">
                  全部
                </a>
                <a href="/?key=undone" class="btn btn-outline-primary {% if key=='undone' %}activa{% endif %}">
                  未完成
                </a>
                <a href="/?key=done" class="btn btn-outline-primary {% if key=='done' %}activa{% endif %}">
                  已完成
                </a>
            </div>
            <a href="/clear_done?key=done" class="btn btn-link text-decoration-none"> 清除已完成 </a>
        </div>
    </div>
  </div>
</template>

<style>
    .col-6{
        flex: 0 0 auto;
        width: 100%;
    }
    #app{
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
        margin-top: 60px;
    }
</style>
