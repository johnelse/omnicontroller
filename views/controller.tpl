<html>
    <head>
        <title>{{name}} interface</title>
        <script type="text/javascript" src="../js/static/jquery-1.6.4.min.js"></script>
        <script type="text/javascript" src="../js/gen/{{name}}.js"></script>
    </head>
    <body>
%for control in controls:
        <input type=button value="{{control[0]}}" id="{{control[1]}}">
%end
    </body>
</html>
