
$( document ).ready(function() {
  
    $('textarea').keydown(function (e) {
        var keyCode = e.keyCode || e.which;

        if (keyCode === 9) {
            e.preventDefault();
            var start = this.selectionStart;
            var end = this.selectionEnd;

            // set textarea value to: text before caret + tab + text after caret
            spaces = "    ";
            this.value = this.value.substring(0, start) + spaces + this.value.substring(end);

            // put caret at right position again
            this.selectionStart = this.selectionEnd = start + spaces.length;
        }
    });
  
});  
