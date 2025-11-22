import { useEffect, useState } from "react";

function Patients() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/patients")
      .then((res) => res.json())
      .then((data) => setPatients(data))
      .catch((err) => console.error("Error fetching patients:", err));
  }, []);

  return (
    <div>
      <h2>Patients</h2>
      <ul>
        {patients.map((patient) => (
          <li key={patient.id}>
            {patient.name} {patient.age ? `– Age ${patient.age}` : ""}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Patients;