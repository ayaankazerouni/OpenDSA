
// sorting the elements of an array with Insertation Sort
var sortArray = function (anArray, tArray, dArray) {
	for (var i = 1; i < anArray.length; i++) {
		var key = anArray[i];
		var tmp = tArray[i];
		var tmpdis = dArray[i];
		var j = i - 1;
		while(j >= 0 && key < anArray[j]) {
			anArray[j + 1] = anArray[j];
			tArray[j + 1] = tArray[j];
			dArray[j + 1] = dArray[j];
			j--;
		}
		anArray[j + 1] = key;
		tArray[j + 1] = tmp;
		dArray[j + 1] = tmpdis;
	}	
}

// shuffle the array by moving left
var shuffle = function (anArray, tArray, dArray, key, node) {
	anArray[1] = key;
	tArray[1] = node;
	dArray[1] = key;
	for (var i = 0; i < anArray.length - 1; i++) {
		anArray[i] = anArray[i + 1];
		tArray[i] = tArray[i + 1];
		dArray[i] = dArray[i + 1];
	}
	anArray.length -= 1;
	tArray.length -= 1;
	dArray.length -= 1;
}

// Constructing the huffmanCodingTree
var huffTree = function (nArray, tArray, dArray) {
	while (nArray.length > 1) {
		sortArray(nArray, tArray, dArray);
		var key = nArray[0] + nArray[1];
		if (nArray.length == 2) {
			var node = bt.root(key);
		}
		else {
			var node = bt.newNode(key);
		}
		node.left(tArray[0]);
		node.right(tArray[1]);
		shuffle(nArray, tArray, dArray, key, node);
	}	
}

// Constructing the huffmanCodingTree with animation
var huffTree_animation = function (nArray, tArray, dArray) {
	while (nArray.length > 1) {
		sortArray(nArray, tArray, dArray);
		caption_label.text(caption_text + "Sorting the data by their frequency.");
	
		bt.hide();	
		arr.hide();
		tmpBT.hide();
		arr = jsav.ds.array(dArray);
		jsav.step();
		caption_label.text(caption_text + "Choose the two samllest number: " + nArray[0] + " and " + nArray[1]);

		arr.css([0, 1], {"color": "blue", "background-color": "yellow"});
		var key = nArray[0] + nArray[1];
		bt.hide();
		jsav.step();	
		
/*	caption_label.text(caption_text + "Merge them together, and the result is " + key);
			tmpBT.root(key);
			tmpBT.root().left(dArray[0]);
			tmpBT.root().right(dArray[1]);
			bt.hide();
			arr.hide();
			tmpBT.show();
			traverse_color(tmpBT.root(), "white");
			tmpBT.layout();
			jsav.step(); */

		if (nArray.length == 2) {
			var node = bt.root(key);
		}
		else {
			var node = bt.newNode(key);
		}
		node.left(tArray[0]);
		node.right(tArray[1]);

		caption_label.text(caption_text + "Merge them together, and the result is " + key);
		tmpBT.root(key);
		tmpBT.root().left(dArray[0]);
		tmpBT.root().right(dArray[1]);
		bt.hide();
		arr.hide();
		tmpBT.show();
		traverse_color(tmpBT.root(), "white");
		tmpBT.layout();
		jsav.step();

		caption_label.text(caption_text + "Use " + key + " to replace " + nArray[0] + " and " + nArray[1] + ": ");
		shuffle(nArray, tArray, dArray, key, node);
		bt.hide();
		tmpBT.hide();
		arr = jsav.ds.array(dArray);
		jsav.step();
	}	
}

// traverse to re-set background color of the entire tree
var traverse_color = function(node, col) {
	var val = node.value();

	// the node is an empty node	
	if (!val || val === "jsavnull") {	
		return;
	} 
	else {
		// if the node is an internal node, then display an circle
		if (node.left()) {
			node.css("background-color", col);
			traverse_color(node.left(),col);
		}
		if (node.right()) {
			node.css("background-color", col);
			traverse_color(node.right(),col);
		}
		// if the node is a leaf node, then display an rectangle
		else { 
			if (node.value().indexOf("<br />") > 0) {
				node.css({"height": "90px", "width": "45px", "border-radius":1, "background-color":"YELLOW"});	
			}
			else
			//node.css({"background-color": col, "width": "46px", "height": "46px", "-moz-border-radius": "23px", "-webkit-border-radius": "23px", "border-radius": "23px"});
			node.css({"height": "90px", "width": "45px", "background-color": col, "border-radius": "23px"});
		}
	}
}
    
	var jsav = new JSAV("av");
	var bt = jsav.ds.bintree();	// used to store the HuffmanCoding tree
	var tmpBT = jsav.ds.bintree();	// used to display the intermediate process for tree construction
	var caption_label = jsav.label("Huffman Coding Tree Construction", {before: bt});
	var caption_text = "";

	// userArry: an array to store the number and character
	var userArray = new Array();
	userArray[0] = 32;
	userArray[1] = "C";
	userArray[2] = 42;
	userArray[3] = "D";
	userArray[4] = 120;
	userArray[5] = "E";
	userArray[6] = 7;
	userArray[7] = "K"
	userArray[8] = 42;
	userArray[9] = "L"
	userArray[10] = 24;
	userArray[11] = "M";
	userArray[12] = 37;
	userArray[13] = "U";
	userArray[14] = 2;
	userArray[15] = "Z";

	// treeArray: an array to store the information of HuffmanCodingTree
	var treeArray = new Array();

	// numArray: used for logic control
	var numArray = new Array();

	// disArray: used for display control
	var disArray = new Array();

	// initialization for all the arrays
	for (var i = 0, j = 0; i < userArray.length - 1; i += 2, j++) {
		value = userArray[i] + "<br />" + userArray[i + 1];
		treeArray[j] = bt.newNode(value);
		disArray[j] = value;
		numArray[j] = userArray[i];
	}

	// an array to control the display
	arr = jsav.ds.array(disArray);
	caption_label.text(caption_text + "The initial data are as follows: the first line is frequency and the second line is the chracter");
	bt.hide();
	tmpBT.hide();
	jsav.step();

	// building the HuffmanCoding tree
	huffTree_animation(numArray, treeArray, disArray);

	traverse_color(bt.root(), "white");
	tmpBT.layout();
	tmpBT.hide();
	bt.show();
	bt.layout();
    jsav.recorded(); // done recording changes, will rewind
    
    $(".jsavtreenode").live("hover", function() {
	//console.log($(this).text(), $(this).offset().left, $(this).offset().top);
    });
    $("path").live("hover", function() {
	//console.log($(this).attr("d"));
    });
