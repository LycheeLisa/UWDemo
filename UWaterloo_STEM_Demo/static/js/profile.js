function clusterview(val){
	$.post("/clusterview",
	{
		data: JSON.stringify(val),
	},
	function(response) {
					$("#profile").html(response);
				},
);
$([document.documentElement, document.body]).animate({
	scrollTop: $("#profile").offset().top
}, 1000);

};

// $(document).ready(function(){
// 			clusterGraph();
// 	 });

function clusterGraph(clusterVals){
	var ctx = document.getElementById('myChart').getContext('2d');
	var chart = new Chart(ctx, {
	    // The type of chart we want to create
	    type: 'pie',

	    // The data for our dataset
	    data: {
	        labels: ['Cluster 1', 'Cluster 2', 'Cluster 3', 'Cluster 4', 'Cluster 5', 'Cluster 6'],
	        datasets: [{
	            label: 'Demo Statistics',
	            // backgroundColor: 'rgb(255, 99, 132)',
	            // borderColor: 'rgb(255, 99, 132)',
							backgroundColor: [
                    "#F7464A",
                    "#46BFBD",
                    "#FDB45C",
                    "#949FB1",
                    "#4D5360",
										"#4D8360",
                ],
	            data: clusterVals
	        }]
	    },
			options: {
				legend: {
            display: true,
						position: "right",
        }
			}
			//
	    // // Configuration options go here
	    // options: {}
	});
};
