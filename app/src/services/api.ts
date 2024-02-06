import axios from 'axios'

const baseUrl = 'http://localhost:8001'

const api = axios.create({
	baseURL: baseUrl,
})
  
export default api