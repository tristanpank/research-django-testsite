import {useState, useEffect} from 'react';
import axios from 'axios';

export default function VideoDisplay() {
  const [videoData, setVideoData] = useState([])

  useEffect(() => {
    async function getVideos() {
      const config = {
        method: "get",
        url: "http://127.0.0.1:8000/api/files/"
      }

      const response = await axios(config);
      return response.data;
    }

    getVideos().then((data) => {
      console.log(data);
      setVideoData(data);
    })
  }, [])

  return (
    <>
      {(videoData.length != 0) ? <img src={videoData[4].file_url}></img> : <></>}
      {(videoData.length != 0) ? <video width="320" height="240" controls><source src={videoData[8].file_url}></source></video> : <></>}
      
    </>
  )
}