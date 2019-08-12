import axios from 'axios';
export default class Request {
    host:string = '/';

    requestDataJson() {
        return this.get('data.json');
    }
    private get(url:string) {
        return axios.get(this.host+url)
            .then(response =>{
                return response.data;
            })

    }
    private post(url:string) {
        return axios.get(this.host+url)
            .then(response =>{
                return response.data;
            })
    }
}