import React from 'react'
import Navbar from '../components/Navbar'

function Login() {
  return (
    <div>
      <Navbar/>
      <div className='centered-column-container'>
        <h3>Login</h3>
        <form method='post'>
          <input className='input-group-text mb-2' type={'text'} name='email' placeholder='Email'/>
          <input className='input-group-text mb-2' type={'text'} name='password' placeholder='Password'/>
          <div className='d-flex justify-content-center'>
            <button className='btn btn-primary' type='submit'>Login</button>
          </div>
        </form>
      </div>
    </div>
  )
}

export default Login