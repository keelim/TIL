// start
fun main() {
    test()
}

fun test() {
    val a: Int? = 10000
    val b: Int? = 10000

    println("${a === b}")
    println("${a === b}")
}

// 2019 07 03
// package && return and jumps
fun foo3(){
    var ints = listOf(0, 1, 2, 3)
    ints.forEach label@{
        if(it == 1) return@label
        print(it)
    }
    print("End")
}

fun foo4(){
    var ints = listOf(0, 1, 2, 3)
    ints.forEach {
        if(it == 1) return@forEach
        print(it)
    }
    print("End")
}