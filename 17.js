//
//
// var tick = process.hrtime()
var tick = Date.now();

function spin(N, start=0, stop=2017) {
  var p = 0
  var z = 0
  var neigh = 0

  for (let i = 1; i < stop + 1; i++) {
    p = ((p + N) % i) + 1

    if (((p - 1) % i) == z) {
      neigh = i
    } else if (((p - 1) % i) === (z - 1)) {
      z += 1
    }
  }

  // var tock = process.hrtime(tick)
  var tock = Date.now();
  process.stdout.write(`time: ${(tock - tick) / 1000} neigh: ${neigh}\n`)
  return neigh
}

spin(329, 0, 50000000)

