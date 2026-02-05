import { useState } from "react";

function Practice1() {

    const [inputName, setInputName] = useState("");
    const [inputEmail, setInputEmail] = useState("");
    const [users, setUsers] = useState([]);
    
    const addUser = () => {
        const newUser = users.concat({
            id : users.length + 1,
            name : inputName,
            email : inputEmail
        });
        setUsers(newUser);
        setInputName("");
        setInputEmail("");
    };

    const deleteUser = (targetId) => {
        const newUsers = users.filter((user) => user.id !== targetId);
        setUsers(newUsers)
    }
    return ( 
        <>
        <input 
            type="text" 
            placeholder="이름"
            value={inputName}
            onChange={(e) => {
                setInputName(e.target.value)
            }}
        />
        <input 
            type="text" 
            placeholder="이메일"
            value={inputEmail}
            onChange={(e) => {
                setInputEmail(e.target.value)
            }}
        />
        <button onClick={addUser}>등록</button>
        <ol>
            {users.map((user) => {
                return <li key={user.id} onDoubleClick={() => deleteUser(user.id)}> <strong>{user.name}</strong> : <strong>{user.email}</strong></li>
            })}
        </ol>
        </>
    );
};

export default Practice1;