

function add_comma(x) {
     return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
 }

function full_total(c) {return (weeks_value*c*1.07);
}

function show_cart_total() {alert("Thank you for renting with us! Your total was: $"+add_comma(cart_total)); }
