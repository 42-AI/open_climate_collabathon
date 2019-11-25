require("./main.scss");
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux'
import { createStore } from 'redux'
import rootReducer from './reducers'
import App from './containers/App';
import statesData from './data/states-data';
// import fetch_map_data from './api/fetch_map_data'

// async function fetch_map_data () {
// 	try {
// 	  const map_data = await fetch('/data/API_data_output.json')
// 	  console.log(`Here are data : ${map_data}`)
// 	  return map_data;
// 	} catch (error) {
// 	  console.log(`${error} - Couldn't fetch data`)
// 	}
//   }
// fetch_map_data()

fetch('https://my-json-server.typicode.com/ArthurLan/fake_api/us_data')
.then(resp => {
	console.log("hello !")
	resp.json()
	.then(hello => {
		console.log(`Here are data : ${JSON.stringify(hello)}`)
	})
})
.catch(error => {
		  console.log(`${error} - Couldn't fetch data`)
 	// }
});

const initialState = {
	regionData: statesData,
	emptyRegions: [],
	sortState: { key: 'regionName', direction: 'ASC' }
};

const store = createStore(rootReducer, initialState);

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('app')
);
