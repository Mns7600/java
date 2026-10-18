import React, { useState } from "react";

const COLORS = ["Red", "Blue", "Green", "Yellow"];

function App() {
    const [selectedColor, setSelectedColor] = useState("");

    return (
        <div
            style={{
                textAlign: "center",
                marginTop: "50px",
                fontFamily: "sans-serif"
            }}
        >
            <h1>Color Selection</h1>

            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    gap: "10px",
                    margin: "20px 0"
                }}
            >
                {COLORS.map((color) => (
                    <button
                        key={color}
                        onClick={() => setSelectedColor(color)}
                        style={{
                            padding: "8px 16px",
                            cursor: "pointer",
                            borderRadius: "6px",
                            border: "1px solid #ccc",
                            backgroundColor:
                                selectedColor === color
                                    ? color.toLowerCase()
                                    : "#f0f0f0",
                            color:
                                selectedColor === color &&
                                ["Red", "Blue", "Green"].includes(color)
                                    ? "#fff"
                                    : "#000",
                            fontWeight:
                                selectedColor === color ? "bold" : "normal"
                        }}
                    >
                        {color}
                    </button>
                ))}
            </div>

            {selectedColor && (
                <h2>
                    You have selected{" "}
                    <span style={{ color: selectedColor.toLowerCase() }}>
                        {selectedColor}
                    </span>{" "}
                    color.
                </h2>
            )}
        </div>
    );
}

export default App;