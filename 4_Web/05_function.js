// 1. 함수 선언

// 1-1. 함수 선언식 (기본적인 함수 선언 방법)
function myFunc(str) {
    // 중괄호 내부에 함수 호출 시 동작할 코드 작성
    return str;
}
console.log(myFunc("안녕하세요!"));

// 간단 실습
// 함수를 호출했을 때 호출많 해도 콘솔에 띄우기

function myFunc2(str) {
    console.log(str = "안녕하세요! 반갑습니다.");
}
myFunc2()

// 1-2. 함수 표현식
// 변수에 익명함수를 할당하는 방법
const myFunc3 = function() {
    console.log("함수표현식으로 함수 선언하기");
}
myFunc3();

// 1-3. 화살표 함수
// 콜백함수 (어떤 코드나 로직 안에 작성할 때 많이 사용)
const myFunc4 = () => {
    // 화살표 함수는 {}안에 꼭 return이 되어야 함.
    return "화살표 함수로 함수 선언하기";
}
console.log(myFunc4());

// 한줄로 작성 + 괄호 없는 경우에는 해당 내용을 자동으로 return
const myFunc5 = () => "return없이 사용하기";
console.log(myFunc5); // 호출 안하고 변수를 콘솔에 찍은 버전 => 변수 전체
console.log(myFunc5()); // () 사용해서 함수를 호출한 버전 => 함수가 실행된 결과

// 사걱형의 넓이를 구하는 함수
const square = (width, height) => width * height;
console.log("사각형의 넓이 구하기", square(10, 8)); // 80

function noReturnFunc(width, height) {
    width * height;
}
console.log(noReturnFunc(5, 7)); //undefined : return 하지 않으면 함수 스코프 내부 실행되고 끝

//함수 호이스팅(Hoisting)
/*
함수 선언식으로 함수를 만들었을 때는 선언보다 위에서 호출 가능
**함수 표현식, 화살표함수는 호출 불가!!!!!**
*/