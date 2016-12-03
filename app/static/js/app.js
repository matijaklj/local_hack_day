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

		$scope.displayUcilnica = function() {
				console.log("laalal");
				//$location.path("/ucilnica");
		};

		$scope.ucilnice = [
		  {
		    "ime": "P01",
		    "opis": "velika predavalnica 1",
			"steviloPrisotnih": 86
		  },
		  {
		    "ime": "P3",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 6
		  },
		  {
		    "ime": "P4",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 12
		  },
		  {
		    "ime": "P5",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 15
		  },
		  {
		    "ime": "P6",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 17
		  },
		  {
		    "ime": "P3",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 20
		  },
		  {
		    "ime": "P4",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 22
		  },
		  {
		    "ime": "P5",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 12
		  },
		  {
		    "ime": "P3",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 12
		  },
		  {
		    "ime": "P4",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 12
		  },
		  {
		    "ime": "P5",
		    "opis": "mala predavalnica 3",
			"steviloPrisotnih": 12
		  }
		];

}]);

app.controller('indexPageController', [
	'$scope', '$http', '$location', '$rootScope',
	function($scope, $http, $location, $rootScope) {
		//$location.path("/ucilnice")

		$scope.linkTo = function() {
				$location.path("/ucilnica");
		};

		$scope.display = function() {
				console.log("laalal");
				//$location.path("/ucilnica");
		};

}]);
