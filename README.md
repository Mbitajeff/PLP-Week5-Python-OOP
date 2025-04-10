# PLP Week 5: Python OOP Assignment  
**Programming Lab Project**  
*Demonstrating Class Design, Inheritance, and Polymorphism*  

---

## 🏗️ Assignment 1: Superhero Class Hierarchy  
**Objective**: Implement OOP concepts using a `Superhero` class with encapsulation and inheritance.  

### Key Features  
- **Base Class**: `Superhero` with:  
  - Public (`name`), protected (`_secret_identity`), and private (`__weakness`) attributes  
  - Methods like `introduce()`, `use_power()`, and `save_civilians()`  
- **Inherited Class**: `FlyingSuperhero` extending functionality with `fly()` and method overriding.  

### Code Snippet  
```python  
superman = FlyingSuperhero("Superman", "Clark Kent", ["flight", "x-ray vision"], "kryptonite", 50000)  
superman.fly()  # Output: "Superman soars through the air at 50000 feet!"  
```  

---

## 🎭 Assignment 2: Animal Polymorphism  
**Objective**: Implement polymorphic behavior through animal movement.  

### Classes & Behaviors  
| Class | `move()` Output | `speak()` Output |  
|-------|-----------------|------------------|  
| `Dog` | "Runs happily! 🐕" | "Woof! Woof!" |  
| `Fish` | "Swims gracefully! 🐟" | "Blub blub..." |  
| `Bird` | "Flies high! 🦅" | "Tweet tweet!" |  

### Demo  
```python  
for animal in [Dog("Buddy"), Fish("Nemo")]:  
    print(animal.move())  # Unique per animal  
```  

---

## 📌 How to Run  
1. Clone the repo:  
   ```bash  
   git clone https://github.com/Mbitajeff/PLP-Week5-OOP-Concepts.git  
   ```  
2. Run the scripts:  
   ```bash  
   python superhero.py  
   python animals.py  
   ```  

---

## 📚 Key OOP Concepts Covered  
| Concept | Example |  
|---------|---------|  
| **Encapsulation** | Private `__weakness` attribute |  
| **Inheritance** | `FlyingSuperhero` subclass |  
| **Polymorphism** | Different `move()` behaviors |  
| **Method Overriding** | Custom `save_civilians()` in subclass |  

---

## 🔗 Related Resources  
- [Python OOP Documentation](https://docs.python.org/3/tutorial/classes.html)  
- [PLP Course Materials](#) *(PLP LMS)*  

---

*** Note**: Submitted for **PLP Week 5** assignment at PLP.  
