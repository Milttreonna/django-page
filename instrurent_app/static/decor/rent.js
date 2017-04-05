

function add_comma(x) {
     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
 }

function full_total(c) {return (weeks_value*c*1.07);
}

function show_cart_total() {alert("Thank you for renting with us! Your total was: $"+add_comma(cart_total)); }

var item_total= function(){
  weeks_value= document.getElementById("Weeks").value;
  customer_total=full_total(instrument_cost).toFixed(2);
  document.getElementById("Total").innerHTML="$"+customer_total;
}

var add_to_cart = function(){
     cart_total=Number(cart_total)
     cart_total+=Number(customer_total)
     cart_total=(cart_total.toFixed(2));
     document.getElementById("complete_total").innerHTML="$"+add_comma(cart_total);
    console.log(cart_total);
    }
