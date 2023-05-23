import axios from 'axios';
import { useState } from 'react';

async function apiLogin(username, password) {
  const config = {
    method: "post",
    url: "http://127.0.0.1:8000/api-token/",
    data: {
      "username": username,
      "password": password,
    }
  }
  const { data } = await axios(config);
  console.log(data);
  return data;
} 

export default function Login({setUser}) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [token, setToken] = useState("");
  
  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(username);
    console.log(password);
    const tokenData = await apiLogin(username, password);
    setToken(tokenData);
    const user = {
      "username": username,
      "password": password,
      "token": tokenData
    }
    setUser(user);
  }

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor='username'>Username</label>
      <input type='text' id='username' onChange={(e) => {setUsername(e.target.value)}}></input>
      <label htmlFor='password'>Password</label>
      <input type='password' id='password' onChange={(e) => {setPassword(e.target.value)}}></input>
      <button type='submit'>Submit</button>
    </form>
  );
}