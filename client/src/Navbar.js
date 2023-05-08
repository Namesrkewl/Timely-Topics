import './index.css';

function Navbar() {
    return (
        <div className='navbar'>
            <div className='brand'>
                Timely Topics
            </div>
            <a href='/'>
                <img src='/home.png'/>
            </a> 
            <a href='/contacts'>
                <img src='/contacts.jpg'/>
            </a>
            <a href='/profile'>
                <img src='/profile.png'/>
            </a>
        </div>
    )
}

export default Navbar