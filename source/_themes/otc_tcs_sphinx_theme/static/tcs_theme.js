var i;
var contents = document.getElementsByClassName("content-collapse section");

var bashDollarDivs = document.getElementsByClassName("bash-dollars highlight-bash"); 

for (i = 0; i< bashDollarDivs.length; i++) {
    _pre = bashDollarDivs[i].querySelectorAll("pre");
    for (j = 0; j < _pre.length; j++) {
      console.log(_pre[j]);
      _pre[j].innerHTML="<span class='bash-dollar'>"+(_pre[j].textContent.split("\n").filter(Boolean).join("</span>\n<span class='bash-dollar'>"))+"</span>";
    }
}

//needed for nested collapsible sections - otherwise the top container 
//won't resize after expanding a child.
function resetActiveCollapsedSections() {

  var sections = document.getElementsByClassName("content-collapse section");

  //for (i = 0; i < sections.length; i++) {
  for (i = sections.length -1; i >= 0; i-- ){

    if (sections[i].style.maxHeight != "0px"){
       sections[i].style.maxHeight = sections[i].scrollHeight + "px";
    }
  }
}

for (i = 0; i < contents.length; i++) {

  //Make sure the "content-collapse section" class is occurring in <div>
  if (contents[i].tagName.toLowerCase() == 'div') {
    var element = contents[i].children[0];
    var element_type = element.tagName.toLowerCase();
    var btn_id;
    var divElement;

    divElement = contents[i];
    btn_id = contents[i].id;

    //if the next element is a span skip to the header
    if (element_type == 'span') {
      element = contents[i].children[1];
      element_type = element.tagName.toLowerCase();
    } else {
      divElement.id = "";
    }

    var btn = document.createElement("BUTTON");
    //If it is a header capture which level and pass on to button
    if (element_type.length == 2 && element_type[0] == 'h') {
      var newClass = 'clps' + element_type[1];
      //collapses the section by default only if javascript is working
      contents[i].style.maxHeight = 0;
      //Build the button and define behavior
      btn.className += " " + newClass;
      btn.innerHTML = element.innerHTML;
      btn.className += " collapsible";
      btn.id = btn_id;
      btn.addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight != "0px"){
          content.style.maxHeight = 0;
        } else {
          content.style.maxHeight = content.scrollHeight + "px";
        } 
        resetActiveCollapsedSections(); //reset the size of parent containers
      });

      //Add the button to the page and remove the header
      contents[i].parentNode.insertBefore(btn, contents[i]);
      contents[i].removeChild(element);
    }
  }
}
