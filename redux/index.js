const createStore = function(reducer, initState){
    let state = initState;
    let listeners = [];

    function getState(){
        return state;
    }

    function dispatch(action){
        state = reducer(state, action);

        for(let i = 0; i<listeners.length; i++){
            const listener = listeners[i];
            listener();
        }
    }

    function subscribe(listener) {
        listeners.push(listener);
    }

    dispatch({type: Symbol()});
    
    return {
        subscribe, changeState: dispatch, getState
    }

}

let initCountState = {
    count: 0
}

function counterReducer(state, action) {
    if(!state) {
        state = initCountState;
    }
    switch(action.type) {
        case 'INCREMENT': return{
                ...state,
                count: state.count + 1
            }   

        case 'DECREMENT': return {
                ...state,
                count: state.count - 1
            }
        default: return state;
    }
}

let initInfoState = {
    name: 'Summer Fang',
    title: 'Director'
}
function InfoReducer(state, action){
    if(!state){
        state = initInfoState;
    }
    switch(action.type) {
        case 'SET_NAME': return {
            ...state,
            name: action.name
        }
        case 'SET_TITLE': return {
            ...state,
            title: action.title
        }
        default: return state;
    }
}

function combineReducers(reducers) {
    const reducerKeys = Object.keys(reducers);
    
    return function combination(state = {}, action){
        const nextState = {}
        
        for(let i=0; i<reducerKeys.length; i++){
            const key = reducerKeys[i];
            const reducer = reducers[key];
            const previousStateForKey = state[key];
            const nextStateForKey = reducer(previousStateForKey, action)

            nextState[key] = nextStateForKey
        }

        return nextState;
    }
}

const reducer = combineReducers({
    counter: counterReducer,
    info: InfoReducer
});

let store = createStore(reducer);

store.subscribe(()=>{
    let state = store.getState();
    console.log(state.counter.count, state.info.name, state.info.title);
});

store.changeState({
    type: 'INCREMENT'
});

store.changeState({
     type: 'SET_NAME',
     name: 'Wendy Wang'
})