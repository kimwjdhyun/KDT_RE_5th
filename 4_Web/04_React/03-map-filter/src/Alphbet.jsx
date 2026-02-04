import { useState } from "react";

function Alphabet() {
    const list = ["a", "b", "c", "d", "e"];
    // input 값을 state 변수로 선언
    const [inputValue, setInputValue] = useState("");
    const [alphbet, setAlphbet] = useState(['b', 'a', 'n', 'a', 'n', 'a']);
    
    const addAlpha = () => {
        const newAlpha = alphbet.concat(inputValue);
        setAlphbet(newAlpha);
        setInputValue("");
    };
    return ( 
        <>
        {/* <ol>
            {list.map((value, idx) => {
                return <li key={idx}>{value}</li>
            })}
        </ol> */}
        {/* onChange 이벤트로 값으 변경 감지 -> state 변수값이 변경되게 끔 만들기 */}
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
            {alphbet.map((value, idx) => {
                return <li key={idx}>{value}</li>
            })}
        </ol>
        </>
    );
};

export default Alphabet;