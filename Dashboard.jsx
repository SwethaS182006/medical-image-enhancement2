import { useEffect, useState } from "react";

function Dashboard() {
  const [dashboard, setDashboard] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/dashboard")
      .then((res) => res.json())
      .then((data) => setDashboard(data))
      .catch((err) => console.error("Error fetching dashboard:", err));
  }, []);

  if (!dashboard) return <p>Loading...</p>;

  return (
    <div>
      <h2>Dashboard</h2>
      <ul>
        <li>Images Enhanced: {dashboard.images_enhanced}</li>
        <li>Notes Generated: {dashboard.notes_generated}</li>
        <li>ICD Codes Suggested: {dashboard.icd_codes}</li>
        <li>Active Patients: {dashboard.active_patients}</li>
        <li>Uptime: {dashboard.uptime}</li>
      </ul>
    </div>
  );
}

export default Dashboard;