// 구조 분해 할당
// 배열의 구조분해 할당
const arr1 = [10, 20, 30, 40, 50];
const [ten, twenty, thirty, fourty, fifty] = arr1;

console.log(ten);

// 기본값 지정
const arr2 = ["치킨", "피자"];
const [a, b, c = "콜라"] = arr2;
console.log(a, b, c);

// 객체 구조분해 할당 -> 키를 기준으로 할당
const obj = {
    name : "kim",
    age : "29",
    city : "jeju"
};

const {name, age, city, hobby = "산책"} = obj;
console.log("객체 구조 할당", name, age, city, hobby);

// 전개 연산자 ...(spread syntax)
// 배열전개
const arr3 = [1, 2, 3];
const arr4 = [4, 5, 6];
const spread = [...arr3, ...arr4];
console.log(spread);

// 문자열의 전개
const spread2 = [..."HELLO"]
console.log(spread2);

// 객체의 전개
const chip = {
    base : "포카칩",
    company : "오리온",
};

const potatochip = {
    ...chip,
    flavor : "어니언",
};

console.log(potatochip);

// rest 파라미터
const values = ['가', '나', '다', '라', '마'];

function myFunc(a, b, c, ...rest) {
    // 순서대로 받고 나머지는 resxt에 넣어줘
    console.log(a, b, c);
    console.log("rest", rest)
}
myFunc(...values);

const {flavor, ...rest} = potatochip;
console.log(flavor);
console.log(rest);

const word1 = "abc";
const word2 = "xyz";

const newword1 = [..."abc"];
const newword2 = [..."xyz"];
console.log(...newword1, ...newword2);
console.log(..."abc", ..."xyz");