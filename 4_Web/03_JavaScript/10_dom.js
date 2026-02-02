// script 태그 위치가 head > title 아래였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head태그
console.log(document.body); // null
// html도 위에서부터 코드가 순차적으로 실행되기 때문에
// js를 불러온 뒤에 body 태그가 생성되어서 body가 null로 반환

// script 태그 위치가 html 닫히는 태그 위였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head태그
console.log(document.body); // html 내 body태그
// body가 생성된 이후 js 코드를 불러오면
// 문제 없이 body 태그를 불러올 수 있는 것

// 이런 불편함을 개선하고자
// script 태그에 type="module" 속성을 부여할 경우
// html이 모두 로드된 두 js 코드를 불러와 실행
// 현재 html에 적힌 script 태그 형태
// <script type="module" src="./11_dom_01.js"></script>
// 위치: head 태그 내부 title 아래

let user = {
  name: 'layla',
  age: 20,
  city: 'Seoul',
};

console.log('user 객체 원본:', user);

// for in
for (let key in user) {
  console.log('key:', key, ' | value:', user[key]);
}

// 객체
// 문자열, 숫자, 배열은 내장 메서드가 존재 (ex. concat, filter, sort, ...)
// 하지막 객체는 내장 메서드 X
//  객체는 키/값을 쌍으로 가지고 있다는 구조만 명확하고, 해당 값들의 타입이나 의미, 용도가 전부 제각각임
//  그래서 객체는 아예 Object라는 전역 내장 객체를 제공

// key 추출 (배열로 반환)
// JS에서 기본적으로 제공하는 Object 객체의 keys라는 메서드를 사용해서
// 매개변수로 전달한 user 객체의 key들을 배열로 반환
console.log('key 추출:', Object.keys(user));

// 값 추출
console.log('값 추출:', Object.values(user));

// [키, 값] 추출 (배열로 반환)
console.log('키, 값 추출:', Object.entries(user));

let entries = [
  ['name', 'layla'],
  ['age', 20],
  ['city', 'Seoul'],
];

// 배열을 객체로 변환
console.log('배열을 객체로 변환', Object.fromEntries(entries));

// script 태그 위치가 head > title 아래였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head태그
console.log(document.body); // null
// html도 위에서부터 코드가 순차적으로 실행되기 때문에
// js를 불러온 뒤에 body 태그가 생성되어서 body가 null로 반환

// script 태그 위치가 html 닫히는 태그 위였을 때
console.log(document); // html 문서
console.log(document.head); // html 내 head태그
console.log(document.body); // html 내 body태그
// body가 생성된 이후 js 코드를 불러오면
// 문제 없이 body 태그를 불러올 수 있는 것

// 이런 불편함을 개선하고자
// script 태그에 type="module" 속성을 부여할 경우
// html이 모두 로드된 두 js 코드를 불러와 실행
// 현재 html에 적힌 script 태그 형태
// <script type="module" src="./11_dom_01.js"></script>
// 위치: head 태그 내부 title 아래

// document 객체를 활용한 HTML 요소 선택
// 이전 방식 (legacy)
console.log(document.getElementById('green'));
console.log(document.getElementsByClassName('default'));
console.log(document.getElementsByTagName('div'));

console.log('---------------------');

// 선호되는 방식
// querySelector
// CSS 선택자로 HTML 요소를 가져옴
// 제일 처음 발견한 요소 하나만 반환
console.log(document.querySelector('#green'));
console.log(document.querySelector('.default'));
console.log(document.querySelector('input'));
console.log(document.querySelector('[name="id"]'));

console.log('---------------------');

// querySelectorAll
// CSS 선택자에 만족하는 모든 HTML 요소들을 NodeList라는 배열과 유사한 형태로 반환
// 불러온 요소들에 대한 순회가 가능  (forEach 활용)
console.log(document.querySelectorAll('.default'));
console.log(document.querySelectorAll('.others'));
console.log(document.querySelectorAll('div'));

// forEach 활용 NodeList 순회
const divEl = document.querySelectorAll('div');
console.log('querySelectorAll 활용 모든 div 요소 선택:', divEl);
divEl.forEach((el) => console.log('순회한 요소:', el));

// for of 활용 NodeList 순회
const classDefaultEl = document.querySelectorAll('.default');
for (let el of classDefaultEl) {
  console.log('for of 활용 .default 요소 순회:', el);
}