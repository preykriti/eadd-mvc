const loadTodo = async () => {
  try {
    const response = await fetch("http://localhost:5000/mytask");
    const todo = await response.json();
    const list = document.getElementById("todo-list");
    list.innerHTML = todo.map((todos) => `<li>${todos.title}</li>`);
  } catch (error) {
    console.log(error);
  }
};

loadTodo();
