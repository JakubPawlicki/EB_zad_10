import axios from "axios";

export const axiosInstance= axios.create({
    baseURL: "https://eb-zad10-backend.azurewebsites.net"
})
