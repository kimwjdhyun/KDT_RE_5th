import { useSearchParams, useNavigate } from "react-router-dom";

function Practice2() {
    const [searchParams] = useSearchParams();
    const name = searchParams.get("name");
    const realName = {kdt3rd: "김정현"};
    const navigate = useNavigate();

    return (
        <div>
        <h3>학생 이름: {name}</h3>
        <p>실제 이름은 {realName[name]} 입니다.</p>
        <button onClick={() => navigate(-1)}>이전 페이지</button>
        </div>
    );
}

export default Practice2;