var clarinet_cost=152.36;
var drum_cost=118.30;
var piano_cost=221.13;
var violin_cost=91.00;
var eguitar_cost=117.00;
var aguitar_cost= 57.20;
var banjo_cost= 62.27;
var sax_cost=410.02;
var trumpet_cost=317.07;
var conga_cost=35.10;
var weeks_value="";
var customer_total="";
var cart_total=0;


function add_comma(x) {
     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
 }

function full_total(c) {return (weeks_value*c*1.07);
}

function show_cart_total() {alert("Thank you for renting with us! Your total was: $"+add_comma(cart_total)); }


var clarinetTotal = function() {
    weeks_value= document.getElementById("clarinetWeeks").value;
    customer_total=full_total(clarinet_cost).toFixed(2);
    document.getElementById("clarinetTotal").innerHTML="$"+customer_total;

}


var aguitarTotal =function() {
    weeks_value= document.getElementById("aguitarWeeks").value;
    customer_total=full_total(aguitar_cost).toFixed(2);
    document.getElementById("aguitarTotal").innerHTML="$"+customer_total;
}


var banjoTotal = function() {
 weeks_value= document.getElementById("banjoWeeks").value;
 customer_total=full_total(banjo_cost).toFixed(2);
    document.getElementById("banjoTotal").innerHTML="$"+customer_total;
}

var congaTotal = function() {
    weeks_value= document.getElementById("congaWeeks").value;
    customer_total=full_total(conga_cost).toFixed(2);
    document.getElementById("congaTotal").innerHTML="$"+customer_total;

}

var drumTotal= function() {
    weeks_value= document.getElementById("drumWeeks").value;
    customer_total=full_total(drum_cost).toFixed(2);
    document.getElementById("drumTotal").innerHTML="$"+customer_total;

}

var eguitarTotal= function(){
  weeks_value= document.getElementById("eguitarWeeks").value;
  customer_total=full_total(eguitar_cost).toFixed(2);
  document.getElementById("eguitarTotal").innerHTML="$"+customer_total;

}

var pianoTotal= function(){
  weeks_value= document.getElementById("pianoWeeks").value;
  customer_total=full_total(piano_cost).toFixed(2);
    document.getElementById("pianoTotal").innerHTML="$"+customer_total;

}

var saxTotal= function() {
  weeks_value= document.getElementById("saxWeeks").value;
  customer_total=full_total(sax_cost).toFixed(2);
    document.getElementById("saxTotal").innerHTML="$"+add_comma(customer_total);

}

var trumpetTotal= function(){
    weeks_value= document.getElementById("trumpetWeeks").value;
    customer_total=full_total(trumpet_cost).toFixed(2);
    document.getElementById("trumpetTotal").innerHTML="$"+add_comma(customer_total);

}

var violinTotal= function(){
  weeks_value= document.getElementById("violinWeeks").value;
  customer_total=full_total(violin_cost).toFixed(2);
    document.getElementById("violinTotal").innerHTML="$"+customer_total;

}

var add_to_cart = function(){
     cart_total=Number(cart_total)
     cart_total+=Number(customer_total)
     cart_total=(cart_total.toFixed(2));
     document.getElementById("complete_total").innerHTML="<img class='cart' src='images/cart2.png'> $"+add_comma(cart_total);
    console.log(cart_total);
    }
