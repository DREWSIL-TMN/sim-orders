import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [orders, setOrders] = useState([]);
  const [tab, setTab] = useState("all");

  useEffect(() => {
    let url = "http://localhost:8000/api/orders/";
    if (tab === "new") url += "?status=1";
    else if (tab === "completed") url += "?status=2";

    axios.get(url)
      .then(res => setOrders(res.data))
      .catch(err => console.error(err));
  }, [tab]); // 👈 useEffect срабатывает при смене tab

  return (
    <div style={{ padding: "24px", fontFamily: "Segoe UI, sans-serif", backgroundColor: "#f9f9f9", minHeight: "100vh" }}>
      <h1 style={{ marginBottom: "16px" }}>Список заказов</h1>
  
      <div style={{ marginBottom: "20px", display: "flex", gap: "10px" }}>
        <button onClick={() => setTab("all")}>Все</button>
        <button onClick={() => setTab("new")}>Новые</button>
        <button onClick={() => setTab("completed")}>Выполненные</button>
      </div>
  
      {orders.map(order => (
        <div
          key={order.id}
          style={{
            backgroundColor: "#fff",
            border: "1px solid #ddd",
            borderRadius: "8px",
            padding: "16px",
            marginBottom: "12px",
            boxShadow: "0 1px 3px rgba(0, 0, 0, 0.05)"
          }}
        >
          <p><strong>Менеджер:</strong> {order.manager.name} ({order.manager.number})</p>
          <p><strong>Краткий адрес:</strong> {order.adresse.location}</p>
          <p><strong>Полный адрес:</strong> {order.adresse.caption}</p>
          <p><strong>Создан:</strong> {new Date(order.time_create).toLocaleString()}</p>
          <p><strong>Статус:</strong> {
            order.status === 1 ? "Новый" :
            order.status === 2 ? "Выполнен" : "Другой"
          }</p>
        </div>
      ))}
    </div>
  );
}

export default App;
