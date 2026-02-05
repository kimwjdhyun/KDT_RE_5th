import { useState } from "react";

function ColorText() {
    const [inputColor, setInputColor] = useState('black');

    return (
        <div style={{ color: inputColor}}>
            <h2><strong>{inputColor === 'red' ? '빨간색' : inputColor === 'blue' ? '파란색' : '검정색'} 글씨</strong></h2>
            <button onClick={() => setInputColor('red')}>빨간색</button>
            <button onClick={() => setInputColor('blue')}>파란색</button>
            <button onClick={() => setInputColor('black')}>검정색</button>
        </div>
    );
}

export default ColorText;