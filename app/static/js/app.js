'use strict';
var app = angular.module('a_atendance', ['ngRoute']);

app.config(
	function($routeProvider) {
		$routeProvider.
	    when("/index", {
	        templateUrl: "/static/templates/index.html"
	    }).
	    when("/login", {
	        templateUrl: "/static/templates/login.html"
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

app.config(['$qProvider', function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
}]);

app.controller('loginPageController', [
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
				console.log("FUCK YOU");
				$window.location.href = '/index.html';
			},
			function(response) {
    			console.log("No success");
  	})};
}]);