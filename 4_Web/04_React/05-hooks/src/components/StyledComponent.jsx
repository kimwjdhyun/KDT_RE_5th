import styled from 'styled-components'

/**
 * CSS in JS
 * 각 컴포넌트마다 격리된 스타일 적용 가능
 */

const styledContainer = styled.div`
    display: flex;
`

const StyledBox = styled.div`
    width: 100px;
    height: 100px;
    background-color: aliceblue;
`

function StyledComponent() {
    return (
        <styledContainer>
            <StyledBox />
        </styledContainer>
    );
}

export default StyledComponent;