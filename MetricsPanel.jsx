import React, { useEffect, useState } from 'react';
import axios from 'axios';

const MetricsPanel = () => {
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    axios.get('/api/dashboard_metrics')
      .then(res => setMetrics(res.data));
  }, []);

  return (
    <section>
      <h2>Metrics Overview</h2>
      <ul>
        <li>Images Enhanced: {metrics.images_enhanced}</li>
        <li>Notes Generated: {metrics.notes_generated}</li>
        <li>ICD-10 Codes: {metrics.icd_codes}</li>
        <li>Active Patients: {metrics.active_patients}</li>
      </ul>
    </section>
  );
};

export default MetricsPanel;