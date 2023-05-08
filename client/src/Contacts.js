import React, {useState, useEffect} from "react";
import './index.css';

function Contacts() {
    const [data, setData] = useState([{}]);
  
    useEffect(() => {
        fetch("/profiles").then(
          res => res.json()
        ).then(
          data => {
            setData(data);
            console.log(data)
          }
        )
      }, []);
    
    return (
    <div className='content'>
        <div className='post'>
            <div className='user-name'>
                Khadar
            </div>
            <div className='user-city'>
                Lawrenceville, Georgia
            </div>
        </div>
        <div className='post'>
            <div className='user-name'>
                Philip
            </div>
            <div className='user-city'>
                Anaheim, California
            </div>
        </div>
        <div className='post'>
            <div className='user-name'>
                Marius
            </div>
            <div className='user-city'>
                Kaunas, Lithuania
            </div>
        </div>
        <div className='post'>
            <div className='user-name'>
                Fredrick
            </div>
            <div className='user-city'>
                Charlottesville, Virginia
            </div>
        </div>
        <div className='post'>
            <div className='user-name'>
                Hamel
            </div>
            <div className='user-city'>
                Bucharest, Romania
            </div>
        </div>
    </div>
    )
}

export default Contacts