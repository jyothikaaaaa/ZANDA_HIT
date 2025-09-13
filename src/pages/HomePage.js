import React, { useState, useEffect } from 'react';
import { GoogleMap, LoadScript, Marker, InfoWindow } from '@vis.gl/react-google-maps';
import { useProjects } from '../contexts/ProjectContext';
import FilterPanel from '../components/FilterPanel';
import ProjectCard from '../components/ProjectCard';
import { MapPin, Filter, X } from 'lucide-react';

const HomePage = () => {
  const { filteredProjects, loading, filters, updateFilters } = useProjects();
  const [selectedProject, setSelectedProject] = useState(null);
  const [showFilterPanel, setShowFilterPanel] = useState(false);
  const [mapCenter, setMapCenter] = useState({
    lat: parseFloat(process.env.REACT_APP_BENGALURU_LAT) || 12.9716,
    lng: parseFloat(process.env.REACT_APP_BENGALURU_LNG) || 77.5946
  });

  const getMarkerColor = (status) => {
    switch (status) {
      case 'Completed':
        return '#28a745';
      case 'In Progress':
        return '#ffc107';
      case 'Pending':
        return '#dc3545';
      default:
        return '#6c757d';
    }
  };

  const getRiskColor = (risk) => {
    switch (risk) {
      case 'High':
        return '#dc3545';
      case 'Medium':
        return '#ffc107';
      case 'Low':
        return '#28a745';
      default:
        return '#6c757d';
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-screen">
        <div className="loading-spinner"></div>
        <span className="ml-2 text-gray-600">Loading projects...</span>
      </div>
    );
  }

  return (
    <div className="relative h-screen">
      {/* Google Map */}
      <LoadScript
        googleMapsApiKey={process.env.REACT_APP_GOOGLE_MAPS_API_KEY}
        libraries={['places']}
      >
        <GoogleMap
          mapContainerStyle={{ width: '100%', height: '100%' }}
          center={mapCenter}
          zoom={12}
          options={{
            styles: [
              {
                featureType: 'poi',
                elementType: 'labels',
                stylers: [{ visibility: 'off' }]
              }
            ]
          }}
        >
          {filteredProjects.map((project) => (
            <Marker
              key={project.id}
              position={{
                lat: project.geoPoint?.latitude || 0,
                lng: project.geoPoint?.longitude || 0
              }}
              onClick={() => setSelectedProject(project)}
              icon={{
                url: `data:image/svg+xml;charset=UTF-8,${encodeURIComponent(`
                  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <circle cx="12" cy="12" r="10" fill="${getMarkerColor(project.status)}" stroke="white" stroke-width="2"/>
                    <circle cx="12" cy="12" r="4" fill="white"/>
                  </svg>
                `)}`,
                scaledSize: new window.google.maps.Size(24, 24),
                anchor: new window.google.maps.Point(12, 12)
              }}
            />
          ))}

          {selectedProject && (
            <InfoWindow
              position={{
                lat: selectedProject.geoPoint?.latitude || 0,
                lng: selectedProject.geoPoint?.longitude || 0
              }}
              onCloseClick={() => setSelectedProject(null)}
            >
              <div className="p-2 max-w-xs">
                <h3 className="font-bold text-lg mb-2">{selectedProject.projectName}</h3>
                <p className="text-sm text-gray-600 mb-2">{selectedProject.description}</p>
                <div className="flex items-center space-x-2 mb-2">
                  <span className={`status-badge status-${selectedProject.status.toLowerCase().replace(' ', '-')}`}>
                    {selectedProject.status}
                  </span>
                  {selectedProject.predictedDelayRisk && (
                    <span 
                      className="text-xs font-semibold px-2 py-1 rounded"
                      style={{ 
                        backgroundColor: getRiskColor(selectedProject.predictedDelayRisk) + '20',
                        color: getRiskColor(selectedProject.predictedDelayRisk)
                      }}
                    >
                      Risk: {selectedProject.predictedDelayRisk}
                    </span>
                  )}
                </div>
                <p className="text-xs text-gray-500">
                  Ward: {selectedProject.wardNumber} | {selectedProject.department}
                </p>
                {selectedProject.budget && (
                  <p className="text-xs text-gray-500">
                    Budget: ₹{selectedProject.budget}
                  </p>
                )}
              </div>
            </InfoWindow>
          )}
        </GoogleMap>
      </LoadScript>

      {/* Filter Toggle Button */}
      <button
        onClick={() => setShowFilterPanel(!showFilterPanel)}
        className="absolute top-4 left-4 z-10 bg-white hover:bg-gray-50 text-gray-700 px-4 py-2 rounded-lg shadow-lg flex items-center space-x-2 transition-colors"
      >
        <Filter className="h-4 w-4" />
        <span>Filters</span>
      </button>

      {/* Filter Panel */}
      {showFilterPanel && (
        <div className="absolute top-4 left-4 z-20">
          <FilterPanel
            filters={filters}
            onFiltersChange={updateFilters}
            onClose={() => setShowFilterPanel(false)}
          />
        </div>
      )}

      {/* Project List (Mobile) */}
      <div className="md:hidden absolute bottom-0 left-0 right-0 bg-white max-h-64 overflow-y-auto">
        <div className="p-4 border-t">
          <h3 className="font-bold text-lg mb-3">Projects ({filteredProjects.length})</h3>
          <div className="space-y-2">
            {filteredProjects.slice(0, 5).map((project) => (
              <ProjectCard
                key={project.id}
                project={project}
                onClick={() => setSelectedProject(project)}
              />
            ))}
            {filteredProjects.length > 5 && (
              <p className="text-sm text-gray-500 text-center">
                +{filteredProjects.length - 5} more projects
              </p>
            )}
          </div>
        </div>
      </div>

      {/* Desktop Project List */}
      <div className="hidden md:block absolute top-4 right-4 w-80 max-h-96 overflow-y-auto bg-white rounded-lg shadow-lg">
        <div className="p-4">
          <h3 className="font-bold text-lg mb-3">Projects ({filteredProjects.length})</h3>
          <div className="space-y-2">
            {filteredProjects.slice(0, 10).map((project) => (
              <ProjectCard
                key={project.id}
                project={project}
                onClick={() => setSelectedProject(project)}
              />
            ))}
            {filteredProjects.length > 10 && (
              <p className="text-sm text-gray-500 text-center">
                +{filteredProjects.length - 10} more projects
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
