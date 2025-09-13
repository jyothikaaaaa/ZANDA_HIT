import React from 'react';
import { X, MapPin, Building, DollarSign } from 'lucide-react';

const FilterPanel = ({ filters, onFiltersChange, onClose }) => {
  const bengaluruWards = [
    'Ward 1', 'Ward 2', 'Ward 3', 'Ward 4', 'Ward 5', 'Ward 6', 'Ward 7', 'Ward 8',
    'Ward 9', 'Ward 10', 'Ward 11', 'Ward 12', 'Ward 13', 'Ward 14', 'Ward 15', 'Ward 16',
    'Ward 17', 'Ward 18', 'Ward 19', 'Ward 20', 'Ward 21', 'Ward 22', 'Ward 23', 'Ward 24',
    'Ward 25', 'Ward 26', 'Ward 27', 'Ward 28', 'Ward 29', 'Ward 30', 'Ward 31', 'Ward 32',
    'Ward 33', 'Ward 34', 'Ward 35', 'Ward 36', 'Ward 37', 'Ward 38', 'Ward 39', 'Ward 40',
    'Ward 41', 'Ward 42', 'Ward 43', 'Ward 44', 'Ward 45', 'Ward 46', 'Ward 47', 'Ward 48',
    'Ward 49', 'Ward 50', 'Ward 51', 'Ward 52', 'Ward 53', 'Ward 54', 'Ward 55', 'Ward 56',
    'Ward 57', 'Ward 58', 'Ward 59', 'Ward 60', 'Ward 61', 'Ward 62', 'Ward 63', 'Ward 64',
    'Ward 65', 'Ward 66', 'Ward 67', 'Ward 68', 'Ward 69', 'Ward 70', 'Ward 71', 'Ward 72',
    'Ward 73', 'Ward 74', 'Ward 75', 'Ward 76', 'Ward 77', 'Ward 78', 'Ward 79', 'Ward 80',
    'Ward 81', 'Ward 82', 'Ward 83', 'Ward 84', 'Ward 85', 'Ward 86', 'Ward 87', 'Ward 88',
    'Ward 89', 'Ward 90', 'Ward 91', 'Ward 92', 'Ward 93', 'Ward 94', 'Ward 95', 'Ward 96',
    'Ward 97', 'Ward 98', 'Ward 99', 'Ward 100', 'Ward 101', 'Ward 102', 'Ward 103', 'Ward 104',
    'Ward 105', 'Ward 106', 'Ward 107', 'Ward 108', 'Ward 109', 'Ward 110', 'Ward 111', 'Ward 112',
    'Ward 113', 'Ward 114', 'Ward 115', 'Ward 116', 'Ward 117', 'Ward 118', 'Ward 119', 'Ward 120',
    'Ward 121', 'Ward 122', 'Ward 123', 'Ward 124', 'Ward 125', 'Ward 126', 'Ward 127', 'Ward 128',
    'Ward 129', 'Ward 130', 'Ward 131', 'Ward 132', 'Ward 133', 'Ward 134', 'Ward 135', 'Ward 136',
    'Ward 137', 'Ward 138', 'Ward 139', 'Ward 140', 'Ward 141', 'Ward 142', 'Ward 143', 'Ward 144',
    'Ward 145', 'Ward 146', 'Ward 147', 'Ward 148', 'Ward 149', 'Ward 150', 'Ward 151', 'Ward 152',
    'Ward 153', 'Ward 154', 'Ward 155', 'Ward 156', 'Ward 157', 'Ward 158', 'Ward 159', 'Ward 160',
    'Ward 161', 'Ward 162', 'Ward 163', 'Ward 164', 'Ward 165', 'Ward 166', 'Ward 167', 'Ward 168',
    'Ward 169', 'Ward 170', 'Ward 171', 'Ward 172', 'Ward 173', 'Ward 174', 'Ward 175', 'Ward 176',
    'Ward 177', 'Ward 178', 'Ward 179', 'Ward 180', 'Ward 181', 'Ward 182', 'Ward 183', 'Ward 184',
    'Ward 185', 'Ward 186', 'Ward 187', 'Ward 188', 'Ward 189', 'Ward 190', 'Ward 191', 'Ward 192',
    'Ward 193', 'Ward 194', 'Ward 195', 'Ward 196', 'Ward 197', 'Ward 198', 'Ward 199', 'Ward 200'
  ];

  const departments = [
    'BBMP', 'BDA', 'BMRCL', 'BWSSB', 'BESCOM', 'KUIDFC', 'BMTC', 'PWD', 'Karnataka Government'
  ];

  const statuses = ['Completed', 'In Progress', 'Pending', 'Cancelled'];

  const budgetRanges = [
    { label: 'Under ₹1 Lakh', value: '0-100000' },
    { label: '₹1 Lakh - ₹10 Lakh', value: '100000-1000000' },
    { label: '₹10 Lakh - ₹1 Crore', value: '1000000-10000000' },
    { label: '₹1 Crore - ₹10 Crore', value: '10000000-100000000' },
    { label: 'Above ₹10 Crore', value: '100000000-999999999' }
  ];

  const handleFilterChange = (filterType, value) => {
    onFiltersChange({ [filterType]: value });
  };

  const clearFilters = () => {
    onFiltersChange({
      wardNumber: '',
      department: '',
      status: '',
      budgetRange: ''
    });
  };

  return (
    <div className="bg-white rounded-lg shadow-lg p-6 w-80 max-h-96 overflow-y-auto">
      <div className="flex justify-between items-center mb-4">
        <h3 className="text-lg font-bold text-gray-900">Filter Projects</h3>
        <button
          onClick={onClose}
          className="text-gray-500 hover:text-gray-700"
        >
          <X className="h-5 w-5" />
        </button>
      </div>

      {/* Ward Filter */}
      <div className="mb-4">
        <label className="flex items-center text-sm font-medium text-gray-700 mb-2">
          <MapPin className="h-4 w-4 mr-2" />
          BBMP Ward
        </label>
        <select
          value={filters.wardNumber}
          onChange={(e) => handleFilterChange('wardNumber', e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        >
          <option value="">All Wards</option>
          {bengaluruWards.map((ward) => (
            <option key={ward} value={ward}>
              {ward}
            </option>
          ))}
        </select>
      </div>

      {/* Department Filter */}
      <div className="mb-4">
        <label className="flex items-center text-sm font-medium text-gray-700 mb-2">
          <Building className="h-4 w-4 mr-2" />
          Department
        </label>
        <select
          value={filters.department}
          onChange={(e) => handleFilterChange('department', e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        >
          <option value="">All Departments</option>
          {departments.map((dept) => (
            <option key={dept} value={dept}>
              {dept}
            </option>
          ))}
        </select>
      </div>

      {/* Status Filter */}
      <div className="mb-4">
        <label className="text-sm font-medium text-gray-700 mb-2 block">
          Status
        </label>
        <select
          value={filters.status}
          onChange={(e) => handleFilterChange('status', e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        >
          <option value="">All Statuses</option>
          {statuses.map((status) => (
            <option key={status} value={status}>
              {status}
            </option>
          ))}
        </select>
      </div>

      {/* Budget Range Filter */}
      <div className="mb-4">
        <label className="flex items-center text-sm font-medium text-gray-700 mb-2">
          <DollarSign className="h-4 w-4 mr-2" />
          Budget Range
        </label>
        <select
          value={filters.budgetRange}
          onChange={(e) => handleFilterChange('budgetRange', e.target.value)}
          className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
        >
          <option value="">All Budgets</option>
          {budgetRanges.map((range) => (
            <option key={range.value} value={range.value}>
              {range.label}
            </option>
          ))}
        </select>
      </div>

      {/* Clear Filters Button */}
      <button
        onClick={clearFilters}
        className="w-full bg-gray-200 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-300 transition-colors"
      >
        Clear All Filters
      </button>
    </div>
  );
};

export default FilterPanel;
