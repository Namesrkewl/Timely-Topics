import React, {useState, useEffect} from "react";
import './index.css';


function Home() {
    const [data, setData] = useState([{}]);
  
    useEffect(() => {
      fetch("/news/Khadar").then(
        res => res.json()
      ).then(
        data => {
          setData(data);
        }
      )
    }, []);
  
    return (
      <div className='content'>
          {(typeof data.news === 'undefined') ? (
              <div className="loading">Loading...</div>
              ) : (
              data.news.map((post, id) => (
                  <div className='post' key={id}>
                      <div className='post-title'>
                          <a href={post.link} target='_blank'>{post.title}</a>
                      </div>
                      <div className='post-time'>
                          {post.time}
                      </div>
                  </div>
              ))
          )}
      </div>
    )
}

export default Home