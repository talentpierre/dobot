$(document).ready(function(){
	
	$('.upButton').on('click', function() {
		
		req = $.ajax({
			url : '/doup',
			type : 'POST'
		});
		
		req.done(function(data) {
			
			$('#span_id_1').fadeOut(1000).fadeIn(1000);
			$('#span_id_1').text(data.member_number);
			
		});
			
	});
	
	$('.downButton').on('click', function() {
		
		req = $.ajax({
			url : '/dodown',
			type : 'POST'
		});
		
		req.done(function(data) {
			
			$('#span_id_1').fadeOut(1000).fadeIn(1000);
			$('#span_id_1').text(data.member_number);
			
		});
			
	});
	
	$('.leftButton').on('click', function() {
		
		req = $.ajax({
			url : '/doleft',
			type : 'POST'
		});
		
		req.done(function(data) {
			
			$('#span_id_1').fadeOut(1000).fadeIn(1000);
			$('#span_id_1').text(data.member_number);
			
		});
			
	});
	
	$('.rightButton').on('click', function() {
		
		req = $.ajax({
			url : '/doright',
			type : 'POST'
		});
		
		req.done(function(data) {
			
			$('#span_id_1').fadeOut(1000).fadeIn(1000);
			$('#span_id_1').text(data.member_number);
			
		});
			
	});
	
	$('.forwardButton').on('click', function() {
		
		req = $.ajax({
			url : '/doforward',
			type : 'POST'
		});
		
		req.done(function(data) {
			
			$('#span_id_1').fadeOut(1000).fadeIn(1000);
			$('#span_id_1').text(data.member_number);
			
		});
			
	});
	
	$('.backwardButton').on('click', function() {
		
		req = $.ajax({
			url : '/dobackward',
			type : 'POST'
		});
		
		req.done(function(data) {
			
			$('#span_id_1').fadeOut(1000).fadeIn(1000);
			$('#span_id_1').text(data.member_number);
			
		});
			
	});
	
});