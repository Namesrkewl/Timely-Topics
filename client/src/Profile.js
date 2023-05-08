import React, {useState, useEffect} from "react";
import './index.css';

function Profile() {
    const [name, setName] = useState('');
    const [city, setCity] = useState('');
    const [state, setState] = useState('');

    const updateProfile = () => {
        fetch("/user")
    }
    


    return (
        <div className='content'>
            <form>
                <label>Enter your name:
                    <input type='text' value={name} onChange={(e) => setName(e.target.value)}/>
                </label>    
                <label>Enter your city:
                    <input type='text' value={city} onChange={(e) => setCity(e.target.value)}/>
                </label>
                <label>Enter your state:
                    <input type='text' value={state} onChange={(e) => setState(e.target.value)}/>
                </label>
            </form>
        </div>
    )
}

export default Profile