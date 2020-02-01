function removeTagByTagName(f="footer") {
    var ele = document.getElementsByTagName(f);
    return ele[0].parentNode.removeChild(ele[0]);
}
removeTagByTagName();