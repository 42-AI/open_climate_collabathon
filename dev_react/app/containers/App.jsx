import React from 'react';
import { connect } from 'react-redux'

import DataMap from '../components/DataMap';
import Navbar from '../components/Navbar';
import statesData from '../data/states-data.js'

class App extends React.Component {
  constructor(props){
	super(props);
	this.state = {
		map_data:[]
	};
  }
  componentDidMount() {
		console.log("Fetching map data from API");
		const api = 'http://127.0.0.1:8000/api/maps/USA?format=json';
		fetch(api)
		.then(response => 
			response.json()
		)
		.then(response => {
			response.forEach(element => {
				statesData.forEach(region => {
					if (region.regionName == element.regionName) {
						element.code = region.code
					}
				});
			});
			console.log(response)
			this.setState({ map_data:response})
		})
	}
  render() {
    return (
      <div>
        <Navbar />
        <div className="datamap-outer-conainer">
          <DataMap regionData={this.state.map_data} />
        </div>
      </div>
    );
  }
}

App.propTypes = {
  regionData: React.PropTypes.array.isRequired,
  emptyRegions: React.PropTypes.array.isRequired,
  sortState: React.PropTypes.object.isRequired
};

function sortCollection(collection, sortState) {
  switch (sortState.direction) {
    case 'ASC':
      return collection.sort(function(a, b) {
        if (a[sortState.key] > b[sortState.key]) return 1;
        if (a[sortState.key] < b[sortState.key]) return -1;
        return 0;
      });

    case 'DESC':
      return collection.sort(function(a, b) {
        if (a[sortState.key] > b[sortState.key]) return -1;
        if (a[sortState.key] < b[sortState.key]) return 1;
        return 0;
      });

    default:
      return collection;
  }
}

function alphabeticOrder(collection) {
  return collection.sort(function(a, b) {
    if (a.regionName > b.regionName) return 1;
    if (a.regionName < b.regionName) return -1;
    return 0;
  });
}

function mapStateToProps(state) {
  return {
    regionData: sortCollection(state.regionData, state.sortState),
    emptyRegions: alphabeticOrder(state.emptyRegions),
    sortState: state.sortState
  }
}

export default connect(mapStateToProps)(App);
