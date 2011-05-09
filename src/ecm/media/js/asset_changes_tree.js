$(function () {


    $("#assets_tree").jstree({ 
        "plugins" : [ "themes" , "json_data" , "search" , "adv_search" , "ui",  "types" , "sort" ],
        "core" : { 
            "animation" : 150,
            "html_titles" : true
        },
        "ui" : {
            "select_limit" : 1
        },
        "themes" : {
            "url" : "/m/css/jstree.css",
            "dots" : false
        },
        "search" : {
            "case_insensitive" : true,
            "ajax" : {
                "url": function() {
                    var params = {
                        "stations" : SHOW_IN_STATIONS,
                        "space" : SHOW_IN_SPACE,
                        "since_weeks" : SINCE_WEEKS,
                        "to_weeks" : TO_WEEKS
                    };
                    if (SHOW_DIVISIONS != "None") {
                        params["divisions"] = SHOW_DIVISIONS;
                    }
                    return "/assets/changes/" + DATE + "/search?" + decodeURIComponent(jQuery.param(params));
                }
            }
        },
        "types" : {
            "max_depth" : -2,
            "max_children" : -2,
            "valid_children" : [ "system" ],
            "types" : {
                "system" : {
                    "class" : "system-row",
                    "icon" : { 
                        "image" : "/m/img/system.png" 
                    },
                    "valid_children" : [ "array", "station" ],
                    "max_depth" : 5,
                    "open_node"   : true,
                    "close_node"  : true
                },
                "array" : {
                    "class" : "hangar-row",
                    "icon" : { 
                        "image" : "/m/img/array.png" 
                    },
                    "valid_children" : [ "hangar" ],
                    "max_depth" : 4,
                    "open_node"   : true,
                    "close_node"  : true
                },
                "station" : {
                    "class" : "station-row",
                    "icon" : { 
                        "image" : "/m/img/station.png" 
                    },
                    "valid_children" : [ "hangar" ],
                    "max_depth" : 4,
                    "open_node"   : true,
                    "close_node"  : true
                },
                "hangar" : {
                    "class" : "hangar-row",
                    "icon" : { 
                        "image" : "/m/img/hangar.png" 
                    },
                    "valid_children" : [ "can", "mineral", "ship",  "ammo", "blueprint","item" ],
                    "max_depth" : 3,
                    "open_node"   : true,
                    "close_node"  : true
                },
                "added" : {
                    "icon" : { 
                        "image" : "/m/img/plus-tree-icon.png" 
                    },
                    "valid_children" : "none",
                    "max_depth" : 0,
                    "select_node" : true,
                    "open_node"   : true,
                    "close_node"  : true,
                    "create_node" : false,
                    "delete_node" : false
                },
                "removed" : {
                    "icon" : { 
                        "image" : "/m/img/minus-tree-icon.png" 
                    },
                    "valid_children" : "none",
                    "max_depth" : 0,
                    "select_node" : true,
                    "open_node"   : true,
                    "close_node"  : true,
                    "create_node" : false,
                    "delete_node" : false
                }
            }
        },
        "json_data" : {
            "ajax" : {
                "url" : function(node) { 
                    var url = "/assets/changes/" + DATE;
                    url += node.attr ? node.attr("id").replace(/_/g, "/") : "";
                    url += "/data"
                    var params = {
                        "stations" : SHOW_IN_STATIONS,
                        "space" : SHOW_IN_SPACE,
                        "since_weeks" : SINCE_WEEKS,
                        "to_weeks" : TO_WEEKS
                    };
                    if (SHOW_DIVISIONS != "None") {
                        params["divisions"] = SHOW_DIVISIONS;
                    }
                    return url + "?" +  decodeURIComponent(jQuery.param(params)); 
                }
            }
        },
        "sort" : function (a, b) {
            var key_a = +a.attributes['sort_key'].value;
            var key_b = +b.attributes['sort_key'].value;
            if (isNaN(key_a)) {
                key_a = a.attributes['sort_key'].value;
            }
            if (isNaN(key_b)) {
                key_b = b.attributes['sort_key'].value;
            }
            if (key_a > key_b) {
                return 1;
            } else {
                return -1;
            }
        }
    });
});

$("#search_form").submit(function(event) {
    event.preventDefault();
    $("#assets_tree").jstree("search", $("#search_text").val());
});

$("#clear_search").click(function() {
    $("#search_text").val("");
    $("#assets_tree").jstree("clear_search");
});

$("#expand_all").click(function() {
    $("#assets_tree").jstree("open_all");
});

$("#close_all").click(function() {
    $("#assets_tree").jstree("close_all");
});

$("#apply_filter").click(function() {
    var params = {
        "stations" : $("#show_stations").attr("checked"),
        "space" : $("#show_space").attr("checked"),
        "since_weeks" : SINCE_WEEKS,
        "to_weeks" : TO_WEEKS
    };
    var checkboxes = $(".hangar-checkbox");
    var divisions = "";
    for (var i=0 ; i < checkboxes.length ; i++) {
        if (checkboxes[i].checked) {
            divisions += "," + checkboxes[i].id;
        }
    }
    if (divisions.length != 0) {
        divisions = divisions.substring(1);
        params["divisions"] = divisions;
    }
    
    window.location = "/assets/changes/" + DATE + "?" + decodeURIComponent(jQuery.param(params)); 
});

$("#reset_filter").click(function() {
    window.location = "/assets/changes/" + DATE;
});

$("#date_selector").change(function () {
    var url = "/assets/changes/" + $("#date_selector option:selected").val();
    var params = {
        "stations" : $("#show_stations").attr("checked"),
        "space" : $("#show_space").attr("checked"),
        "since_weeks" : SINCE_WEEKS,
        "to_weeks" : TO_WEEKS
    };
    var checkboxes = $(".hangar-checkbox");
    var divisions = "";
    for (var i=0 ; i < checkboxes.length ; i++) {
        if (checkboxes[i].checked) {
            divisions += "," + checkboxes[i].id;
        }
    }
    if (divisions.length != 0) {
        divisions = divisions.substring(1);
        params["divisions"] = divisions;
    }
    window.location = url + "?" + decodeURIComponent(jQuery.param(params));
});

$(".hangar-checkbox").click(function (event) {
    if (event.ctrlKey) {
        /* if ctrl + click, deselect all divisions and select only this one */
        var checkboxes = $(".hangar-checkbox");
        for (var i=0 ; i < checkboxes.length ; i++) {
            checkboxes[i].checked = false;
        }
        this.checked = true;
    }
});

$(".space-checkbox").click(function (event) {
    if (event.ctrlKey) {
        /* if ctrl + click, deselect all divisions and select only this one */
        var checkboxes = $(".space-checkbox");
        for (var i=0 ; i < checkboxes.length ; i++) {
            checkboxes[i].checked = false;
        }
        this.checked = true;
    }
});