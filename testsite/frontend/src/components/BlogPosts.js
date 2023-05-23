import { useState, useEffect } from 'react';
import axios from 'axios';


function BlogPostsList({ user, triggerUseEffect }) {
  const [allBlogPosts, setAllBlogPosts] = useState([]);
  
  
  useEffect(() => {
    async function getPosts() {
      const config = {
        method: "get",
        url: "http://127.0.0.1:8000/api/"
      }
      const { data } = await axios(config);
      // console.log(data);
      return data;
    }

    getPosts().then((data) => {
      data = data.filter((post) => {
        return post.owner === user.username;
      });
      console.log(data);
      setAllBlogPosts(data);
    });
  }, [user, triggerUseEffect])
  
  // let posts = [];
  // posts = getPosts();
  // console.log(typeof(posts));
  // posts.filter((post) => {
  //   return post.owner === user.username;
  // });
  // console.log(posts);
  return (
    <div>{allBlogPosts.map((post) => {
      return <li key={post.id}>{post.text}</li>
    })}</div>
  );
}

function AddBlogPost({ user, setUser, setTriggerUseEffect, triggerUseEffect }) {
  const [postText, setPostText] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    console.log(postText);

    const config = {
      method: 'post',
      url: `http://127.0.0.1:8000/api/`,
      headers: { 
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + user.token.access
      },
      data : {
        'text': postText
      },
    };

    const { data } = await axios(config);
    console.log(data);
    console.log(user);
    setTriggerUseEffect(triggerUseEffect + 1);
  }

  return (
    <>
      <div>Add Posts</div>
      <form onSubmit={handleSubmit}>
        <label htmlFor='postText'>Post Text</label>
        <input type='text' id='postText' onChange={(e) => setPostText(e.target.value)}></input>
        <button type='submit'>Add Post</button>
      </form>
    </>
  )
}

function AddFilePost({user}) {
  const [data, setData] = useState({
    title: "",
    file_url: "",
  });
  const handleImageChange = (e) => {
    let newData = {...data};
    newData["file_url"] = e.target.files[0];
    newData["title"] = e.target.files[0].name;
    setData(newData);
    console.log(data);
    console.log(e.target.files[0])
  }

  async function handleSubmit(e) {
    e.preventDefault();
    console.log(e.target);
    let formData = new FormData();
    formData.append('title', data.title);
    formData.append('file_url', data.file_url);

    const config = {
      method: 'post',
      url: `http://127.0.0.1:8000/api/files/`,
      headers: { 
          'Content-Type': 'multipart/form-data',
          'Authorization': 'Bearer ' + user.token.access
      },
      data : formData,
    };

    const {responseData} = await axios(config);
    console.log(responseData);

  }

  return (
    <>
      <div>Add Files</div>
      <form onSubmit={handleSubmit}>
        <label htmlFor='fileURL'>Upload File</label>
        <input type='file' id='fileURL' accept='image/jpeg,image/png,image/svg,video/mp4' onChange={handleImageChange}></input> 
        <button type='submit'>Upload</button>
      </form>
    </>
  )
}


export default function BlogPosts({ user, setUser }) {
  const [triggerUseEffect, setTriggerUseEffect] = useState(0);
  
  return (
    <>
      <BlogPostsList user={user} triggerUseEffect={triggerUseEffect} />
      <AddBlogPost user={user} setUser={setUser} triggerUseEffect={triggerUseEffect} setTriggerUseEffect={setTriggerUseEffect} />
      <AddFilePost user={user} />
    </>
  )
}