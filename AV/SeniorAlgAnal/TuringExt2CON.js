/*global JSAV, document */
// Written by Cliff Shaffer

$(document).ready(function() {
  "use strict";
  var av = new JSAV("TuringExt2CON", {animationMode: "none"});
  var xleft = 375;
  var ytop = 10;
  var cellwidth = 20;
  var i;

  for (i = 0; i < 5; i++) {
    av.g.line(xleft + cellwidth,     ytop + i * cellwidth,
              xleft + 5 * cellwidth, ytop + i * cellwidth,
              {"stroke-width": 2});
    av.g.line(xleft + i * cellwidth, ytop,
              xleft + i * cellwidth, ytop + 4 * cellwidth,
              {"stroke-width": 2});
  }
  av.g.line(xleft, ytop, xleft + cellwidth, ytop,
            {"stroke-width": 2});
  av.g.line(xleft,             ytop + 4 * cellwidth,
            xleft + cellwidth, ytop + 4 * cellwidth,
            {"stroke-width": 2});

  av.label("$\\$$", {top: ytop + 16, left: xleft + 5});
  av.label("$a$", {top: ytop - 13, left: xleft + 5 + cellwidth});
  av.label("$b$", {top: ytop - 13, left: xleft + 5 + cellwidth * 2});
  av.label("$\\#$", {top: ytop - 13, left: xleft + 5 + cellwidth * 3});

  av.label("$1$", {top: ytop - 13 + cellwidth, left: xleft + 5 + cellwidth});
  av.label("$1$", {top: ytop - 13 + 3 * cellwidth,
                   left: xleft + 5 + 2 * cellwidth});

  av.label("$a$", {top: ytop - 13 + 2 * cellwidth,
                   left: xleft + 5 + cellwidth});
  av.label("$a$", {top: ytop - 13 + 2 * cellwidth,
                   left: xleft + 5 + cellwidth * 2});
  av.label("$\\#$", {top: ytop - 13 + 2 * cellwidth,
                     left: xleft + 5 + cellwidth * 3});

  av.label("$0$", {top: ytop - 13 + cellwidth * 4,
                   left: xleft + 5 + 0 * cellwidth});
  av.label("$1$", {top: ytop - 13 + cellwidth * 4,
                   left: xleft + 5 + 1 * cellwidth});
  av.label("$2$", {top: ytop - 13 + cellwidth * 4,
                   left: xleft + 5 + 2 * cellwidth});
  av.label("$3$", {top: ytop - 13 + cellwidth * 4,
                   left: xleft + 5 + 3 * cellwidth});
  av.label("$4$", {top: ytop - 13 + cellwidth * 4,
                   left: xleft + 5 + 4 * cellwidth});

  av.displayInit();
  av.recorded();
});
