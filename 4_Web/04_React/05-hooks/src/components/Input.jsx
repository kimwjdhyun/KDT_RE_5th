function Input({ setData }) {
    return (
        <div>
            <span style={{ fontWeight: "bold" }}>내용 :</span>
            <input 
                type="text" 
                placeholder="내용을 입력하세요."
                style={{ fontWeight: "bold" }}
                onChange={(e) => {
                    setData(prev => ({ ...prev, content: e.target.value}));
                }}
            />
        </div>
    );
}

export default Input;