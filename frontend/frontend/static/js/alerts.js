async function loadTodayAlerts() {
  const res = await fetch("/alerts/list");
  const alerts = await res.json();

  const alertList = document.getElementById("alert-list");
  alertList.innerHTML = "";

  alerts.forEach((alert) => {
    const item = document.createElement("div");
    item.className = "alert-item";
    item.innerHTML = `
      <div><strong>유형:</strong> ${alert.alert_type}</div>
      <div><strong>시간:</strong> ${alert.detected_at}</div>
    `;
    alertList.appendChild(item);
  });
}

document.addEventListener("DOMContentLoaded", loadTodayAlerts);
