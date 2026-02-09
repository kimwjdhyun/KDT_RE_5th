import { useParams, useNavigate } from "react-router-dom";

function Practice() {
    const { name } = useParams();
    const navigate = useNavigate();

    return (
        <div>
        <h3>학생 이름: {name}</h3>
        <p>학생 이름은 {name} 입니다.</p>
        <button onClick={() => navigate(-1)}>이전 페이지</button>
        </div>
    );
}

export default Practice;