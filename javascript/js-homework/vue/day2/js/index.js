new Vue({
    el: "#todoapp",
    data: {
        cur: null,
        todos: [{
            id: 1,
            title: '吃饭',
            completed: false
        }, {
            id: 2,
            title: '睡觉',
            completed: false
        }, {
            id: 3,
            title: '打豆豆',
            completed: true
        }]
    },
    methods: {
        addTodo: function(event) {
            var todoText = event.target.value.trim();
            if (!todoText.length) {
                return;
            }
            const todoId = this.todos.length == 0 ? 1 : this.todos.length + 1;
            this.todos.push({
                id: todoId,
                title: todoText,
                completed: false
            });
            console.log(this.todos);
        },
        delTodo: function(index) {
            this.todos.splice(index, 1);
        },
        edit: function() {

        }
    }
})