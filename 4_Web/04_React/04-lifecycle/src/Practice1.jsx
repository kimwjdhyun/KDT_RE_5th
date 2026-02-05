import { useEffect, useState } from "react";
import Practice1Child from "./Practice1Child";
import { fakePosts } from "./Practice1Child";

function Practice1() {
    const [postList, setPostList] = useState([]);
    
    useEffect(() => {
        setTimeout(() => {
            setPostList(fakePosts);
        }, 2000);
    }, []);
    return (
        <div>
            <h1>Post List</h1>
            {postList.length === 0 ? (
                <p>loading.....</p>
            ) : (
                <Practice1Child posts = {postList} />
            )}
        </div>
    );
}

export default Practice1;

fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(response => response.json())
    .then(json => console.log(json))