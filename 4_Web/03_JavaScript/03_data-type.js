// 원시 자료형

// 1. 문자열 (string)
const str = '좋은 아침!';
console.log(str);

// 문자열 연산
const str2 = '오늘도 화이팅!😊';
console.log(str + str2);

const name = '_kimwjdhyun';
const age = 29;
console.log("안녕하세요 저는 "+ name + "이고, 나이는 " + age + "살 입니다.");
//안녕하세요 저는 _kinwjdhyun 이고 나이는 29살 입니다.

//템플릿 리터럴
//변수와 문자열을 함께 쓸 수 있도록 하는 문법
console.log(`안녕하세요~ 저는 ${name}이고, 나이는 ${age}살 입니다.`);

console.log(`변수 말고 코드 실행도 가능해요 ${4+6}`);

// =====================================================

// 2. 숫자형 (number)

// 정수와 실수를 구분하지 않고 전부 number type
const num = 100;
const num2 = 3.14;

console.log("숫자형", num, num2);

// =====================================================

// 3. 불리언 / 논리형 (boolean)

//참 or 거짓을 표현하는 true, false
const istrue = true;
const isfalse = false;
console.log("불리언", istrue, isfalse);

// =====================================================

// 4. null (빈 값)

// 의도적으로 값을 비운 상태
//"값이 없음"을 명시

let isvar = null;
console.log(isvar);
isvar = '이렇게 이후 값이 할당될 수 있어요';
console.log(isvar);

// =====================================================

// 5. undefined
// 값이 정의(할당)되지 않은 상태
let x;
console.log(x); // undefined 출력
// console.log(x2); 할당되지 않은 변수로 에러 발생

// =====================================================

// [객체 자료형]

// 1. 배열 (array)
let fruits = ["청포도", "오렌지", "체리", "납작복숭아", "감귤"];
console.log("배열", fruits);

// 인덱싱
console.log(fruits[3]);
console.log(fruits[-1]); // undefined

// at 활용 시 음수 인덱싱 가능
console.log(fruits.at(2)); // 체리
console.log(fruits.at(-1)); // 망고스틴

fruits[3] = "말랑복숭아";
console.log(fruits);

// 배열 안에 요소로 배열 넣을 수 있음
const korean = [
    ["가", "나", "다"],
    ["라", "마", "바"],
    ["사", "아", "자"]
]

// 변수 자체에 대한 수정은 불가능
// 하지만 배열 내부의 요소는 수정 가능

console.log(korean[0][1]); // 나 출력 인덱스 출력 방법 숙지하기!
korean[2][2] = "하";
console.log(korean[2][2]); // javascript 가 느슨한 언어인 이유

// =====================================================

// 2. 객체 (object)

// 키 - 값 쌍을 값으로 가짐
let cat = {
    name : "장화",
    age : 18,
    iscute : true,
    mew : function() {
        return "야옹"
    },
};

console.log("객체", cat);

// 객체의 값 조회
// 1) 점 표기법
// 키가 문자열인 경우만 가능
console.log(cat.name);
console.log(cat.age);
// console.log(cat.12); // 키가 숫자인 경우 접근 못함

// 2) 대괄호 표기법
// console,log(cat["name"]);
// console.log(cat["age"]);
// console.log(cat[12]); //키가 숫자여도 접근 가능

// cat.mew(); // => 냅다 '야옹' 쓴거랑 다를바가 없다. console.log로 찍어야 콘솔창에서 확인 가능

let catMew = cat.mew();
console.log(catMew);

let cat2 = {
    name : "장화",
    age : 18,
    iscute : true,
    mew : function() {
        // alert("야옹")
    },
};

cat2.mew(); // cat2라는 객체의 mew 키 값을 실행시키는 코드

let cat3 = {
    name : "장화",
    age : 18,
    iscute : true,
    mew : function(str) {
        return str;
    },
};

cat3.mew('야옹야옹'); // 매개변수로 전달한 '야옹야옹 리턴
// alert(cat.mew());
// alert(cat.mew('멍멍'));

// =====================================================

// 자료형 확인 (typeof)
console.log(typeof '문자'); //string
console.log(typeof 100); // number
console.log(typeof 3.14); // number
console.log(typeof true); // boolean
console.log(typeof null);  // object
console.log(typeof undefined); //undefined

// object -> 배열은 object 하위의 array 이고 메서드들이 자동으로 
// 포함되어 typeof로 자료형 확인 시 object로 출력됨
console.log(typeof fruits); // object
console.log(typeof cat) // object

