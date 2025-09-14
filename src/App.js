import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import { ProjectProvider } from './contexts/ProjectContext';
import Navbar from './components/Navbar';
import HomePage from './pages/HomePage';
import ProjectDetailPage from './components/ProjectDetailPage';
import ProjectTrackingPage from './pages/ProjectTrackingPage';
import Login from './pages/Login';
import './App.css';

function App() {
  return (
    <AuthProvider>
      <ProjectProvider>
        <Router>
          <div className="App">
            <Navbar />
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/projects" element={<ProjectTrackingPage />} />
              <Route path="/project/:id" element={<ProjectDetailPage />} />
              <Route path="/login" element={<Login />} />
            </Routes>
          </div>
        </Router>
      </ProjectProvider>
    </AuthProvider>
  );
}

export default App;
