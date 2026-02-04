import PropTypes from 'prop-types';

// interface Props {
//     name?: String,
//     age : number
// }

export default function FunctionComponent({name = '기본이름', age}) {
    const student = "김정현";
    // console.log(props.name);
    // const {name} = props;
    console.log(age);
    return (
    <div>
        <h1>Hi {student}!</h1>
        {/* <div>넘겨받은 props {props.name}</div> */}
        <div>넘겨받은 props {name}</div>
        {age}
    </div>
    )
}

// 리액트 18 version에서 가능 -> TypeScript
FunctionComponent.propTypes = {
    age : PropTypes.number,
}