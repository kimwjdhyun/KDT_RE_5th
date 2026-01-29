// 1. if문

console.log("========= if 문 =========")
let a = 10;
if (a > 5) {
    // if 문의 조건이 true일 때 실행할 코드
    console.log(`${a}이(가) 5보다 커요.`);
}

// 코드가 한 줄일 때는 scope({}) 생략이 가능
if (a > 3) console.log(`${a}이(가) 3보다 커요.`);

// if - else
if (a > 20) {
    console.log(`${a}이(가) 20보다 커요.`);
} else {
    // if 문의 모든 조건이 false인 경우에도 무조건 실행시킬 코드
    console.log(`${a}이(가) 20보다 작거나 같아요.`);
}

// if - else if - else
let score = 85;

if (score >= 90) {
    console.log('A');
} else if (score >= 80) {
    console.log('B');
} else if (score >= 70) {
    console.log('C');
} else if (score >= 60) {
    console.log('D');
} else {
    console.log('F');
}

// if 문을 따로 따로 작성하는 경우
if (score < 90 && score >= 80) {
    console.log('B');
}

// 마지막 else 문도 else if 문으로 작성 가능
//ex)
else if (sore < 60) {
    console.log('F');
}
// 이럴경우 개발자 입장에서도 번거롭고, 코드가 실행될 때 조건에 만족하는지 불필요한 검사를 진행함

// if 문 중첩
// console.log("========= if 문 중첩 =========");

// let user_ID = "kimwjdhyun"
// let user_PW = "4321!"

// let user_input_ID = prompt('아이디를 입력해주세요.');
// if (user_input_ID === user_ID) {
//     let user_input_PW = prompt("비밀번호를 입력해주세요.");
//     if (user_PW === user_input_PW) {
//         alert("로그인 성공!");
//     } else {
//         alert("비밀번호가 틀렸습니다.");
//     }
// } else {
//     alert("아이디가 틀렸습니다.");
// }

// 2. switch 문

// console.log("========= switch 문 =========");

// let b = Number(prompt("숫자를 입력해주세요."));

// switch (b) {
//     case 1:
//         console.log("b가 1이네요.");
//         break;
//     case 2:
//     case 3:
//     case 4:
//     // case만 연달아 작성한 경우 해당 케이스 중 하나라도 만족하면 : 다음 코드 실행
//         console.log("b가 2 ~ 4 중 하나네요.");
//     case 5:
//         console.log("b가 5네요.")
//     default:
//         //위의 모든 조건들이 불만족할 때 무조건 실행되는 코드
//         console.log("b가 뭔지 모르겠어요.")
//         break;
// }

// 3. 삼항 연산자

console.log("========= 삼항연산자 ==========");
//간단한 조건문을 간결하게 표현하는데 사용

let num = 100;

//일반 if문
if (num > 50) {
    console.log("num이 50보다 커요.")
} else {
    console.log("num이 50보다 작거나 같아요.")
}

//동일한 로직 삼항연산자로 변환
// 조건 ? 조건이 true일 때 실행될 코드 : 조건이 false일 때 실행될 코드
num > 50
 ? console.log("num이 50보다 커요.") // ? 다음은 참일 때 실행
  : console.log("num이 50보다 작거나 같아요."); // : 다음은 거짓일 때 실행

//실습 1. 연령대 별 나이 출력
// let age = prompt("나이를 입력하세요.");

// if (age < 10) {
//     alert("0~9세 입니다.");
// } else if (age < 20) {
//     alert("10대입니다.");
// } else if (age < 30) {
//     alert("20대입니다.");
// } else if (age < 40) {
//     alert("30대입니다.");
// } else if (age < 50) {
//     alert("40대입니다.");
// } else if (age < 60) {
//     alert("50대입니다.");
// } else if (age < 70) {
//     alert("60대입니다.");
// } else if (age < 80) {
//     alert("70대입니다.");
// } else if (age < 90) {
//     alert("80대입니다.");
// } else if (age < 100) {
//     alert("90대입니다.");
// } else {
//     alert("100세가 넘으셨네요 장수하세요!");
// }

// 실습 2. 지금은 오전? 오후?

let ampm = new Date().getHours();
console.log('현재시간', ampm);

ampm < 12 ? console.log("오전") : console.log("오후");