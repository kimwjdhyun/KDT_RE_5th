// const Practice = (props) => {
//     const {food = "기본값"} = props
//     return (
//         <div>
//             <span style={{color: 'red'}}>{food}</span>은 맛있습니다.
//         </div>
//     )
// }



const Practice1 = (props) => {
    const {title = "나의 하루는 4시 40분에 시작된다",
        author = "김우중",
        price = "13,500원",
        type = "자기계발서"}
        = props
    
    return (
        <div className="book">
            <h1>이번주 베스트셀러</h1>
            <div className="info">
                <div className="image">
                    <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyNTA1MDlfMTI2%2FMDAxNzQ2Nzc0MjUxNjgx.3QkNIVMFZh-wchONwCA6IGQlmWmqrDa9rW6w3bb53HAg.IYYApGBcs0cwrDWKeVNPivUcVwDpGsAoqa3DPfVWit4g.JPEG%2F900%25A3%25DF20250509%25A3%25DF091657.jpg&type=a340"/>
                </div>
                <div>
                    <h3>{title}</h3>
                    <p>저자: {author}</p>
                    <p>가격: {price}</p>
                    <p>구분: {type}</p>
                </div>
            </div>
        </div>
    )
}

export default Practice1