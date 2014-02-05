<!DOCTYPE html>
<html>
<head>
<title>Hello world</title>
</head>
<body>
<p>
welcome {{username}}
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
<p>
<form action="/favorite_fruit" method="POST">
what is your favorite fruit?
<input type="text" name"fruit" size=40><br>
<input type="submit" value="Submit">
</form>
</body>
</html>