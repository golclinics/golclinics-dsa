
//function that reverse array of integers
fun reverse(a: ArrayList<Int>): ArrayList<Int>{
    val copyA = ArrayList<Int>()
    for (i in a.size - 1 downTo 0){
        copyA.add(a[i])
    }
    return copyA
}

fun main(args: Array<String>) {
    //test
    val a = arrayListOf(1,2,5,6)
    println(reverse(a).toString())
}