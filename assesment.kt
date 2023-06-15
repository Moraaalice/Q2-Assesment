//Create a class called Product with attributes for name, price, and quantity.
//Implement a method to calculate the total value of the product (price * quantity).
//Create multiple objects of the Product class and calculate their total values.

class Product(var name:String,var price:Int,var quantity:Int){
    fun calculate_total(){
        return price*quantity
    }
}
product1 = Product("Rice",300,10)
product2 = Product("Soap",5,500)
product3 = Product("Flour",4,700)

println(product1.calculate_total()
println(product2.calculate_total()))
println(product3.calculate_total())

