function Register() {
  return <div>Login</div>;
}

function App() {
  let [UI, setUI] = useState('Login');
  let onClickLogin = () => {
    setUI('Login')
  }
  let onClickRegister = () => {
    setUI('Register') 
  }
  let showUI = () => {
    switch(UI) {
      case 'Login':
        return <Login/>
      case 'Register':
        return <Register/>
    }
  }
  return (
    <div className="App">
      <button onClick={onClickLogin}>Login</button>
      <button onClick={onClickRegister}>Register</button>
      <div>
          {showUI()}
      </div>
    </div>
  );
}
