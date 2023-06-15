//Create a class called Product with attributes for name, price, and quantity.
//Implement a method to calculate the total value of the product (price * quantity).
//Create multiple objects of the Product class and calculate their total values.
class Product{
    constructor(name,price,quantity){
        this.name = name
        this.quantity = quantity
        this.price = price
    }
    calculateTotal(){
        return this.price * this.quantity
    }
}
let product1 = new Product("Soap",20,400)
let product2 = new Product("Rice",4,300)
let product3 = new  Product("Sweets",7,900)
product1.calculateTotal()
product2.calculateTotal()
product3.calculateTotal()


//Implement a class called Student with attributes for name, age, and grades (a
//list of integers). Include methods to calculate the average grade, display the
//student information, and determine if the student has passed (average grade >=60). 
//Create objects for the Student class and demonstrate the usage of these methods.
class Student{
    constructor(name,age,grades){
        this.name = name
        this.grades = []
        this.age = age

    }
    calculateAverage(grades){
        count = 0
        for(let i = 0;i<grades.length;i++){
            count += i;
            let average = count / length(grades);
            if(average >= 60){
                console.log("You have passed")
            }
            else{
                console.log("You have failed")
            }
        }
    }
    displayInformation(){
        console.log(`${this.Student}`)
        console.log(`${this.grades}`)
        console.log(`${this.grades}`)
    }
}

let student = new Student("Alice",24,[23,75,90,39])
student.displayInformation()
student.calculateAverage()

//Create a LibraryCatalog class that handles the cataloging and management of
//books in a library. Implement methods to add new books, search for books by
//title or author, keep track of available copies, and display book details.
class Library{
    constructor(book,author,copies){
        this.book = book
        this.author = author
        this.copies =  copies
    }
    addNewBook(new_book,author){
        return new_book && author
    }
    searchBook(author){
        return author
    }
    displayDetails(){
        console.log(`${this.book}`);
        console.log(`${this.author}`);
        console.log(`${this.copies}`)
    }
    availableBooks(){
        return this.copies
    }
}
let library = new Library("Born a crime","Trevor Noah",90)
library.addNewBook()
library.searchBook()
library.displayDetails()
library.availableBooks()