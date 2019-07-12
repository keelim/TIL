// 2019 07 13
fun main() {
    val t = Thread(object : Runnable {
        override fun run() {
            println("hello kotlin")
        }

    })

    val data = object {
        var x = 1
        var y = 1
    }

    println("${data.x}, ${data.y}")

    val data1 = object {}
}

class MyClass {
    public fun publicFun() = object {
        var x = 111

    }

    private fun publicFun1() = object {
        var x = 111

    }

    fun print() {
        println(publicFun())
        println(publicFun1())
    }
}

//1
object CountManager {
    var count = 0
}

fun main1() {
    CountManager.count++
    CountManager.count++
    CountManager.count++
    CountManager.count++
    CountManager.count++
}


object MyClass_1{
    init {
        println("create MyClass_1")
    }
}

object MyClass_2{
    init {
        println("create MyClass_2")
    }
}

object MyClass_3{
    init {
        println("create MyClass_3")
    }
}
