async function fetch_map_data () {
	try {
	  const map_data = await fetch('/data/API_data_output.json')
	  console.log(`Here are data : ${map_data}`)
	  return map_data;
	} catch (error) {
	  console.log(`${error} - Couldn't fetch data`)
	}
  }

 export default fetch_map_data;