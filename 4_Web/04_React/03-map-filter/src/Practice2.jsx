import { useState } from "react";

function Practice2() {
    const [input, setInput] = useState({ user: "", title: "" });
    const [userTitle, setUserTitle] = useState([]);
    const [search, setSearch] = useState({ type: "작성자", word: "" });
    const [searchResults, setSearchResults] = useState([]);

    const addUser = () => {
        const newUser = userTitle.concat({
            id : userTitle.length + 1,
            name : input.user,
            title : input.title
        });
        setUserTitle(newUser);
        setInput({ user: "", title: "" });
    };

    const searchUser = () => {
        const key = search.type === "작성자" ? "name" : "title";
        const filtered = userTitle.filter((user) => user[key].includes(search.word));
        setSearchResults(filtered);
    };
    return (
        <>
        <input 
            type="text"
            placeholder="작성자"
            value={input.user}
            onChange={(e) => {
                setInput({ ...input, user: e.target.value })
            }}
        />
        <input 
            type="text"
            placeholder="제목"
            value={input.title}
            onChange={(e) => {
                setInput({ ...input, title: e.target.value })
            }}
        />
        <button onClick={addUser}>작성</button>
            <br />
        <select value={search.type} onChange={(e) => setSearch({ ...search, type: e.target.value })}>
            <option>작성자</option>
            <option>제목</option>
        </select>
        <input 
            type="text"
            placeholder="검색어"
            value={search.word}
            onChange={(e) => {
                setSearch({ ...search, word: e.target.value })
            }}
        />
        <button onClick={searchUser}>검색</button>

        <h3>전체 글 목록</h3>
        <ol>
            {userTitle.map((item) => (
                <li key={item.id}>{item.name} : {item.title}</li>
            ))}
        </ol>

        <h3>검색한 항목</h3>
        <ol>
            {searchResults.length > 0 
                ? searchResults.map((item) => <li key={item.id}>{item.name} : {item.title}</li>)
                : <li>검색 결과가 없습니다.</li>
            }
        </ol>      
    </>
    );
}

export default Practice2;