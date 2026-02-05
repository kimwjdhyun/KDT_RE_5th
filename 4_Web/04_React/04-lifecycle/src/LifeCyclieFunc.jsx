import { useState } from "react";
import LifeCyclieChild from "./LifeCycleChild";

function LifeCycleFunc() {
    const [number, setNumber] = useState(0);
    const [visible, setVisible] = useState(true);


    const changeNumber = () => {
        setNumber(number + 1);
    };
    const changeVisible = () => {
        setVisible(!visible);
    }
    return (
        <div>
            <button onClick={changeNumber}>plus</button>
            <button onClick={changeVisible}>On / Off</button>

            {visible && <LifeCyclieChild number={number} />}
        </div>
    );
}

export default LifeCycleFunc;