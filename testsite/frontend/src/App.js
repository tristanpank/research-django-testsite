import axios from 'axios';
import { useState } from 'react';
import Login from './components/Login';
import BlogPosts from './components/BlogPosts';


function App() {
  const onClick = (usernameInput="testuser", passwordInput="testing") => {
    axios.post('http://127.0.0.1:8000/api-token/', {
      username: usernameInput,
      password: passwordInput
    }).then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    })
  }

  const testBlogClick = async () => {
    const config = {
      method: 'post',
      url: `http://127.0.0.1:8000/api/`,
      headers: { 
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjgzMjEwMTIwLCJpYXQiOjE2ODMyMDk4MjAsImp0aSI6IjkwODA5MWFhZThlYjQxZTNiYmZmZjY2ODVjN2QwYzNkIiwidXNlcl9pZCI6Mn0.JEXuS4zmXdbu37iba1pqY0XdzHsGXA4JTFojmcxoi-A'
      },
      data : {
        'text': 'axios test'
      },
    };
    const { data } = await axios(config);
    console.log(data);
  }

  const testCreateUserClick = async () => {
    const config = {
      method: 'post',
      url: 'http://127.0.0.1:8000/api/users/create/',
      data: {
        'username': 'axiosuser',
        'password': 'testing'
      }
    };
    const { data } = await axios(config);
    console.log(data);
    onClick(data.username, "testing");
  }
  
  const [user, setUser] = useState(null);

  if (user === null) {
    return <Login setUser={setUser} />
  } else {
    return (
      <>
        <div>Logged in</div>
        <BlogPosts user={user} setUser={setUser} />
      </>
    )
  }

}

export default App;
