import React, {Component} from 'react'

class EventBind extends Component {
    constructor(props) {
        super(props)

        this.state = {
            message: 'Hello'
        }

        /* 3rd approach:  bind 'this'in the constructor */
        this.clickHandler = this.clickHandler.bind(this)
    }

    /* 1st to 3rd approach to event binding uses a class method */
    /* clickHandler() {
        this.setState({
            message: 'Goodbye'
        })
    } */

    /* 4th approach: use an arrow function to turn the clickHandler */
    clickHandler = () => {
        this.setState({
            message: 'Goodbye'
        })
    }

    render() {
        return (
            <div>
                <div>{this.state.message}</div>
                
                {/* 1st approach to bind 'this' to the event handler */}
                {/* <button onClick={this.clickHandler.bind(this)}>Click</button> */}

                {/* 2nd approach to bind 'this' to the event handler */}
                {/* <button onClick={() => this.clickHandler()}>Click</button> */}

                {/* 3rd approach:  bind 'this' in the constructor */}
                {/* 4th approach: use an arrow function to turn the clickHandler into a class property */}
                <button onClick={this.clickHandler}>Click</button>
            
            </div>
        )
    }
}

export default EventBind