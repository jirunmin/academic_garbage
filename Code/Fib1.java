public class Fib1 {
    static int fib1(int n){
        if(n <= 1)
            return 1;
        else
            return fib1(n-1) + fib1(n-2);
    }
}
