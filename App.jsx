import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/todos")
      .then(res => setTodos(res.data))
      .catch(err => setTodos([
          {"id":1,"task":"Simple Task","completed":false},
          {"id":2,"task":"MERN Stack Project Completed","completed":true},
          {"id":3,"task":"Python Project Finished","completed":true},
          {"id":4,"task":"Write Report","completed":false}
      ]));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>TODO App</h1>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            {todo.task} - {todo.completed ? "Done ✅" : "Pending ⏳"}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;