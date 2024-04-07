import React, { useState } from 'react';

const FavoriteColor = () => {
  const [color, setColor] = useState('red');
  return (
    <>
      <h1>My favorite color is {color}!</h1>
      <button onClick={() => setColor('red')}>Red</button>
      <button onClick={() => setColor('blue')}>Blue</button>
      <button onClick={() => setColor('green')}>Green</button>
      <button onClick={() => setColor('yellow')}>Yellow</button>
    </>
  );
};

export default FavoriteColor() 