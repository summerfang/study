import React, { useEffect, useState } from 'react';

const App = () => {
  const [items, setItems] = useState([{ id: 1, name: 'Item 1' }, { id: 2, name: 'Item 2' }]);
  const [refresh, setRefresh] = useState(false);

  const updateItem = (itemId, newName) => {
    // Create a new array with updated values
    const updatedItems = items.map(item => {
      if (item.id === itemId) {
        return { ...item, name: newName };
      }
      return item;
    });

    // Set the new array as the new state
    setItems(updatedItems);
  };

  const addItem = (newName) => {
    // Create a new array with updated values
    const updatedItems = [...items, { id: items.length + 1, name: newName }];

    // Set the new array as the new state
    setItems(updatedItems);
  };

  useEffect(() => {
    // setTimeout(() => {
      addItem(Math.random().toString(36).substring(7));
    // }, 1000);
  }, [items]);

  return (
    <div>
      {items.map(item => (
        <div key={item.id}>
          {item.name}
          <button onClick={() => updateItem(item.id, 'New Name')}>
            Update
          </button>
        </div>
      ))}
      <button onClick={()=>addItem("New Item")}>Add</button>
      <br/>
      <h1>Refresh:{refresh?"true":"false"}</h1>
      <button onClick={()=>setRefresh(!refresh)}>Refresh</button>
    </div>
  );
};

export default App;
