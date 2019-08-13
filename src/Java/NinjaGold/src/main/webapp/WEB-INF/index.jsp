<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
     <%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<!-- Font Awesome -->
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.8.2/css/all.css">
<!-- Bootstrap core CSS -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
<!-- Material Design Bootstrap -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.7/css/mdb.min.css" rel="stylesheet">

<style>
.score{
padding:5px;
margin-left:5px;
padding-right:50px;
border: 1px solid black;
}
.card{
margin:30px;
display:inline-block;
} 
img{
width:200px;
height:200px;
}
h1{
color:white;
}
.wrapper{
height:660px;
padding:30px;
}
.activities{
padding: 10px;
background-color:white;
}
.red,.green{
margin:5px; 
padding:5px;
color:white;
}

</style>
<meta charset="ISO-8859-1">
<title>Ninja Gold!</title>
</head>
<body class="blue-gradient">
<div class="wrapper col-12">
<h1 class='animated shake'>Your Gold:<span class="score"><c:out value="${gold}"/></span></h1>
<div class="card text-white bg-warning mb-3 animated zoomInLeft" style="max-width: 15rem;">
  <div class="card-body">
    <h5 class="card-title">Farm</h5>
 <img src="<c:url value="\resources\imgs\farm.png"/>"/>
    <p class="card-text text-white">Earns 10-20 Gold!</p>
    <form action="process_money" method="post">
 					<input type="hidden" name="building" value="farm">
					<button type="submit" class="btn btn-rounded btn-primary"><i class="fas fa-rocket pr-2" aria-hidden="true"></i>Find Gold!</button>	
		</form>
 </div>
 </div>
 
<div class="card text-white bg-dark animated zoomInLeft" style="max-width: 15rem;">
 <div class="card-body">
   <h5 class="card-title">Cave</h5>
    <img src="<c:url value="\resources\imgs\cave.png"/>"/>
   <p class="card-text text-white">Earns 5-10 Gold!</p>
      <form action="process_money" method="post">
 					<input type="hidden" name="building" value="cave">
					<button type="submit" class="btn btn-rounded btn-primary"><i class="fas fa-rocket pr-2" aria-hidden="true"></i>Find Gold!</button>	
		</form>
</div> 
</div>

<div class="card text-white bg-secondary mb-3 animated zoomInRight" style="max-width: 15rem;">
  <div class="card-body">
    <h5 class="card-title">House</h5>
         <img src="<c:url value="\resources\imgs\house.png"/>"/>
    <p class="card-text text-white">Earns 2-5 Gold!</p>
       <form action="process_money" method="post">
 					<input type="hidden" name="building" value="house">
					<button type="submit" class="btn btn-rounded btn-primary"><i class="fas fa-rocket pr-2" aria-hidden="true"></i>Find Gold!</button>	
		</form>
  </div>
</div>

<div class="card text-white bg-danger mb-3 animated zoomInRight" style="max-width: 15rem;">
  <div class="card-body">
    <h5 class="card-title">Casino</h5>
     <img src="<c:url value="\resources\imgs\casino.png"/>"/>
    <p class="card-text text-white">Win/Lose 0-50 Gold!</p>
       <form action="process_money" method="post">
 					<input type="hidden" name="building" value="casino">
					<button type="submit" class="btn btn-rounded btn-primary"><i class="fas fa-rocket pr-2" aria-hidden="true"></i>Find Gold!</button>	
		</form>
  </div>
</div>  

	<div class="activities" style='overflow:auto; height:150px;'>
			<h4>Activities:</h4>
			<c:forEach var="i" begin="0" end="${size}">
				<p class="<c:out value="${updates.get(i).get(0)}"/>"  >  <c:out value="${updates.get(i).get(1)}"/> <c:out value="${updates.get(i).get(2)}"/></p>
			</c:forEach>
			</div>
</div>

<!-- JQuery -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<!-- Bootstrap tooltips -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.4/umd/popper.min.js"></script>
<!-- Bootstrap core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
<!-- MDB core JavaScript -->
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mdbootstrap/4.8.7/js/mdb.min.js"></script>
<script>
$('button').on('click', function() {
    $(this).toggleClass('rubberBand animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
        $(this).toggleClass('rubberBand animated');
    });
})
</script>
</body>
</html>