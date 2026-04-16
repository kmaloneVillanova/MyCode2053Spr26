console.log(document);




function testTheDom() {
    nodeList=document.getElementsByTagName("li");
    console.log(nodeList);
    for (let node of nodeList) {
        console.log("node"+node.textContent);
    }
    cnode=document.getElementById('checking');
    balance=cnode.textContent;
    console.log(balance);
    cnode.textContent="changed";
    // balance=parseInt(balance)+100;
    // cnode.textContent=balance;
}