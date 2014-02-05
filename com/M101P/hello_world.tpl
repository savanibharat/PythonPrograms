<html>
<head
<title>
</title>
</head>
<body>

<p>
Welcome {{username}}

<ul>

%for thing in things:
<li>{{thing}}</li>
%end
</ul>
</body>
</html>