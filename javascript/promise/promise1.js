const p = new Promise(()=>(setTimeout((x)=>(x+1), 3000)))

p.then(()=>(console.log(x)))