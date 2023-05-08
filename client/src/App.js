import Navbar from './Navbar'
import Home from './Home.js'
import Contacts from './Contacts'
import Profile from './Profile'
import './index.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'

function App() { 

  return (
    <>
    <Router>
      <div className="app">
        <Navbar/>
        <Routes>
          <Route path='/' element={<Home />}/>
          <Route path='/contacts' element={<Contacts />}/>
          <Route path='/profile' element={<Profile />}/>
        </Routes>
      </div>
    </Router>
    </>
  );
}

export default App