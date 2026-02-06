function Result({ data }) {
    const fruitImages = {
        watermelon: 'https://i.namu.wiki/i/lhDOWH4eIVI8FJVg7xms-hBlfwAUNpHcNRqbTGWfJ-yHPhh6qIEJrOKc43yEDvF2Pc5n6RADrKwFXUukM9NPvg.webp',
        banana: 'https://i.namu.wiki/i/Pk395EYC1jq_VGgkx9HM5Q9Oh9Pgd05yCMMgYMh7dnQKLPVuabR3-_5epQoo6fwiCB7nf7F1Ia6m89586Z7BRA.webp',
        orange: 'https://i.namu.wiki/i/v7_y8Hul3AIxpuJvATIr4t2RdVO3xwF1bXjHMtNmTlXOSkHPidgJQbZMivDN-6tZZznFSXdAVs303TLAMBueMw.webp'
    };

    return (
        <div style={{ textAlign: 'center' }}>
            <img 
                src={fruitImages[data.fruit]} 
                alt={data.fruit}
                style={{ width: '200px' }}
            />
            <div 
                style={{ 
                    backgroundColor: data.background,
                    color: data.color,
                    padding: '20px 20px',
                    marginTop: '10px',
                    marginBottom: '20px'
                }}
            >
                {data.content}
            </div>
        </div>
    );
}

export default Result;