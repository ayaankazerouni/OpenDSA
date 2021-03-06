/*global define */
(function() {
  "use strict";

  var jsav,                // The JSAV object
    answerArr = [],        // The (internal) array that stores the correct answer
    listArr = [],          //
    status = 0,            // Nothing is currently selected, status = 0;
                           // Data area of the node is selected, status = 1;
                           // pointer area is selected, status = 2.
    newNodeGen,            //
    newLinkNode,           // New node
    search_value,
    search_index,
    exe_head,              // head of the list
    connections = [],      //
    fromNode,              //
    toNode,                //
    jsavList,              // JSAV list
    listSize,              // JSAV list size
    selected_node;         // Position that has been selected by user for swap

  // JSAV extensions
/*  JSAV._types.ds.ListNode.prototype.exe_next = {};
  JSAV._types.ds.ListNode.prototype.exe_tail = {};
  JSAV._types.ds.ListNode.prototype.exe_edgeToNext = {};*/

  // Add an edge from obj1 to obj2
  function connection(obj1, obj2){
    if(obj1 == obj2){ return;}
    var fx = $('#' + obj1.id()).position().left + 37 + 2;
    var tx = $('#' + obj2.id()).position().left  +2;
    var fy = $('#' + obj1.id()).position().top + 15 + 1 + 54;
    var ty = $('#' + obj2.id()).position().top + 15 +1 + 54;
    var fx1 = fx, fy1 = fy, tx1 = tx, ty1 = ty;

    var disx = (fx - tx - 22) > 0 ? 1 : (fx - tx - 22) == 0 ? 0 : -1;
    var disy = (fy - ty) > 0 ? 1 : (fy - ty) == 0 ? 0 : -1;

    var dx = Math.max(Math.abs(fx - tx) / 2, 35);
    var dy = Math.max(Math.abs(fy - ty) / 2, 35);

    if(fy - ty > -25 && fy - ty < 25 && (tx - fx < 36 || tx - fx > 38)){
      dx = Math.min(Math.abs(fx - tx), 20);
        dy = Math.min(Math.abs(fx - tx)/3, 50);
        tx += 22;
        ty -= 15;
        fx1 = fx;
        fy1 = fy - dy;
        tx1 = tx - dx;
        ty1 = ty - dy;
    }else{
      if(disx == 1){
        tx += 22;
        ty += 15 * disy;
        fx1 = fx + dx;
        fy1 = fy - dy * disy;
        tx1 = tx;
        ty1 = ty + dy * disy;
      }else if(disx == -1){
        fx1 = fx + dx;
        fy1 = fy;
        tx1 = tx - dx;
        ty1 = ty;
      }
    }

    var edge = jsav.g.path(["M", fx, fy , "C", fx1, fy1, tx1 , ty1, tx, ty].join(","),{"arrow-end": "classic-wide-long", "opacity": 100,"stroke-width": 2} );
    if(obj1.exe_next){
      obj1.exe_edgeToNext.element.remove();
    }else{
      obj1.exe_tail.element.remove();
      obj1.exe_tail = null;
    }

    obj1.exe_edgeToNext = edge;
  }

  // Function for connecting to nodes when click them
  function Connect(obj1, obj2){
    if(obj1 == obj2){ return;}
    connection(obj1,obj2);
    obj1.exe_next = obj2;
    obj1._next = obj2;
    for(var i=0; i<connections.length; i++)
    {
      if(connections[i].from == obj1 && connections[i].to != obj2){
        connections[i].to = obj2;
        return;
      }
    }
      connections.push({from: obj1, to: obj2});
  }

  // Click event handler on the list
  function clickHandler(e) {
    var x = parseInt(e.pageX - $('#' + this.id()).offset().left);
    var y = parseInt(e.pageY - $('#' + this.id()).offset().top);
    if(x > 31 && x < 42 && y > 0 && y < 31){
      if(status == 1){
        selected_node.removeClass('bgColor');
        selected_node = null;
      }else if(status == 2){
        $('#' + fromNode.id() + " .jsavpointerarea:first").removeClass('bgColor');
      }

      if(status == 0 || status == 1){
        $('#' + this.id() + " .jsavpointerarea:first").addClass('bgColor');
        fromNode = this;
        status = 2;
      }else if(status == 2){
        if(this.id() == fromNode.id()){
          $('#' + this.id() + " .jsavpointerarea:first").removeClass('bgColor');
          fromNode = null;
          status = 0;
        }else{
          $('#' + this.id() + " .jsavpointerarea:first").addClass('bgColor');
          fromNode = this;
          status = 2;
        }
      }
    }else{
      if(status == 0){
        this.addClass('bgColor');
        selected_node = this;
        status = 1;
      }else if(status == 1){

        selected_node.removeClass('bgColor');
        selected_node = null;
        status = 0;
      }else if(status == 2){
        toNode = this;

        Connect(fromNode, toNode);
        $('#' + fromNode.id() + " .jsavpointerarea:first").removeClass('bgColor');
        $('#' + toNode.id()).removeClass('bgColor');
        fromNode = null;
        toNode = null;
        status = 0;
      }
      SelfOrgMove_to_FrontPro.userInput = true;
    }
  }


  // reset function definition
  function f_reset() {
    SelfOrgMove_to_FrontPro.userInput = false;
    newNodeGen = false;
    connections = [];
    selected_node = null;
    status = 0;
    if($("#jsav .jsavcanvas")){
      $("#jsav .jsavcanvas").remove();
    }
    if($("#jsav .jsavshutter")){
      $("#jsav .jsavshutter").remove();
    }
    jsav = new JSAV("jsav");
    jsav.recorded();

    if($("#jsav path")){
      $("#jsav path").remove();
    }
    if(jsavList){
      jsavList.clear();
    }

    jsavList = jsav.ds.list({"nodegap": 30, "top": 40, left: 0});
    jsavList.addFirst("null");
    for(var i = listSize - 2; i > 0; i--)
    {
      jsavList.addFirst(listArr[i]);
    }
    jsavList.addFirst("null");
    jsavList.layout();

    exe_head = jsavList.get(0);
    for(i = 0; i < listSize; i ++)
    {
      jsavList.get(i).exe_next = jsavList.get(i).next();
      jsavList.get(i).exe_edgeToNext = jsavList.get(i).edgeToNext();
    }


    jsavList.get(listSize - 1).exe_tail = jsav.g.line(34 + (listSize - 1)*74, 32 + 55,
                            44 + (listSize - 1)*74, 1 + 55,{"opacity": 100,"stroke-width": 1});

    //JSAV array for insert animation
    var jsavArr = jsav.ds.array([search_value], {indexed: false, center: false,left: 650, top: -70});

    jsavList.click(clickHandler); // Rebind click handler after reset
    SelfOrgMove_to_FrontPro.userInput = false;
  }

  var SelfOrgMove_to_FrontPro = {
    // Initialise the exercise

    userInput : false,             // Boolean: Tells us if user ever did anything

    initJSAV : function(size, pos) {
      answerArr.length = 0;
      listSize = size;

      // Give random numbers in range 0..999
      answerArr[0] = "null";
      for (i = 1; i < size-1; i++) {
        answerArr[i] = Math.floor(Math.random() * 1000);
      }
      answerArr[size-1] = "null";
      listArr = answerArr.slice(0);

      search_index = Math.floor((Math.random() * (size - 2)) + 1);
      search_value = listArr[search_index];

      f_reset();

      // correct answer
      if (search_index>1){
      answerArr.splice(search_index, 1);
      answerArr.splice(1, 0, search_value);
    }

        // Set up handler for reset button
      $("#reset").click(function () { f_reset(); });

    },

    // Check user's answer for correctness: User's array must match answer
    checkAnswer: function(arr_size) {
      var i = 0;
      var curr = exe_head;
      /*
      i = 0;
      var curr = exe_head;
      */
      while(curr.exe_next){
        if(curr.value() == answerArr[i]){
          curr = curr.exe_next;
          i++;
        }else{
          return false;
        }
      }

      return true;
    },

    getSearch: function (){
      return search_value;
    }
  }

  window.SelfOrgMove_to_FrontPro = window.SelfOrgMove_to_FrontPro || SelfOrgMove_to_FrontPro;
}());

