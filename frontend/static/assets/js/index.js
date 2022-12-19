// convert the textarea to a CodeMirror editor
var editor = CodeMirror.fromTextArea(document.getElementsByClassName("code"), {
  lineNumbers: true,
  border: true,
  theme: "eclipse",
  mode: "application/json",
  gutters: ["CodeMirror-lint-markers"],
  styleActiveLine: true,
  lint: true
});