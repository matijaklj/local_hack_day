'use strict';
var app = angular.module('a_atendance', ['ngRoute']);

app.config(
	function($routeProvider) {
		$routeProvider.
	    when("/login", {
	        templateUrl: "/static/templates/login.html"
	    }).
	    when("/index", {
	        templateUrl: "/static/templates/index.html"
	    }).
	    otherwise({
	    	redirectTo : "/login"
	    });
	}
);

app.config( 
	function($interpolateProvider) {
		$interpolateProvider.startSymbol('{$').endSymbol('$}');
	}
);

app.controller('loginPageController', [
	'$scope', '$http', '$rootScope', function($scope, $http, $rootScope) {

	$scope.base_url =
	  		'http://' + document.domain + ':' + location.port
	var url = $scope.base_url + '/login'

	$scope.login = 
		$http.post(url, { 'data': user })
			.success(function(response) {
				console.log("SUCCESS");
			})
			.error(function(response) {
    			console.log(response.success);
  		});	
}]);
