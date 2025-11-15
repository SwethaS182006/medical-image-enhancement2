import React from 'react';
import Sidebar from './components/Sidebar';
import MetricsPanel from './components/MetricsPanel';
import UploadImage from './components/UploadImage';
import ClinicalNote from './components/ClinicalNote';
import ICDMapper from './components/ICDMapper';

function App() {
  return (
    <div style={{ display: 'flex' }}>
      <Sidebar />
      <main style={{ padding: '20px', flex: 1 }}>
        <h1>EHR Dashboard</h1>
        <MetricsPanel />
        <UploadImage />
        <ClinicalNote />
        <ICDMapper />
      </main>
    </div>
  );
}

export default App;