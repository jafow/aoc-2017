# include <stdio.h>
#include <sys/time.h>
#include <sys/resource.h>

double get_time()
{
    struct timeval t;
    struct timezone tzp;
    gettimeofday(&t, &tzp);
    return t.tv_sec + t.tv_usec*1e-6;
}

int main()
{
    int p, k, z, res;
    int n = 329;
    int end = 50000000;
    double tick = get_time();

    p = 0;
    k = 0;
    z = 0;
    res = 0;


    for (int i = 1; i < end; i++) {
        p = ((p + n) % i) + 1;
        k = (p - 1) % i;
        if (k == z) {
            res = i;
        } else if (k == (z - 1)) {
            z++;
        }
    }

    double tock = get_time();
    double t = tock - tick;
    printf("time is %f and res is %d\n", t, res);
}
