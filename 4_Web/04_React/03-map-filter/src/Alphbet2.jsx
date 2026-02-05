import { useState } from "react";

function Alphabet2() {
    // input 값을 state 변수로 선언
    /** 
     * {
     * id :1,
     * alpha:'a'
     * },
     * ...
    */
    const [inputValue, setInputValue] = useState("");
    const [alphbet, setAlphbet] = useState([]);
    
    const addAlpha = () => {
        const newAlpha = alphbet.concat({
            id : alphbet.length + 1,
            alpha : inputValue
        });
        setAlphbet(newAlpha);
        setInputValue("");
    };

    const deleteAlpha = (targetId) => {
        const newAlpha = alphbet.filter((alpha) => alpha.id !== targetId);
        setAlphbet(newAlpha)
    }
    return ( 
        <>
        <input 
            type="text" 
            placeholder="알파벳 입력"
            value={inputValue}
            onChange={(e) => {
                setInputValue(e.target.value)
                console.log(e.target.value)
            }}
        />
        <button onClick={addAlpha}>ADD</button>
        <ol>
            {alphbet.map((value) => {
                return <li key={value.id} onDoubleClick={() => deleteAlpha(value.id)}>{value.alpha}</li>
            })}
        </ol>
        {/* 단축평가 */}
        {alphbet.length === 0 && <span>알파벳을 입력해주세요!</span>}
        </>
    );
};

export default Alphabet2;