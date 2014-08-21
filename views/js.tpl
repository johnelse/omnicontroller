function sendCommand(command) {
    $.get(
        "/command",
        {name: "{{name}}", command: command},
        "json");
};

$(document).ready(function() {
%for control in controls:
    $("#{{control[1]}}").click(function() {sendCommand("{{control[2]}}")});
%end
});
