'use strict';
var app = angular.module('a_atendance', ['ngRoute']);


app.config(
	function($routeProvider) {
		$routeProvider.
	    when("/index", {
			templateUrl: "/static/templates/ucilnice.html"
	    }).
		when("/ucilnica", {
	        templateUrl: "/static/templates/ucilnica.html"
	    }).
		otherwise({
	        templateUrl: "/static/templates/ucilnice.html"
    });
	}
);



app.config(
	function($interpolateProvider) {
		$interpolateProvider.startSymbol('{$').endSymbol('$}');
	}
);

app.config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);

app.controller('ucilnicePageController', [
	'$scope', '$http', '$location', '$rootScope',
	function($scope, $http, $location, $rootScope) {

		$scope.ucilnice = {};

		$scope.base_url = 'http://' + document.domain + ':' + location.port;

		var url = $scope.base_url + '/devices';

		$http.get(url)
	    .then(function(response) {
	        $scope.ucilnice = response.data.ucilnice;
	        console.log($scope.ucilnice);

	    }, function(response) {
			console.log("Error");
		});

		$scope.displayUcilnica = function(ime) {
				console.log(ime);

				$location.path("/ucilnica");
				$http.post(url, {'name': ime})
				    .then(function(response) {

						$location.path("/ucilnica");

				    }, function(response) {
						console.log("Error");
					});

		};

}]);

app.controller('ucilnicaPageController', [
	'$scope', '$http', '$location', '$rootScope',
	function($scope, $http, $location, $rootScope) {



}]);

app.controller('indexPageController', [
	'$scope', '$http', '$location', '$rootScope',
	function($scope, $http, $location, $rootScope) {
		//$location.path("/ucilnice")

		$scope.linkToUcilnice = function() {
				$location.path("/ucilnice");
		};


}]);
