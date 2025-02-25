## Revisiting Polymorphism and anticipating relevant issues for the project

### **Stage 1**. Processing Computation expressions with numbers only

Develop the classes shown in the UML class diagram shown at the end of this document, as specified in the Javadoc attached to this script.

![Stage 1](/LAB1/images/stage_1.png)

    After that, create a Main class and insert there the main() method. Its execution has to perform the following tasks:

    1. Create an object Computation for evaluating the expression: 15 + 5
    2. Evaluate this Computation object and present the result
    3. Create an object Computation for evaluating the expression: 20 + 10
    4. Evaluate this Computation object and present the result

### **Stage 2**. Preparing the code for allowing more types of operands

You should note that the former UML class diagram only allows Computation objects with ONLY ONE TYPE OF OPERANDS: objects MyNumber.

![Stage 2](/LAB1/images/stage_2.png)

One of the goals is to process Computation objects which may have MyNumber objects or Variable objects as operands.

The first step for achieving this is to define an abstraction Operand, from which MyNumber and Variable classes shall be concrete versions.
Once defined this abstraction, you have to declare MyNumber as a class that implements the Operand interface.

After that, you have to change, in Computation and in Operator, any declaration of attribute or argument from MyNumber to Operand, as objects of both classes will not only deal with numbers, but with any type of operand (numbers or variables) in the final version.

Finally, you have to implement the abstraction SimpleExpression and declare that Computation is a class that implements it.
In this second stage you must generate a new program which implements the classes shown in the UML class diagram shown in the next page.

Note the most relevant changes in the diagram:
a) The method Operator::compute(Operand first, Operand second) has changed the declaration of the arguments: they are not MyNumber objects anymore. Now they are Operand objects. This allows to pass to this method objects instance of ANY class that IMPLEMENTS the interface Operand (i.e. any object which has a getValue() method returning a double value!!!).
b) The MyNumber class is now defined as a class that implements the Operand interface. This will allow to pass objects MyNumber as arguments to the Operator::compute(...) method.
c) Finally, the class Computation is declared as a class that implements the interface SimpleExpression. This is the first step for incorporating to the program another type of simple expression: the assignment.

    After that, create a Main class and insert there the main() method. Its execution has to perform the following tasks:

    1. Create an object Computation for evaluating the expression: 15 + 5
    2. Evaluate this Computation object and present the result
    3. Create an object Computation for evaluating the expression: 20 + 10
    4. Evaluate this Computation object and present the result
