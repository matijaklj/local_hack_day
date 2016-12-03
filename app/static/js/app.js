'use strict';
var app = angular.module('a_atendance', ['ngRoute']);

app.config(
	function($routeProvider) {
		$routeProvider.
	    when("/index", {
	        templateUrl: "/static/templates/index.html"
	    }).
	    otherwise({
	    	redirectTo : "/index"
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


app.controller('indexPageController', [
	'$scope', '$http', '$location', '$rootScope', 
	function($scope, $http, $location, $rootScope) {

	$scope.base_url =
	  		'http://' + document.domain + ':' + location.port
	var url = $scope.base_url + '/index'

	$scope.login =  function(user) {
        console.log(user.username);
        $http.post(url, { 'data': user }).then(
			function(response) {
				console.log(response.data.message);
			},
			function(response) {
    			console.log("No success");
  	})};
}]);