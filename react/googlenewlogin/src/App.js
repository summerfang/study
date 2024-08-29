import logo from './logo.svg';
import './App.css';
<script src="https://accounts.google.com/gsi/client" async></script>
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
      <div id="g_id_onload"
        data-client_id="386055258196-3b9ca0auhq72ct39o0q98jvebng51e3n.apps.googleusercontent.com"
        data-context="signin"
        data-ux_mode="popup"
        data-callback="googleLoginCallBack"
        data-auto_prompt="false">
      </div>

      <div class="g_id_signin"
        data-type="standard"
        data-shape="rectangular"
        data-theme="outline"
        data-text="signin_with"
        data-size="large"
        data-logo_alignment="left">
      </div>
    </div>
  );
}

export default App;
