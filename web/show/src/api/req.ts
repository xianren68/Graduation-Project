// 重写axios方法
import axios from 'axios'
const req = axios.create({
    baseURL:"http://127.0.0.1:5000/",
    timeout:5000
})
// req.defaults.withCredentials = true
export default req