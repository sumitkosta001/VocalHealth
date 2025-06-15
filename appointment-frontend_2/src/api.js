import axios from 'axios';

// Automatically picks up the API URL from environment variables
// Falls back to localhost if not set (for local development)
const API = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://127.0.0.1:8000',
});

// Upload voice file to the backend
export const uploadVoice = async (file) => {
  const formData = new FormData();
  formData.append('audio', file);

  return await API.post('/appointments/voice', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  });
};

// Create a new appointment
export const createAppointment = async (data) => {
  return await API.post('/appointments/create', data);
};
