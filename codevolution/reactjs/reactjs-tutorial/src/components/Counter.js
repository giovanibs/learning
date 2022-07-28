import React, {Component} from 'react'

class Counter extends Component {
    constructor(props) {
        super(props)

        this.state = {
            count: 0
        }
    }

    increment() {
        
       /*  this.setState({
            count: this.state.count + 1
            },
            () => {
            console.log('Callback function value', this.state.count)
            }
        ) */

        /* TO UPDATE THE STATE BASED ON THE PREVIOUS STATE
        WE MUST PASS A FUNCTION INSTEAD OF AN OBJECT */

        this.setState( (prevState, props) => ({
            count: prevState + 1
        })
        )
    }

    render() {
        return (
            <div>
                <div>Count: {this.state.count}</div>
                <button onClick={() => this.increment()}>Increment</button>
            </div>
        )
    }

}

export default Counter