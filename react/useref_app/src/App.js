import { useState, useEffect, useRef } from "react";
import ReactDOM from "react-dom/client";

export default function App() {
  const [inputValue, setInputValue] = useState("");
  const count = useRef(0);
  const [renderCount, setRenderCount] = useState(0);

  useEffect(() => {
    // count.current = count.current + 1;
    // setRenderCount((prev) => prev + 1);
  });

  return (
    <>
      <input
        type="text"
        value={inputValue}
        onChange={(e) => {setInputValue(e.target.value);setRenderCount((prev) => prev + 1);}}
      />
      <h1>Render Count: {count.current}</h1>
      <h1>Render Count with state value: {renderCount}</h1>

    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);