const redux = require('redux');
const reduxLogger = require('redux-logger')

const combineReducers = redux.combineReducers
const applyMidlleware = redux.applyMiddleware
const logger = reduxLogger.createLogger()

const BUY_CAKE = 'BUY_CAKE'
const BUY_ICECREAM = 'BUY_ICECREAM'

/* ####### ACTION CREATOR ####### */
//action creator is a function that returns an action

function buyCake()  {

     //the action is the object with a type property
    return {   
        type: BUY_CAKE,
        info: 'First Redux action'
    }
}

function buyIceCream()  {

   return {   
       type: BUY_ICECREAM
   }
}

/* ##############################
    INITIAL STATE  
############################## */

// ### CASE 1: HAVING ONLY 1 REDUCER FOR SEVERAL STATES

/* const initialState = {
    numOfCakes: 10,
    numOfIceCreams: 20
} */
// END CASE 1 FOR INITIAL STATE

// ### CASE 2: HAVING SEVERAL REDUCERS

// in this case, we must have many initial states as necessary
const initialCakeState = {
    numOfCakes: 10,
}

const initialIceCreamState = {
    numOfIceCreams: 20
}
// END CASE 2 FOR INITIAL STATE


/* ##############################
    REDUCER FUNCTION
############################## */

//pure function that takes the state and action and returns the new state as an object
// (previousState, action) => newState

// ### CASE 1: HAVING ONLY 1 REDUCER FOR SEVERAL STATES

/* const reducer = (state = initialState, action)  => {
    switch (action.type) {
        case BUY_CAKE: return {
            ...state,
            numOfCakes: state.numOfCakes - 1
        }
        case BUY_ICECREAM: return {
            ...state,
            numOfIceCreams: state.numOfIceCreams - 1
        }
        
        default: return state
    }
} */

// END CASE 1 FOR 1 REDUCER

// ### CASE 2: HAVING MULTIPLE REDUCERS

const cakeReducer = (state = initialCakeState, action)  => {
    switch (action.type) {
        case BUY_CAKE: return {
            ...state,
            numOfCakes: state.numOfCakes - 1
        }
        
        default: return state
    }
}

const iceCreamReducer = (state = initialIceCreamState, action)  => {
    switch (action.type) {
        case BUY_ICECREAM: return {
            ...state,
            numOfIceCreams: state.numOfIceCreams - 1
        }
        
        default: return state
    }
}

// ### CASE 1: HAVING ONLY 1 REDUCER FOR SEVERAL STATES
/* const store = redux.createStore(reducer) */
//END CASE 1

// ### CASE 2: HAVING MULTIPLE REDUCERS

// combine the reducers into one 'rootReducer'
const rootReducer = combineReducers({
    cake: cakeReducer,
    iceCream: iceCreamReducer
})

const store = redux.createStore(rootReducer, applyMidlleware(logger))

//END CASE 2

console.log('Initial state ', store.getState())
const unsubscribe = store.subscribe( () => {})
store.dispatch(buyCake())
store.dispatch(buyCake())
store.dispatch(buyCake())
store.dispatch(buyIceCream())
store.dispatch(buyIceCream())
unsubscribe()