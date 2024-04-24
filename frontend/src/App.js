import React, { useState, useEffect } from "react";

function App() {
	const [data, setData] = useState([]);

	useEffect(() => {
		fetch("/api/prices")
			.then((response) => response.json())
			.then((data) => setData(data));
	}, []);

	return <div>{data}</div>;
}

export default App;
