//make a function that prints the nth prime number


function nthPrime(n) {
    var primes = [2];
    var i = 3;
    while (primes.length < n) {
        var isPrime = true;
        for (var j = 0; j < primes.length; j++) {
            if (i % primes[j] === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push(i);
        }
        i++;
    }
    return primes[primes.length - 1];
}

console.log(nthPrime(10001));
//output: 104743
//time: 0.000s
//memory: 37.8MB
//