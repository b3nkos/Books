fun main() {
    val secret = 4
    var guess = readlnOrNull()?.toInt() ?: 0

    // Loop until the guess is correct
    while (guess != secret) {
        println("Guess: $guess")

        if (guess < secret) {
            println("Too low!")
        } else if (guess > secret) {
            println("Too high!")
        }

        guess += 1
    }

    println("Correct! You win! \uD83C\uDF89")
}