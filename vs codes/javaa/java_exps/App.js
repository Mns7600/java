import React, { useState } from "react";

function App() {
const [color, setColor] = useState("");

return (
<div style={{ textAlign: "center", marginTop: "50px" }}>
<h1>Color Selection</h1>

<button onClick={() => setColor("Red")}>Red</button>
<button onClick={() => setColor("Blue")}>Blue</button>
<button onClick={() => setColor("Green")}>Green</button>
<button onClick={() => setColor("Yellow")}>Yellow</button>

{color && <h2>You have selected {color} color.</h2>}
</div>
);
}

export default App;