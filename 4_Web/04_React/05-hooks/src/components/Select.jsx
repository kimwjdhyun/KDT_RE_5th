function Select({ setData }) {
    const fruitChange = (e) => {
        setData(prev => ({ ...prev, fruit: e.target.value }));
    };

    const backgroundColor = (e) => {
        setData(prev => ({ ...prev, background: e.target.value }));
    };

    const colorChange = (e) => {
        setData(prev => ({ ...prev, color: e.target.value }));
    };

    return (
        <div>
            <label>과일 : </label>
            <select onChange={fruitChange} defaultValue="watermelon">
                <option value="watermelon">수박</option>
                <option value="banana">바나나</option>
                <option value="orange">오렌지</option>
            </select>

            <label>  배경색 : </label>
            <select onChange={backgroundColor} defaultValue="black">
                <option value="black">검정색</option>
                <option value="white">하얀색</option>
                <option value="yellow">노란색</option>
            </select>

            <label>  글자색 : </label>
            <select onChange={colorChange} defaultValue="white">
                <option value="white">하얀색</option>
                <option value="black">검정색</option>
                <option value="red">빨간색</option>
            </select>
        </div>
    );
}

export default Select;